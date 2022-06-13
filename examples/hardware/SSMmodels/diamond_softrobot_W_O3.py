import numpy as np

def diamond_softrobot_W_O3(in1):
    #diamond_softrobot_W_O3
    #    W_sym = diamond_softrobot_W_O3(IN1)
    
    #    This function was generated by the Symbolic Math Toolbox version 9.0.
    #    09-Jun-2022 09:53:22
    
    p1 = in1[0]
    p2 = in1[1]
    p3 = in1[2]
    p4 = in1[3]
    p5 = in1[4]
    p6 = in1[5]
    t2 = np.power(p1, 2)
    t3 = np.power(p1, 3)
    t4 = np.power(p2, 2)
    t5 = np.power(p2, 3)
    t6 = np.power(p3, 2)
    t7 = np.power(p3, 3)
    t8 = np.power(p4, 2)
    t9 = np.power(p4, 3)
    t10 = np.power(p5, 2)
    t11 = np.power(p5, 3)
    t12 = np.power(p6, 2)
    t13 = np.power(p6, 3)
    et1 = p1*(-9.727698250551137)+p2*6.865188500317576-p3*1.761785885372428e+1-p4*1.550304736590345e-4-p5*2.667399698229866e-4
    et2 = p6*(-1.362880341131159e-3)-t2*1.219292318088505e-2+t3*2.713298758606197e-4-t4*8.284226294557079e-3-t5*1.596227588915326e-4
    et3 = t6*(-3.401271530775543e-2)+t7*1.19482405541617e-4+t8*8.488872290770679e-6-t9*3.022865146976468e-8
    et4 = t10*(-5.71226085214405e-6)+t11*4.193068283395022e-8+t12*8.620983334355097e-6-t13*7.672978729168427e-9
    et5 = p1*p2*2.09840747432353e-4+p1*p3*6.201681921844369e-3+p1*p4*1.451266640900132e-4+p2*p3*2.969176110933215e-3+p1*p5*7.875253195987065e-4
    et6 = p2*p4*(-8.647758622340964e-4)+p1*p6*6.142537529192538e-4+p2*p5*2.923997396224361e-5+p3*p4*7.428830594137908e-4
    et7 = p2*p6*1.660106986582672e-5-p3*p5*8.633173420354272e-4-p3*p6*2.60137444535535e-4-p4*p5*9.532231857905149e-6
    et8 = p4*p6*(-3.934402297528297e-6)+p5*p6*2.579991913672964e-5+p2*t2*7.287045711630805e-6+p1*t4*6.714559483766225e-5
    et9 = p3*t2*(-2.599066960323397e-4)+p4*t2*1.193203869447833e-6-p1*t6*5.823516018001091e-4-p3*t4*4.784611757493619e-5
    et10 = p5*t2*(-1.206797637482977e-4)+p2*t6*3.618680891952788e-4+p4*t4*2.949636587474276e-6-p6*t2*2.067699857140157e-5
    et11 = p1*t8*9.550238607526884e-8+p5*t4*1.794243937833698e-6-p2*t8*4.618444124893761e-6-p4*t6*3.115767722532755e-5
    et12 = p6*t4*2.521249926250314e-5-p1*t10*6.846597427855011e-6+p3*t8*1.801631494094947e-6+p5*t6*2.027018777544981e-5
    et13 = p2*t10*(-3.019552203097329e-7)-p6*t6*8.857100530409708e-6+p1*t12*1.808765559283196e-6+p3*t10*1.343476075773126e-6
    et14 = p5*t8*(-3.326708627819731e-8)-p2*t12*1.366457902625932e-6+p4*t10*1.877867013684019e-8-p6*t8*2.697514944372818e-8
    et15 = p3*t12*(-1.849832143904054e-7)+p4*t12*9.084332864521499e-8-p6*t10*7.852982477690026e-8-p5*t12*7.533736150556809e-8
    et16 = p1*p2*p3*(-1.644780543728266e-4)+p1*p2*p4*1.189556875759288e-4+p1*p2*p5*4.577800665478944e-6-p1*p3*p4*1.830482046647696e-5
    et17 = p1*p2*p6*2.310508980572645e-5-p1*p3*p5*1.515782326207408e-5+p2*p3*p4*6.617631191700237e-6+p1*p3*p6*2.573249025594845e-5
    et18 = p1*p4*p5*4.333509803454637e-6-p2*p3*p5*5.976610035219864e-5-p1*p4*p6*1.723565387084257e-6-p2*p3*p6*7.909527044503304e-6
    et19 = p2*p4*p5*5.975367965398883e-6+p1*p5*p6*5.197580540417555e-6-p2*p4*p6*4.691923904829638e-6-p3*p4*p5*1.070665164439533e-8
    et20 = p2*p5*p6*(-8.71385577886199e-7)-p3*p4*p6*1.897838600530589e-7+p3*p5*p6*3.779587357598472e-7+p4*p5*p6*8.179335043962599e-8
    et21 = p1*1.117242042264593e+1+p2*1.953558104059429e+1+p3*9.699551286091389e-1+p4*2.188001248949106e-5+p5*1.600464871219129e-3
    et22 = p6*1.276216918857141e-3+t2*3.601843243534753e-3+t3*1.187995556469911e-5+t4*1.126549348096727e-3-t5*6.704036173879092e-5
    et23 = t6*2.716926716660897e-3+t7*3.696389060159081e-5-t8*2.692716178989507e-6-t9*3.792483896997471e-9
    et24 = t10*1.856907111794385e-6+t11*2.752696966320657e-8-t12*3.828215677428284e-7-t13*8.842154640360282e-9
    et25 = p1*p2*1.167944862230543e-3-p1*p3*1.45844149377814e-2+p1*p4*1.525535799446708e-5-p2*p3*2.085318787952783e-2+p1*p5*6.627262899808744e-4
    et26 = p2*p4*(-2.873774207847776e-4)-p1*p6*4.394011153753786e-4-p2*p5*9.703111965807575e-5-p3*p4*9.833848228060337e-4
    et27 = p2*p6*(-8.695576142536684e-4)-p3*p5*1.642594430033269e-3-p3*p6*1.175936290038677e-4-p4*p5*1.833130426779725e-5
    et28 = p4*p6*7.647275369725564e-6+p5*p6*2.110463882327821e-5-p2*t2*2.094293576361557e-4-p1*t4*2.528861789219185e-5
    et29 = p3*t2*(-1.407494124981882e-4)+p4*t2*2.760382960888048e-6+p1*t6*9.914743456179308e-5-p3*t4*2.125258657613246e-4
    et30 = p5*t2*(-6.501663272441875e-5)+p2*t6*3.38116353563279e-4+p4*t4*6.463296175928295e-5-p6*t2*6.543882991582231e-6
    et31 = p1*t8*3.420371522126054e-7+p5*t4*1.026869157060841e-5-p2*t8*5.990939667615497e-6-p4*t6*2.180953615203219e-6
    et32 = p6*t4*(-7.84058533354865e-6)+p1*t10*3.581617684398008e-6-p3*t8*1.150449215820274e-6-p5*t6*2.600924815795868e-6
    et33 = p2*t10*7.504528236927804e-8-p6*t6*3.926067936914175e-6-p1*t12*6.758453687351197e-7+p3*t10*2.21073188368866e-6
    et34 = p5*t8*(-2.448065967832277e-8)-p2*t12*1.354036755782364e-6+p4*t10*3.583006136982124e-8+p6*t8*1.029976404955879e-8
    et35 = p3*t12*8.944485459430925e-8-p4*t12*1.367373382454473e-9-p6*t10*3.896623661183683e-8-p5*t12*5.791749785874994e-8
    et36 = p1*p2*p3*(-1.045218709540565e-4)+p1*p2*p4*7.95718768761858e-5-p1*p2*p5*4.613959684711536e-5+p1*p3*p4*8.1528744459987e-6
    et37 = p1*p2*p6*(-6.155072906182494e-6)+p1*p3*p5*1.507221220991276e-4-p2*p3*p4*1.291425134699333e-4+p1*p3*p6*2.018386071305343e-5
    et38 = p1*p4*p5*7.122444639380829e-6+p2*p3*p5*2.151064267685876e-6+p1*p4*p6*1.291684746432357e-6+p2*p3*p6*1.842801962406498e-6
    et39 = p2*p4*p5*(-2.813818969028781e-6)+p1*p5*p6*2.394461116605039e-6-p2*p4*p6*1.416238170438421e-6-p3*p4*p5*4.101599554795592e-7
    et40 = p2*p5*p6*(-2.756895156971852e-6)+p3*p4*p6*2.912011870390991e-7+p3*p5*p6*5.874747117905324e-7+p4*p5*p6*9.486975068400655e-8
    et41 = p1*1.719242965911668e+1-p2*9.137638766332906-p3*1.176944108716569e+1+p4*1.765043131489337e-3-p5*1.681976434446336e-3
    et42 = p6*(-2.251775203565506e-3)-t2*7.49950266845489e-3+t3*2.726944098787451e-5-t4*5.238270534926555e-3+t5*4.375275290322965e-5
    et43 = t6*(-1.691029439119161e-2)+t7*9.647723523407279e-5-t8*7.441558301985243e-6+t9*1.200125371869626e-8
    et44 = t10*3.76550578362671e-6-t11*6.410110765783715e-10+t12*3.942288984498032e-8+t13*2.609424723885081e-9
    et45 = p1*p2*(-3.533019916750576e-3)-p1*p3*2.608764903211459e-2+p1*p4*1.669338425107631e-4+p2*p3*1.354015650638661e-2-p1*p5*8.347936343343429e-4
    et46 = p2*p4*4.9646791938825e-4-p1*p6*6.095696788812828e-4+p2*p5*3.113390392816338e-4-p3*p4*1.109605070254429e-3+p2*p6*5.671142256644806e-4
    et47 = p3*p5*5.9032258226766e-4-p3*p6*7.085901905952831e-5+p4*p5*5.937656774468269e-6+p4*p6*5.939856933333463e-6
    et48 = p5*p6*(-1.41843456695049e-5)+p2*t2*1.378578916272957e-4-p1*t4*2.308356614135144e-4-p3*t2*4.52759191947724e-5
    et49 = p4*t2*9.409878479597145e-6+p1*t6*1.066775644290389e-4-p3*t4*1.599329649161375e-4-p5*t2*3.285200724495891e-5
    et50 = p2*t6*(-7.58389366743372e-5)+p4*t4*1.370957733960016e-4+p6*t2*1.334702430841829e-5-p1*t8*4.343944527000455e-8
    et51 = p5*t4*(-1.098266476011875e-5)-p2*t8*1.508861964492001e-6-p4*t6*1.356491273810221e-5+p6*t4*9.54103759517592e-6
    et52 = p1*t10*1.03088751235512e-6-p3*t8*1.361872617303496e-6+p5*t6*8.001506331077553e-6+p2*t10*3.066750178307526e-7
    et53 = p6*t6*(-6.223129642797081e-6)+p1*t12*7.892871928552055e-7-p3*t10*5.243463633651615e-8+p5*t8*8.466411437359393e-11
    et54 = p2*t12*(-8.556698198298432e-7)-p4*t10*4.293511216984839e-9+p6*t8*1.406331562122167e-9-p3*t12*2.120784184797389e-7
    et55 = p4*t12*(-1.989509976362382e-9)+p6*t10*4.636982111529696e-8-p5*t12*4.413159087779146e-8-p1*p2*p3*2.359212587884988e-4
    et56 = p1*p2*p4*1.762858861761444e-5-p1*p2*p5*1.221247844546884e-4-p1*p3*p4*1.001755217347838e-5+p1*p2*p6*6.619998270426581e-6
    et57 = p1*p3*p5*(-1.437750509372719e-4)+p2*p3*p4*1.255788627862697e-4+p1*p3*p6*1.591890651754119e-5+p1*p4*p5*1.128640704056064e-6
    et58 = p2*p3*p5*(-1.120192024697585e-5)+p1*p4*p6*1.440821994896057e-6-p2*p3*p6*9.555751940589175e-6-p2*p4*p5*6.936224728464066e-7
    et59 = p1*p5*p6*(-7.054943142132471e-6)+p2*p4*p6*6.91720428007818e-6+p3*p4*p5*4.84291680328487e-7+p2*p5*p6*4.439302437921493e-7
    et60 = p3*p4*p6*(-1.169229536148692e-7)-p3*p5*p6*2.91733228123856e-7-p4*p5*p6*1.566876167979157e-8
    et61 = p1*(-3.053053255046954e-1)-p2*1.233108439580624+p3*8.077424959090557e-1-p4*9.786545476162742+p5*6.879512728204232
    et62 = p6*(-1.749011167806636e+1)+t2*4.540658920091793e-2-t3*7.033316794920919e-4+t4*1.320871365443036e-3+t5*8.903891716385621e-4
    et63 = t6*(-9.379193372067603e-2)-t7*5.082209920168278e-4-t8*5.945757814801659e-5+t9*1.010072294257957e-6+t10*1.285205300536023e-4
    et64 = t11*(-1.667039569155189e-6)+t12*1.099222051102508e-4-t13*1.360499082116224e-6-p1*p2*8.668064957360259e-2
    et65 = p1*p3*(-6.221510694448754e-1)-p1*p4*2.290531858803826e-2+p2*p3*2.455054525322188e-1-p1*p5*5.434722898786241e-3+p2*p4*4.031226240573754e-3
    et66 = p1*p6*1.270471770336778e-2-p2*p5*1.085831382785768e-2-p3*p4*1.004241454723056e-2-p2*p6*9.226960507660798e-3+p3*p5*6.883073834522199e-3
    et67 = p3*p6*(-7.296358667769895e-2)+p4*p5*2.507011190257327e-4+p4*p6*1.748628969336519e-3-p5*p6*1.515779072700964e-3-p2*t2*1.156868446147097e-3
    et68 = p1*t4*(-4.391292115166507e-3)+p3*t2*1.755689676841734e-2+p4*t2*9.908151203355867e-4+p1*t6*9.879713549592109e-4+p3*t4*1.403791387319164e-2
    et69 = p5*t2*(-1.287130955344061e-3)-p2*t6*9.922013113181498e-3+p4*t4*1.99632164580775e-3+p6*t2*1.496041420340354e-3+p1*t8*4.531396392118683e-5
    et70 = p5*t4*(-4.141362418620794e-4)+p2*t8*8.610158720069092e-5-p4*t6*4.109424407943487e-4+p6*t4*7.653742731343673e-4
    et71 = p1*t10*2.0195666605988e-4-p3*t8*6.967964186489149e-5+p5*t6*3.555902907112034e-4-p2*t10*1.858179243069705e-5
    et72 = p6*t6*5.35754552616316e-4-p1*t12*1.893872879372939e-5-p3*t10*1.158188425347629e-4+p5*t8*9.473937746870504e-7
    et73 = p2*t12*2.786069890014774e-5-p4*t10*2.183928187958191e-6+p6*t8*2.082458165854854e-6+p3*t12*1.437557794627802e-5
    et74 = p4*t12*4.181809742595064e-7+p6*t10*3.408731355839903e-6-p5*t12*1.396967636668486e-9+p1*p2*p3*7.112264980321105e-3
    et75 = p1*p2*p4*1.223318865703528e-3-p1*p2*p5*1.656135236227557e-3-p1*p3*p4*2.091171487299617e-3+p1*p2*p6*9.93843071820979e-4
    et76 = p1*p3*p5*(-1.114889254027347e-2)+p2*p3*p4*8.824893265104565e-3-p1*p3*p6*2.620160172643043e-3-p1*p4*p5*7.994065949346873e-5
    et77 = p2*p3*p5*(-6.403258127414312e-4)+p1*p4*p6*3.57573919760338e-5+p2*p3*p6*1.590146671765188e-3-p2*p4*p5*2.158389053918838e-4
    et78 = p1*p5*p6*(-1.922141719015647e-4)+p2*p4*p6*1.630793521904067e-4-p3*p4*p5*5.453170402701301e-5+p2*p5*p6*7.369250053799713e-5
    et79 = p3*p4*p6*(-5.709445756771617e-5)+p3*p5*p6*2.338651064406303e-5-p4*p5*p6*2.701823550152831e-6
    et80 = p1*8.861034959893781e-2-p2*6.894698680639246e-1-p3*7.31132819650646e-1+p4*1.1204691475508e+1+p5*1.961061524704063e+1
    et81 = p6*9.197342256836377e-1-t2*3.889332837620039e-2-t3*6.856653443456626e-4+t4*5.067498711248471e-2-t5*3.04095782135711e-3
    et82 = t6*2.049641760713481e-2+t7*7.204361306481761e-4+t8*1.238361079368357e-4-t9*2.217123249466666e-7-t10*1.44958655089738e-4
    et83 = t11*(-4.282421788691117e-7)-t12*1.911273569943037e-4+t13*6.710779037883328e-7-p1*p2*1.567358202031815e-1+p1*p3*4.942751813326157e-1
    et84 = p1*p4*9.422825996133489e-3+p2*p3*8.066303355863577e-1-p1*p5*2.703992714133834e-2+p2*p4*3.575008250038333e-2-p1*p6*9.653392978455966e-3
    et85 = p2*p5*3.379598335762591e-3-p3*p4*2.548308997439731e-2-p2*p6*2.084411492118733e-2-p3*p5*2.515759145512034e-2+p3*p6*5.679801626305553e-3
    et86 = p4*p5*5.517488591862287e-4-p4*p6*1.742673120915098e-3-p5*p6*3.075068949682078e-3-p2*t2*4.263897135525724e-3-p1*t4*6.590163474949355e-3
    et87 = p3*t2*5.955358914188007e-4-p4*t2*1.645836935015749e-4-p1*t6*2.827388215216459e-3-p3*t4*7.164596787863215e-4
    et88 = p5*t2*(-4.046130069717299e-3)+p2*t6*1.627586972933864e-3+p4*t4*2.710486501148701e-3-p6*t2*7.694142986793993e-4+p1*t8*4.648969809012737e-6
    et89 = p5*t4*(-4.099867706846816e-4)+p2*t8*7.795470629041376e-5-p4*t6*4.724991856281627e-4+p6*t4*9.083524935783661e-4
    et90 = p1*t10*(-4.419227392962203e-5)-p3*t8*1.968896441634663e-5-p5*t6*1.366926739116384e-4-p2*t10*3.068050419589212e-6
    et91 = p6*t6*8.773957398325827e-5+p1*t12*3.187834520680481e-5+p3*t10*1.908306074195848e-5+p5*t8*8.634657871117404e-7
    et92 = p2*t12*4.380050925751171e-5+p4*t10*8.939177212813968e-7-p6*t8*9.290215861926313e-7+p3*t12*3.93512177553562e-6
    et93 = p4*t12*(-5.452594629981461e-7)+p6*t10*4.88858180986109e-7-p5*t12*2.675578186924893e-7-p1*p2*p3*5.419561582301668e-3
    et94 = p1*p2*p4*2.732497190394507e-3-p1*p2*p5*3.430698436783895e-3+p1*p3*p4*4.891046175716301e-4-p1*p2*p6*2.338966826813354e-4
    et95 = p1*p3*p5*2.914401019394533e-4-p2*p3*p4*5.254871720875768e-4+p1*p3*p6*7.736584189047374e-4-p1*p4*p5*3.916728095291342e-5
    et96 = p2*p3*p5*(-1.191645869698598e-3)-p1*p4*p6*7.318341097007766e-6+p2*p3*p6*1.273883627414024e-3+p2*p4*p5*5.868866515031877e-5
    et97 = p1*p5*p6*1.674353993758777e-4-p2*p4*p6*2.16830093752047e-4-p3*p4*p5*9.403621375691601e-6+p2*p5*p6*1.635813264472743e-5
    et98 = p3*p4*p6*(-1.027875211196735e-5)+p3*p5*p6*3.722290686536702e-6-p4*p5*p6*9.408571774363647e-7
    et99 = p1*(-9.919176192069853e-1)+p2*5.277638982063827e-1+p3*1.823177480406913+p4*1.722595782467122e+1-p5*9.169124642587022
    et100 = p6*(-1.169094927633541e+1)-t2*6.591210021095822e-2-t3*3.984898696682795e-3-t4*9.300974833556928e-2+t5*3.97262082322646e-3
    et101 = t6*2.658368466327612e-2+t7*1.249642864006309e-3+t8*2.639990425562038e-4-t9*7.978021758228839e-7+t10*2.223430523398047e-4
    et102 = t11*7.022874125683303e-8+t12*1.285166691552357e-4-t13*1.080889554476854e-6+p1*p2*5.49068105487264e-2+p1*p3*5.023802103391743e-1
    et103 = p1*p4*(-1.473977022649463e-2)-p2*p3*3.957428988155452e-1+p1*p5*9.209624495759293e-3-p2*p4*1.691710275053276e-2-p1*p6*3.683011252269849e-2
    et104 = p2*p5*(-1.411295401479378e-2)-p3*p4*1.441355533243193e-2+p2*p6*1.440646531649937e-2+p3*p5*1.127506419438346e-2-p3*p6*2.872869887129709e-2
    et105 = p4*p5*(-4.536461074326318e-4)-p4*p6*1.955909113163696e-3+p5*p6*1.160188691355493e-3+p2*t2*2.637137838721743e-3-p1*t4*6.955060383581851e-3
    et106 = p3*t2*(-6.930348069904199e-4)-p4*t2*5.946046456580296e-5+p1*t6*1.949251894896114e-3+p3*t4*2.516382002892538e-3+p5*t2*2.593266996871687e-3
    et107 = p2*t6*(-3.248173187167455e-3)-p4*t4*1.665640087374323e-3-p6*t2*3.956839635681712e-4-p1*t8*1.272065500541427e-5
    et108 = p5*t4*1.488600279550827e-4+p2*t8*1.44301495979115e-4+p4*t6*4.543332802623844e-4-p6*t4*2.938121108257198e-4
    et109 = p1*t10*(-1.654632102180789e-4)-p3*t8*2.146574812590323e-6-p5*t6*2.208372201574106e-4-p2*t10*1.737766648709678e-5
    et110 = p6*t6*4.151308800822684e-4+p1*t12*3.434946048139511e-5-p3*t10*4.216577323641611e-5+p5*t8*4.036005968003971e-7
    et111 = p2*t12*5.619007876558663e-6+p4*t10*2.3982789701465e-7+p6*t8*4.068402552137465e-7-p3*t12*1.828135942662256e-5
    et112 = p4*t12*5.692846878024634e-7+p6*t10*1.733960477798563e-7-p5*t12*3.196253347255669e-8+p1*p2*p3*8.840047593668266e-3
    et113 = p1*p2*p4*(-1.997181378110197e-3)+p1*p2*p5*6.960558246943884e-4-p1*p3*p4*1.683377428300275e-4+p1*p2*p6*5.768555211670857e-5
    et114 = p1*p3*p5*(-1.01678308118241e-4)-p2*p3*p4*8.495459117608815e-4-p1*p3*p6*1.248998418149067e-4-p1*p4*p5*1.594906885676193e-4
    et115 = p2*p3*p5*(-4.114898081455899e-4)-p1*p4*p6*2.109917545957415e-5+p2*p3*p6*2.859481885949078e-4+p2*p4*p5*2.014112957114373e-4
    et116 = p1*p5*p6*(-1.948607933322177e-4)+p2*p4*p6*2.329227872010006e-4-p3*p4*p5*3.058466052673428e-5+p2*p5*p6*2.685565017637644e-6
    et117 = p3*p4*p6*(-1.070744261362453e-5)+p3*p5*p6*5.809173009899168e-6+p4*p5*p6*1.001214559344789e-6
    W_sym = np.array([et1+et2+et3+et4+et5+et6+et7+et8+et9+et10+et11+et12+et13+et14+et15+et16+et17+et18+et19+et20,et21+et22+et23+et24+et25+et26+et27+et28+et29+et30+et31+et32+et33+et34+et35+et36+et37+et38+et39+et40,et41+et42+et43+et44+et45+et46+et47+et48+et49+et50+et51+et52+et53+et54+et55+et56+et57+et58+et59+et60,et61+et62+et63+et64+et65+et66+et67+et68+et69+et70+et71+et72+et73+et74+et75+et76+et77+et78+et79,et80+et81+et82+et83+et84+et85+et86+et87+et88+et89+et90+et91+et92+et93+et94+et95+et96+et97+et98,et99+et100+et101+et102+et103+et104+et105+et106+et107+et108+et109+et110+et111+et112+et113+et114+et115+et116+et117])
    return W_sym
