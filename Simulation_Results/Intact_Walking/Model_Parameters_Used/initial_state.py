# Initial activation changed ONCE by offline force calibration.
"""Applied model values. Edit the numbers in PARAMETERS, then run run.py.
Comments and PARAMETER_PROVENANCE.json preserve originals; they do not override your edits.
Missing raw originals are stated honestly. SI units unless noted. Experimental agreement and limitations are documented in Documentation/results.html.
"""

# Set PARAMETERS.
PARAMETERS = {
    # Applied at initialization only: coordinates.
    "coordinates": {
        # Specify pelvis x.
        "pelvis_x": {"position": -0.0016605907104320062, "velocity": 0.5896716440202299},
        # Specify pelvis z.
        "pelvis_z": {"position": 0.24034790103064763, "velocity": 0.05644286874902876},
        # Specify pelvis pitch.
        "pelvis_pitch": {"position": -0.034333468282376385, "velocity": 0.5858178223551215},
        # Specify L hip.
        "L_hip": {"position": -2.1237244682504213, "velocity": 4.446632657899646},
        # Specify L knee.
        "L_knee": {"position": -1.059531573168122, "velocity": -4.901043556523409},
        # Specify L ankle.
        "L_ankle": {"position": 0.7177408308002169, "velocity": 3.356027574501965},
        # Specify L mtp.
        "L_mtp": {"position": 0.29178061698209234, "velocity": -13.230841038033809},
        # Specify R hip.
        "R_hip": {"position": -1.426348210546515, "velocity": -2.0305015893898277},
        # Specify R knee.
        "R_knee": {"position": -1.1033795584553152, "velocity": -0.3231637352584178},
        # Specify R ankle.
        "R_ankle": {"position": 1.1211556910765406, "velocity": 0.9628708869811939},
        # Specify R mtp.
        "R_mtp": {"position": 0.6045106857649141, "velocity": 2.0034207680353138},
        # Specify FL scapulothoracic.
        "FL_scapulothoracic": {
            # Specify position.
            "position": -0.17779235701957485,
            # Specify velocity.
            "velocity": -0.9666705305778671,
        },
        # Specify FL shoulder.
        "FL_shoulder": {"position": -1.2990606327736818, "velocity": 0.04538696601418049},
        # Specify FL elbow.
        "FL_elbow": {"position": 1.067536811716204, "velocity": -2.3162794999980707},
        # Specify FL wrist.
        "FL_wrist": {"position": 0.21600753283194274, "velocity": 1.4298443021477187},
        # Specify FL mcp.
        "FL_mcp": {"position": 0.92721934858565, "velocity": 0.7654715641338913},
        # Specify FR scapulothoracic.
        "FR_scapulothoracic": {
            # Specify position.
            "position": 0.24696476144589172,
            # Specify velocity.
            "velocity": 2.547182486139318,
        },
        # Specify FR shoulder.
        "FR_shoulder": {"position": -1.028708257103752, "velocity": 3.5366237873234567},
        # Specify FR elbow.
        "FR_elbow": {"position": 1.3264408126959961, "velocity": -6.63028478727643},
        # Specify FR wrist.
        "FR_wrist": {"position": -0.3427283209852044, "velocity": 6.783399086600686},
        # Specify FR mcp.
        "FR_mcp": {"position": 0.16549837029775155, "velocity": 5.667870111285021},
    },
    # Applied at initialization only: muscles.
    "muscles": {
        # Specify L IP.
        "L_IP": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.870889478246264,
            # Specify fiber length m.
            "fiber_length_m": 0.039459389117220744,
        },
        # Specify L BFA.
        "L_BFA": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.33693246493782775,
            # Specify fiber length m.
            "fiber_length_m": 0.01999658125733006,
        },
        # Specify L VL.
        "L_VL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.3951463958189099,
            # Specify fiber length m.
            "fiber_length_m": 0.01598546639368841,
        },
        # Specify L VM.
        "L_VM": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.44248817183333095,
            # Specify fiber length m.
            "fiber_length_m": 0.015489368024201101,
        },
        # Specify L TA.
        "L_TA": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7042631123533936,
            # Specify fiber length m.
            "fiber_length_m": 0.06007433191440371,
        },
        # Specify L SO.
        "L_SO": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.41423451954983714,
            # Specify fiber length m.
            "fiber_length_m": 0.02281079349454152,
        },
        # Specify L RF.
        "L_RF": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8428922714381261,
            # Specify fiber length m.
            "fiber_length_m": 0.012711978826536503,
        },
        # Specify L BFP.
        "L_BFP": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7238784481010543,
            # Specify fiber length m.
            "fiber_length_m": 0.05093251618436455,
        },
        # Specify L SAM.
        "L_SAM": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6839514598755866,
            # Specify fiber length m.
            "fiber_length_m": 0.0808757932216231,
        },
        # Specify L LG.
        "L_LG": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.18879084432780802,
            # Specify fiber length m.
            "fiber_length_m": 0.016658169614306,
        },
        # Specify L MG.
        "L_MG": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.2870747663958547,
            # Specify fiber length m.
            "fiber_length_m": 0.015756030482443895,
        },
        # Specify R IP.
        "R_IP": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.44855715358602805,
            # Specify fiber length m.
            "fiber_length_m": 0.03198255855515641,
        },
        # Specify R BFA.
        "R_BFA": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8189344400897721,
            # Specify fiber length m.
            "fiber_length_m": 0.024554498211033268,
        },
        # Specify R VL.
        "R_VL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6896074649210291,
            # Specify fiber length m.
            "fiber_length_m": 0.01629905054946983,
        },
        # Specify R VM.
        "R_VM": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8779689515493411,
            # Specify fiber length m.
            "fiber_length_m": 0.015736640474542884,
        },
        # Specify R TA.
        "R_TA": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.728821143364574,
            # Specify fiber length m.
            "fiber_length_m": 0.0573209153625423,
        },
        # Specify R SO.
        "R_SO": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.4804237717184429,
            # Specify fiber length m.
            "fiber_length_m": 0.02817751661427856,
        },
        # Specify R RF.
        "R_RF": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7746316830147807,
            # Specify fiber length m.
            "fiber_length_m": 0.010193743799285913,
        },
        # Specify R BFP.
        "R_BFP": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.3841549925181842,
            # Specify fiber length m.
            "fiber_length_m": 0.05558323243938858,
        },
        # Specify R SAM.
        "R_SAM": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.529908388004167,
            # Specify fiber length m.
            "fiber_length_m": 0.07209592769202408,
        },
        # Specify R LG.
        "R_LG": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.47605841573645397,
            # Specify fiber length m.
            "fiber_length_m": 0.021134775744557927,
        },
        # Specify R MG.
        "R_MG": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.37804841124834615,
            # Specify fiber length m.
            "fiber_length_m": 0.02055712052121198,
        },
        # Specify L EDL.
        "L_EDL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.32007026552830325,
            # Specify fiber length m.
            "fiber_length_m": 0.031201538175173533,
        },
        # Specify R EDL.
        "R_EDL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.47464457639501473,
            # Specify fiber length m.
            "fiber_length_m": 0.024954205051821984,
        },
        # Specify L FDL.
        "L_FDL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.45453153738225355,
            # Specify fiber length m.
            "fiber_length_m": 0.015342914221368843,
        },
        # Specify R FDL.
        "R_FDL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9876062307363418,
            # Specify fiber length m.
            "fiber_length_m": 0.015224822278158214,
        },
        # Specify L FHL.
        "L_FHL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.5691546170544115,
            # Specify fiber length m.
            "fiber_length_m": 0.011661573533581361,
        },
        # Specify R FHL.
        "R_FHL": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8306963826058645,
            # Specify fiber length m.
            "fiber_length_m": 0.012205974902971007,
        },
        # Specify FL ShoulderExtensor.
        "FL_ShoulderExtensor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.43063291013457866,
            # Specify fiber length m.
            "fiber_length_m": 0.01281725001203047,
        },
        # Specify FL ElbowExtensor.
        "FL_ElbowExtensor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9145343439565062,
            # Specify fiber length m.
            "fiber_length_m": 0.025610591218516367,
        },
        # Specify FL BicepsBrachii.
        "FL_BicepsBrachii": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.29178214880918296,
            # Specify fiber length m.
            "fiber_length_m": 0.021807489743804954,
        },
        # Specify FL ElbowFlexor.
        "FL_ElbowFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.37732246783215856,
            # Specify fiber length m.
            "fiber_length_m": 0.04251547778239118,
        },
        # Specify FL ElbowFlexorWristFlexor.
        "FL_ElbowFlexorWristFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8280355687777172,
            # Specify fiber length m.
            "fiber_length_m": 0.020747654241316544,
        },
        # Specify FL WristFlexor.
        "FL_WristFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6433008556980415,
            # Specify fiber length m.
            "fiber_length_m": 0.013797498621129648,
        },
        # Specify FL WristExtensor.
        "FL_WristExtensor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.2703704982605658,
            # Specify fiber length m.
            "fiber_length_m": 0.011151651183557288,
        },
        # Specify FL ShoulderFlexor.
        "FL_ShoulderFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6767523945082969,
            # Specify fiber length m.
            "fiber_length_m": 0.03801547059163581,
        },
        # Specify FL TricepsBrachiiLong.
        "FL_TricepsBrachiiLong": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8869850405266974,
            # Specify fiber length m.
            "fiber_length_m": 0.013958299916842547,
        },
        # Specify FR ShoulderExtensor.
        "FR_ShoulderExtensor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.301707439802904,
            # Specify fiber length m.
            "fiber_length_m": 0.011020895425201835,
        },
        # Specify FR ElbowExtensor.
        "FR_ElbowExtensor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.4268164321845187,
            # Specify fiber length m.
            "fiber_length_m": 0.027428738731987607,
        },
        # Specify FR BicepsBrachii.
        "FR_BicepsBrachii": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6482470786584758,
            # Specify fiber length m.
            "fiber_length_m": 0.016841006526931677,
        },
        # Specify FR ElbowFlexor.
        "FR_ElbowFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7247089281622151,
            # Specify fiber length m.
            "fiber_length_m": 0.04054389076139881,
        },
        # Specify FR ElbowFlexorWristFlexor.
        "FR_ElbowFlexorWristFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.35537596001213295,
            # Specify fiber length m.
            "fiber_length_m": 0.022476831628234568,
        },
        # Specify FR WristFlexor.
        "FR_WristFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.40063667281026594,
            # Specify fiber length m.
            "fiber_length_m": 0.016932311341653846,
        },
        # Specify FR WristExtensor.
        "FR_WristExtensor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9999997773125731,
            # Specify fiber length m.
            "fiber_length_m": 0.007894871266194769,
        },
        # Specify FR ShoulderFlexor.
        "FR_ShoulderFlexor": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.4983023784326215,
            # Specify fiber length m.
            "fiber_length_m": 0.04035880341714433,
        },
        # Specify FR TricepsBrachiiLong.
        "FR_TricepsBrachiiLong": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6933628005641336,
            # Specify fiber length m.
            "fiber_length_m": 0.02025531568340672,
        },
        # Specify FL S C3.
        "FL_S_C3": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8066081491217026,
            # Specify fiber length m.
            "fiber_length_m": 0.04766798427958194,
        },
        # Specify FR S C3.
        "FR_S_C3": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6492382422071201,
            # Specify fiber length m.
            "fiber_length_m": 0.04881698938165903,
        },
        # Specify FL S C4.
        "FL_S_C4": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.805824064245145,
            # Specify fiber length m.
            "fiber_length_m": 0.04276678897326946,
        },
        # Specify FR S C4.
        "FR_S_C4": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6495873248763039,
            # Specify fiber length m.
            "fiber_length_m": 0.043513500716507204,
        },
        # Specify FL S C5.
        "FL_S_C5": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8047254219573989,
            # Specify fiber length m.
            "fiber_length_m": 0.04152814621519471,
        },
        # Specify FR S C5.
        "FR_S_C5": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6502098859327915,
            # Specify fiber length m.
            "fiber_length_m": 0.041844089260979836,
        },
        # Specify FL S C6.
        "FL_S_C6": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.802099108140442,
            # Specify fiber length m.
            "fiber_length_m": 0.04009188627793664,
        },
        # Specify FR S C6.
        "FR_S_C6": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6528287003917232,
            # Specify fiber length m.
            "fiber_length_m": 0.03916847827074793,
        },
        # Specify FL S C7.
        "FL_S_C7": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.800600700876901,
            # Specify fiber length m.
            "fiber_length_m": 0.03709822271907364,
        },
        # Specify FR S C7.
        "FR_S_C7": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6560678976623533,
            # Specify fiber length m.
            "fiber_length_m": 0.03520350815217931,
        },
        # Specify FL S T1.
        "FL_S_T1": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7271579034932936,
            # Specify fiber length m.
            "fiber_length_m": 0.03193330040740165,
        },
        # Specify FR S T1.
        "FR_S_T1": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9387046902314893,
            # Specify fiber length m.
            "fiber_length_m": 0.02738812548245359,
        },
        # Specify FL S T2.
        "FL_S_T2": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7192702956560972,
            # Specify fiber length m.
            "fiber_length_m": 0.03003186000311795,
        },
        # Specify FR S T2.
        "FR_S_T2": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.953439341617972,
            # Specify fiber length m.
            "fiber_length_m": 0.02445173427524605,
        },
        # Specify FL S T3.
        "FL_S_T3": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6910838555588741,
            # Specify fiber length m.
            "fiber_length_m": 0.024542073725324215,
        },
        # Specify FR S T3.
        "FR_S_T3": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9856712532022647,
            # Specify fiber length m.
            "fiber_length_m": 0.018073043037255147,
        },
        # Specify FL S T4.
        "FL_S_T4": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6749288191499689,
            # Specify fiber length m.
            "fiber_length_m": 0.021694420031772754,
        },
        # Specify FR S T4.
        "FR_S_T4": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 1.0,
            # Specify fiber length m.
            "fiber_length_m": 0.01532101032315631,
        },
        # Specify FL S T5.
        "FL_S_T5": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7213261795587402,
            # Specify fiber length m.
            "fiber_length_m": 0.023017895477601573,
        },
        # Specify FR S T5.
        "FR_S_T5": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9520630792006299,
            # Specify fiber length m.
            "fiber_length_m": 0.018874494065113413,
        },
        # Specify FL S T6.
        "FL_S_T6": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7322305916202012,
            # Specify fiber length m.
            "fiber_length_m": 0.02560183712321325,
        },
        # Specify FR S T6.
        "FR_S_T6": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9200696533147289,
            # Specify fiber length m.
            "fiber_length_m": 0.02385443596083572,
        },
        # Specify FL S T7.
        "FL_S_T7": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7394718170818797,
            # Specify fiber length m.
            "fiber_length_m": 0.02758708960586381,
        },
        # Specify FR S T7.
        "FR_S_T7": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9061997489164333,
            # Specify fiber length m.
            "fiber_length_m": 0.02845481722398855,
        },
        # Specify FL S T8.
        "FL_S_T8": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7490953109338967,
            # Specify fiber length m.
            "fiber_length_m": 0.03100819670956552,
        },
        # Specify FR S T8.
        "FR_S_T8": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9028454739809326,
            # Specify fiber length m.
            "fiber_length_m": 0.03413692998463432,
        },
        # Specify FL S T9.
        "FL_S_T9": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7641624239057028,
            # Specify fiber length m.
            "fiber_length_m": 0.03230694304544618,
        },
        # Specify FR S T9.
        "FR_S_T9": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8947121688470366,
            # Specify fiber length m.
            "fiber_length_m": 0.03838176577411198,
        },
        # Specify FL R C2.
        "FL_R_C2": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6309120022392664,
            # Specify fiber length m.
            "fiber_length_m": 0.038771708507027276,
        },
        # Specify FR R C2.
        "FR_R_C2": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.5558068110462022,
            # Specify fiber length m.
            "fiber_length_m": 0.03999777818962708,
        },
        # Specify FL R C3-7.
        "FL_R_C3-7": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.632910105602216,
            # Specify fiber length m.
            "fiber_length_m": 0.0263639343118286,
        },
        # Specify FR R C3-7.
        "FR_R_C3-7": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.555190027273887,
            # Specify fiber length m.
            "fiber_length_m": 0.02771328151854185,
        },
        # Specify FL R T1.
        "FL_R_T1": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7187978404483276,
            # Specify fiber length m.
            "fiber_length_m": 0.0302567885226062,
        },
        # Specify FR R T1.
        "FR_R_T1": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.3416149866935868,
            # Specify fiber length m.
            "fiber_length_m": 0.032179828440175445,
        },
        # Specify FL R T2.
        "FL_R_T2": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7210398523708139,
            # Specify fiber length m.
            "fiber_length_m": 0.03359608922860226,
        },
        # Specify FR R T2.
        "FR_R_T2": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.34138804786212945,
            # Specify fiber length m.
            "fiber_length_m": 0.036299484278712116,
        },
        # Specify FL R T3.
        "FL_R_T3": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7244780858933473,
            # Specify fiber length m.
            "fiber_length_m": 0.03724505676290237,
        },
        # Specify FR R T3.
        "FR_R_T3": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.34102545862691186,
            # Specify fiber length m.
            "fiber_length_m": 0.04112495059230152,
        },
        # Specify FL R T4.
        "FL_R_T4": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7328847980699814,
            # Specify fiber length m.
            "fiber_length_m": 0.03417076634777539,
        },
        # Specify FR R T4.
        "FR_R_T4": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.3395546807676321,
            # Specify fiber length m.
            "fiber_length_m": 0.039509586870092504,
        },
        # Specify FL R T5.
        "FL_R_T5": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7390484871793741,
            # Specify fiber length m.
            "fiber_length_m": 0.03343260018164973,
        },
        # Specify FR R T5.
        "FR_R_T5": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.33773832163507506,
            # Specify fiber length m.
            "fiber_length_m": 0.03983142647253385,
        },
        # Specify FL DigitalExtensors.
        "FL_DigitalExtensors": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.13003897649551047,
            # Specify fiber length m.
            "fiber_length_m": 0.017055430644364416,
        },
        # Specify FR DigitalExtensors.
        "FR_DigitalExtensors": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7225968465421075,
            # Specify fiber length m.
            "fiber_length_m": 0.01739462200914173,
        },
        # Specify FL DigitalFlexors.
        "FL_DigitalFlexors": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.10778298789458943,
            # Specify fiber length m.
            "fiber_length_m": 0.015694696672205573,
        },
        # Specify FR DigitalFlexors.
        "FR_DigitalFlexors": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.030855137478851703,
            # Specify fiber length m.
            "fiber_length_m": 0.010108712531143723,
        },
        # Specify FL TrapeziusCervical.
        "FL_TrapeziusCervical": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.8158144542587283,
            # Specify fiber length m.
            "fiber_length_m": 0.06628613647545409,
        },
        # Specify FR TrapeziusCervical.
        "FR_TrapeziusCervical": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9139421016430548,
            # Specify fiber length m.
            "fiber_length_m": 0.057151230000366704,
        },
        # Specify FL TrapeziusThoracic.
        "FL_TrapeziusThoracic": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.6407481804841275,
            # Specify fiber length m.
            "fiber_length_m": 0.05154216864635602,
        },
        # Specify FR TrapeziusThoracic.
        "FR_TrapeziusThoracic": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.24026029228047824,
            # Specify fiber length m.
            "fiber_length_m": 0.056857006896382616,
        },
        # Specify FL LatissimusDorsi.
        "FL_LatissimusDorsi": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.4100605376422592,
            # Specify fiber length m.
            "fiber_length_m": 0.11476552393267118,
        },
        # Specify FR LatissimusDorsi.
        "FR_LatissimusDorsi": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.09239602871797474,
            # Specify fiber length m.
            "fiber_length_m": 0.13681561326713626,
        },
        # Specify FL PectoralisProfundus.
        "FL_PectoralisProfundus": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.5010229242307643,
            # Specify fiber length m.
            "fiber_length_m": 0.038251000461620645,
        },
        # Specify FR PectoralisProfundus.
        "FR_PectoralisProfundus": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.04887282220468061,
            # Specify fiber length m.
            "fiber_length_m": 0.06443379103520389,
        },
        # Specify FL PectoralisSuperficialis.
        "FL_PectoralisSuperficialis": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7657904109014932,
            # Specify fiber length m.
            "fiber_length_m": 0.04527193394990888,
        },
        # Specify FR PectoralisSuperficialis.
        "FR_PectoralisSuperficialis": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.5290556722902369,
            # Specify fiber length m.
            "fiber_length_m": 0.029620609595436463,
        },
        # Specify FL Clavobrachialis.
        "FL_Clavobrachialis": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.7590123734811056,
            # Specify fiber length m.
            "fiber_length_m": 0.0927788862620518,
        },
        # Specify FR Clavobrachialis.
        "FR_Clavobrachialis": {
            # Specify activation 0 to 1.
            "activation_0_to_1": 0.9999999945105883,
            # Specify fiber length m.
            "fiber_length_m": 0.06709306153434504,
        },
    },
    # Applied at initialization only: contact_memory.
    "contact_memory": {
        # Specify L paw pad0.
        "L_paw_pad0": [0.0, 0.0],
        # Specify L paw pad1.
        "L_paw_pad1": [0.0, 0.0],
        # Specify L paw pad2.
        "L_paw_pad2": [0.0, 0.0],
        # Specify L paw pad3.
        "L_paw_pad3": [0.0, 0.0],
        # Specify L paw pad4.
        "L_paw_pad4": [0.0, 0.0],
        # Specify L paw pad5.
        "L_paw_pad5": [0.0, 0.0],
        # Specify R paw pad0.
        "R_paw_pad0": [0.0, 0.0],
        # Specify R paw pad1.
        "R_paw_pad1": [0.0, 0.0],
        # Specify R paw pad2.
        "R_paw_pad2": [-6.625154927893859e-05, -9.836656344473204e-19],
        # Specify R paw pad3.
        "R_paw_pad3": [-6.625154898795637e-05, -9.836656344473204e-19],
        # Specify R paw pad4.
        "R_paw_pad4": [0.0006065666878787488, -1.7253743856456664e-18],
        # Specify R paw pad5.
        "R_paw_pad5": [0.0006065666892054754, -1.7253743856456664e-18],
        # Specify FL contactpad0.
        "FL_contactpad0": [0.0, 0.0],
        # Specify FL contactpad1.
        "FL_contactpad1": [0.0, 0.0],
        # Specify FL contactpad2.
        "FL_contactpad2": [-0.00023791809765974514, -2.654916342542892e-17],
        # Specify FL contactpad3.
        "FL_contactpad3": [-0.0002379180976599318, -2.6549163425428512e-17],
        # Specify FL contactpad4.
        "FL_contactpad4": [7.091345942516367e-05, -3.3989750215567644e-17],
        # Specify FL contactpad5.
        "FL_contactpad5": [7.091345788102e-05, -3.398975021556764e-17],
        # Specify FR contactpad0.
        "FR_contactpad0": [0.0, 0.0],
        # Specify FR contactpad1.
        "FR_contactpad1": [0.0, 0.0],
        # Specify FR contactpad2.
        "FR_contactpad2": [0.0, 0.0],
        # Specify FR contactpad3.
        "FR_contactpad3": [0.0, 0.0],
        # Specify FR contactpad4.
        "FR_contactpad4": [3.6106912332098414e-05, 0.0],
        # Specify FR contactpad5.
        "FR_contactpad5": [3.6106911690813815e-05, 0.0],
    },
}
