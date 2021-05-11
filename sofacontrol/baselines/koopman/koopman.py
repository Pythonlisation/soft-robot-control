import numpy as np
from scipy.interpolate import interp1d

from sofacontrol.baselines.koopman.koopman_utils import KoopmanData
from sofacontrol.baselines.ros import MPCClientNode
from sofacontrol.closed_loop_controller import TemplateController

# NOTE: Only tested on a single output node, position only (3 dim), and a delay of 1. To test with larger delays and
# compare with MATLAB code

class KoopmanMPC(TemplateController):
    """
    Koopman MPC interface with Sofa. Similar style to sofacontrol/tpwl/controllers.py. Interfaces with Sofa and ROS
    through client node. Not yet designed to be real-time capable
    """

    def __init__(self, dyn_sys, delay=2, u0=None, wait=True, **kwargs):
        super().__init__()

        # Related to Controllers.py file
        self.dyn_sys = dyn_sys

        self.input_dim = self.dyn_sys.m
        self.state_dim = self.dyn_sys.N

        self.dt = self.dyn_sys.Ts

        self.observer = KoopmanObserver()

        self.Y = kwargs.get('Y')
        if u0 is not None:
            self.u0 = u0
        else:
            self.u0 = np.zeros(self.input_dim)

        self.t_compute = 0.
        self.u = self.u0

        self.solve_times = []

        self.data = KoopmanData(self.dyn_sys.scale, self.dyn_sys.delays)

        # self.planning_horizon = kwargs.get('planning_horizon', 10)
        self.rollout_horizon = kwargs.get('rollout_horizon', 1)
        # Consider interpolation or input hold, used if sim dt is different than system dt
        self.input_hold = kwargs.get('input_hold', False)

        # Related to MPC Solver Node
        self.t_opt = None
        self.u_opt = None
        self.x_opt = None
        self.u_bar = None
        self.x_bar = None

        self.x_opt_full = None

        self.wait = wait

        self.t_next_solve = 0
        self.initiailzed = False

        self.MPC = MPCClientNode()

        self.t_delay = delay

    def set_sim_timestep(self, dt):
        """
        Required for interfacing with Sofa
        """
        self.sim_dt = dt

    def compute_policy(self, t_step, zeta_belief):
        xlift_curr = np.asarray(self.dyn_sys.lift_data(*zeta_belief))  # x_belief is directly y_belief in this case
        self.MPC.send_request(round(t_step, 4), xlift_curr, wait=True)

        if not self.MPC.check_if_done():  # If running with wait=True, this is always False
            print('GuSTO cannot provide real-time compatibility, consider modifying problem')
            self.MPC.force_wait()

        t_opt_p, u_opt_p, x_opt_p, t_solve = self.MPC.get_solution(self.state_dim,
                                                                   self.input_dim)  # Why do we need state dim and input dim here??
        t_opt_p = np.round(t_opt_p, 4)
        u_opt_p = self.data.scaling.scale_up(u=u_opt_p)

        self.solve_times.append(t_solve)

        # Downsample and only take the first N_replan dt steps
        u_opt_intp = interp1d(t_opt_p, np.vstack((u_opt_p, u_opt_p[-1, :])), axis=0)
        x_opt_intp = interp1d(t_opt_p, x_opt_p, axis=0)

        if self.t_opt is None:
            t_opt_new = self.dt * np.arange(self.rollout_horizon + 1)
            u_opt_new = u_opt_intp(t_opt_new)
            x_opt_new = x_opt_intp(t_opt_new)
            self.t_opt = t_opt_new
            self.u_opt = u_opt_new
            self.x_opt = x_opt_new
            self.x_opt_full = np.expand_dims(x_opt_p, axis=0)
        else:
            t_opt_new = self.t_opt[-1] + self.dt * np.arange(self.rollout_horizon + 1)
            u_opt_new = u_opt_intp(t_opt_new)
            x_opt_new = x_opt_intp(t_opt_new)
            self.t_opt = np.concatenate((self.t_opt, t_opt_new[1:]))
            self.t_opt = np.round(self.t_opt, 4)
            self.u_opt = np.concatenate((self.u_opt[:-1, :], u_opt_new))
            self.x_opt = np.concatenate((self.x_opt, x_opt_new[1:, :]))
            self.x_opt_full = np.concatenate((self.x_opt_full, np.expand_dims(x_opt_p, axis=0)))

        # Define interpolation functions for new optimal trajectory, note
        # that these include traj from time t = 0 onward

        if self.input_hold:
            self.u_bar = interp1d(self.t_opt, self.u_opt, kind='previous', axis=0)
            self.x_bar = interp1d(self.t_opt, self.x_opt, kind='previous', axis=0)
        else:
            self.u_bar = interp1d(self.t_opt, self.u_opt, axis=0)
            self.x_bar = interp1d(self.t_opt, self.x_opt, axis=0)

    def recompute_policy(self, t_step):
        step = round(round(t_step, 4) / self.dt)
        i = int(step % self.rollout_horizon)
        return True if i == 0 else False  # Recompute if rollout horizon reached (more explicit than: not i)

    def compute_input(self, t_step, z_belief):
        self.MPC.force_spin()

        u = self.u_bar(t_step)
        return u

    def evaluate(self, sim_time, y, x, u_prev):
        """
        Update observer at each step of simulation (each function call). Updates controller at controller frequency
        :param time: Time in the simulation [s]
        :param y: Measurement at time time
        :param x: Full order state at time time. Only used at start of control if using an observer, for initialization
        """
        # print(sim_time)
        sim_time = round(sim_time, 4)
        # Startup portion of controller, before OCP controller is activated
        self.observer.update(None, y, None)

        if self.Y is not None and not self.Y.contains(y):
            y = self.Y.project_to_polyhedron(y)
        self.data.add_measurement(y, u_prev)
        if round(sim_time, 4) < round(self.t_delay, 4):
            self.u = self.u0

        # Optimal controller is active
        else:
            # Updating controller (self.u) and/or policy (if first step or receding horizon)
            if round(sim_time - self.t_delay, 4) >= round(self.t_compute, 4):  # self.t_compute set to
                zeta_belief = self.data.get_zeta()

                if self.recompute_policy(self.t_compute):
                    self.compute_policy(self.t_compute, zeta_belief)

                self.u = self.compute_input(self.t_compute, zeta_belief)

                self.t_compute += self.dt  # Increment t_compute
                self.t_compute = round(self.t_compute, 4)
        self.u = np.atleast_1d(self.u)
        return self.u.copy()  # Returns copy of self.u

    def save_controller_info(self):
        info = dict()
        info['t_opt'] = self.t_opt
        info['u_opt'] = self.u_opt
        info['z_opt'] = self.data.scaling.scale_up(y=(self.dyn_sys.H @ self.x_opt.T).T)
        info['zopt_full'] = self.data.scaling.scale_up(
            y=np.einsum("ij, klj -> ikl", self.dyn_sys.H, self.x_opt_full).T).transpose((1, 0, 2))
        info['solve_times'] = self.solve_times
        info['rollout_time'] = self.rollout_horizon * self.dt
        return info


class KoopmanObserver:
    def __init__(self):
        self.z = None

    def update(self, u, y, dt, x=None):
        self.z = y
