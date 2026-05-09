import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score(input):
    if input[1] < 0.3850742:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[12] < 1.0:
                    if input[8] < -0.030722976:
                        if input[1] < -0.75493634:
                            var0 = -0.20983334
                        else:
                            var0 = 0.050192297
                    else:
                        if input[3] < 1.5074284:
                            var0 = -0.24247298
                        else:
                            var0 = 0.09859791
                else:
                    if input[3] < 0.37825713:
                        if input[1] < -0.46993372:
                            var0 = -0.30988646
                        else:
                            var0 = -0.08535235
                    else:
                        if input[3] < 1.103888:
                            var0 = 0.21450551
                        else:
                            var0 = -0.18284577
            else:
                if input[8] < -0.030567229:
                    if input[9] < 1.4331708:
                        if input[14] < 1.0:
                            var0 = -0.37728876
                        else:
                            var0 = -0.32936782
                    else:
                        if input[7] < -0.7464196:
                            var0 = 0.0859951
                        else:
                            var0 = -0.2281134
                else:
                    if input[1] < -0.37493283:
                        if input[13] < 1.0:
                            var0 = -0.31672847
                        else:
                            var0 = -0.21682619
                    else:
                        if input[14] < 1.0:
                            var0 = -0.27982426
                        else:
                            var0 = -0.1552054
        else:
            if input[3] < -0.35117662:
                if input[7] < 1.1829834:
                    if input[0] < -0.14237958:
                        if input[7] < 0.20974475:
                            var0 = 0.48896727
                        else:
                            var0 = 0.04800985
                    else:
                        if input[9] < -0.83241135:
                            var0 = 0.17812043
                        else:
                            var0 = -0.18407628
                else:
                    var0 = 0.79106146
            else:
                if input[9] < -1.1117297:
                    var0 = 0.3140519
                else:
                    var0 = 1.118107
    else:
        if input[6] < 0.97067964:
            if input[1] < 1.1450812:
                if input[4] < 0.8088304:
                    if input[12] < 1.0:
                        if input[8] < -0.030498018:
                            var0 = 0.75998133
                        else:
                            var0 = 0.18689452
                    else:
                        if input[3] < 1.13005:
                            var0 = 0.91461587
                        else:
                            var0 = 0.33198345
                else:
                    if input[4] < 2.5279171:
                        if input[8] < -0.030498018:
                            var0 = -0.26820168
                        else:
                            var0 = 0.13974671
                    else:
                        var0 = 1.1209295
            else:
                if input[1] < 3.3301015:
                    if input[8] < 0.27596393:
                        var0 = 1.0330055
                    else:
                        var0 = 0.3140519
                else:
                    var0 = -0.058516596
        else:
            if input[4] < 2.5279171:
                if input[4] < 0.8088304:
                    if input[12] < 1.0:
                        if input[3] < -0.13747577:
                            var0 = 0.3180105
                        else:
                            var0 = -0.06589786
                    else:
                        if input[1] < 2.6650953:
                            var0 = 0.5527956
                        else:
                            var0 = -0.15715568
                else:
                    if input[8] < -0.030248145:
                        if input[3] < 0.057679754:
                            var0 = -0.32005206
                        else:
                            var0 = -0.077082016
                    else:
                        if input[1] < 1.8100873:
                            var0 = 0.07736271
                        else:
                            var0 = -0.2081454
            else:
                var0 = 1.0699503
    if input[1] < 0.2900733:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[12] < 1.0:
                    if input[3] < -0.0662711:
                        if input[6] < 0.97067964:
                            var1 = 0.05590999
                        else:
                            var1 = -0.10821002
                    else:
                        if input[1] < -0.08993021:
                            var1 = -0.2355851
                        else:
                            var1 = -0.08147824
                else:
                    if input[1] < 0.005070672:
                        if input[3] < 0.37825713:
                            var1 = -0.20220025
                        else:
                            var1 = 0.020273462
                    else:
                        if input[0] < 1.09998:
                            var1 = 0.3445739
                        else:
                            var1 = -0.2234311
            else:
                if input[8] < -0.030567229:
                    if input[14] < 1.0:
                        if input[7] < -1.7126687:
                            var1 = -0.07336055
                        else:
                            var1 = -0.3468384
                    else:
                        if input[1] < 0.19507243:
                            var1 = -0.29743138
                        else:
                            var1 = -0.035918113
                else:
                    if input[0] < -2.2336848:
                        var1 = 0.07592367
                    else:
                        if input[3] < 0.8534328:
                            var1 = -0.20374152
                        else:
                            var1 = -0.27982178
        else:
            if input[3] < -0.63909185:
                if input[7] < 0.5360101:
                    if input[1] < -0.5649346:
                        var1 = -0.19563217
                    else:
                        if input[7] < -0.33451837:
                            var1 = 0.29195687
                        else:
                            var1 = -0.06992195
                else:
                    var1 = 0.47896844
            else:
                if input[7] < 1.5132883:
                    var1 = 0.5435065
                else:
                    var1 = 0.13302077
    else:
        if input[6] < 0.97067964:
            if input[1] < 0.7650777:
                if input[4] < 0.8088304:
                    if input[0] < -0.7014414:
                        if input[11] < 1.0:
                            var1 = 0.21608283
                        else:
                            var1 = 0.5625316
                    else:
                        if input[11] < 1.0:
                            var1 = 0.2802508
                        else:
                            var1 = 0.055903118
                else:
                    if input[4] < 2.5279171:
                        if input[8] < -0.014425209:
                            var1 = -0.1946586
                        else:
                            var1 = 0.123263136
                    else:
                        var1 = 0.5497984
            else:
                if input[4] < 0.8088304:
                    if input[1] < 2.760096:
                        if input[1] < 1.2400821:
                            var1 = 0.4136344
                        else:
                            var1 = 0.54503936
                    else:
                        if input[14] < 1.0:
                            var1 = -0.14835817
                        else:
                            var1 = 0.3066473
                else:
                    if input[4] < 2.5279171:
                        if input[8] < -0.030722976:
                            var1 = -0.12459884
                        else:
                            var1 = 0.3313049
                    else:
                        var1 = 0.5933602
        else:
            if input[1] < 2.2850916:
                if input[4] < 2.5279171:
                    if input[4] < 0.8088304:
                        if input[13] < 1.0:
                            var1 = 0.21730986
                        else:
                            var1 = 0.007644869
                    else:
                        if input[8] < -0.030290572:
                            var1 = -0.2563368
                        else:
                            var1 = 0.016707143
                else:
                    var1 = 0.5473174
            else:
                if input[12] < 1.0:
                    if input[3] < 0.9759226:
                        if input[0] < -1.0948552:
                            var1 = -0.1404528
                        else:
                            var1 = -0.33794785
                    else:
                        if input[3] < 0.9882684:
                            var1 = 0.102009185
                        else:
                            var1 = -0.22359353
                else:
                    if input[9] < -0.9798294:
                        var1 = 0.27677965
                    else:
                        if input[0] < -0.76355934:
                            var1 = 0.09288246
                        else:
                            var1 = -0.2385854
    if input[1] < 0.10007155:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[12] < 1.0:
                    if input[3] < -0.0662711:
                        if input[0] < -0.31838053:
                            var2 = 0.08846211
                        else:
                            var2 = -0.14028145
                    else:
                        if input[3] < 1.5820119:
                            var2 = -0.20152909
                        else:
                            var2 = 0.104498275
                else:
                    if input[1] < -0.46993372:
                        if input[6] < 0.97067964:
                            var2 = 0.025726927
                        else:
                            var2 = -0.17855331
                    else:
                        if input[3] < 1.098279:
                            var2 = 0.15128398
                        else:
                            var2 = -0.21056113
            else:
                if input[8] < -0.030567229:
                    if input[9] < 1.3400646:
                        if input[2] < -1.3866642:
                            var2 = -0.15012775
                        else:
                            var2 = -0.3079562
                    else:
                        var2 = 0.060818627
                else:
                    if input[6] < 0.97067964:
                        if input[8] < -0.023676272:
                            var2 = -0.053129528
                        else:
                            var2 = -0.24248523
                    else:
                        if input[3] < 1.5820119:
                            var2 = -0.247391
                        else:
                            var2 = -0.0103418175
        else:
            if input[8] < -0.028330084:
                if input[7] < -0.89486235:
                    var2 = -0.135362
                else:
                    if input[8] < -0.029745366:
                        if input[7] < 0.34157342:
                            var2 = 0.09731382
                        else:
                            var2 = 0.36174256
                    else:
                        var2 = -0.10968622
            else:
                var2 = 0.43605968
    else:
        if input[6] < 0.97067964:
            if input[1] < 0.5750759:
                if input[4] < 0.8088304:
                    if input[3] < 1.4464515:
                        if input[3] < 1.2268641:
                            var2 = 0.15599605
                        else:
                            var2 = -0.3277682
                    else:
                        var2 = 0.44906113
                else:
                    if input[4] < 2.5279171:
                        if input[0] < -1.581446:
                            var2 = 0.12746784
                        else:
                            var2 = -0.18500035
                    else:
                        if input[7] < -1.1768137:
                            var2 = 0.017520819
                        else:
                            var2 = 0.35272434
            else:
                if input[1] < 1.4300839:
                    if input[4] < 0.8088304:
                        if input[8] < -0.02874919:
                            var2 = 0.34600165
                        else:
                            var2 = 0.20624344
                    else:
                        if input[4] < 2.5279171:
                            var2 = -0.025022816
                        else:
                            var2 = 0.4370248
                else:
                    if input[1] < 3.3301015:
                        if input[7] < -1.699336:
                            var2 = 0.08168371
                        else:
                            var2 = 0.40957198
                    else:
                        var2 = -0.0743791
        else:
            if input[4] < 2.5279171:
                if input[4] < 0.8088304:
                    if input[1] < 2.3800926:
                        if input[1] < 0.5750759:
                            var2 = -0.042021587
                        else:
                            var2 = 0.14932665
                    else:
                        if input[7] < -0.114853054:
                            var2 = -0.3066703
                        else:
                            var2 = -0.09920098
                else:
                    if input[8] < -0.030248145:
                        if input[0] < -1.4882691:
                            var2 = -0.018792773
                        else:
                            var2 = -0.25873452
                    else:
                        if input[8] < -0.029904474:
                            var2 = 0.4811167
                        else:
                            var2 = -0.05290607
            else:
                if input[1] < 2.09509:
                    var2 = 0.4141146
                else:
                    var2 = 0.1109393
    if input[1] < 0.10007155:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[6] < 0.97067964:
                    if input[14] < 1.0:
                        if input[8] < -0.022054886:
                            var3 = -0.13874938
                        else:
                            var3 = 0.051574077
                    else:
                        if input[11] < 1.0:
                            var3 = 0.14388849
                        else:
                            var3 = -0.02505106
                else:
                    if input[7] < 1.3641307:
                        if input[14] < 1.0:
                            var3 = -0.22169277
                        else:
                            var3 = -0.107172586
                    else:
                        if input[0] < -0.0906146:
                            var3 = 0.24610257
                        else:
                            var3 = -0.099301934
            else:
                if input[8] < -0.030567229:
                    if input[9] < 1.3400646:
                        if input[2] < -1.3866642:
                            var3 = -0.12537847
                        else:
                            var3 = -0.2855476
                    else:
                        if input[7] < -0.28583017:
                            var3 = 0.25344133
                        else:
                            var3 = -0.1815148
                else:
                    if input[1] < -0.37493283:
                        if input[13] < 1.0:
                            var3 = -0.22454955
                        else:
                            var3 = -0.09576263
                    else:
                        if input[6] < 0.97067964:
                            var3 = -0.016150976
                        else:
                            var3 = -0.19145139
        else:
            if input[8] < -0.028330084:
                if input[10] < 2.8915195:
                    if input[6] < 0.97067964:
                        if input[9] < -0.37463963:
                            var3 = 0.009743694
                        else:
                            var3 = 0.2841232
                    else:
                        if input[7] < 1.1829834:
                            var3 = -0.17963503
                        else:
                            var3 = 0.02686483
                else:
                    var3 = 0.31171334
            else:
                var3 = 0.36226872
    else:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[6] < 0.97067964:
                    if input[1] < 1.0500803:
                        if input[8] < -0.027614832:
                            var3 = 0.18516055
                        else:
                            var3 = 0.063544124
                    else:
                        if input[1] < 2.760096:
                            var3 = 0.30499163
                        else:
                            var3 = 0.04570294
                else:
                    if input[1] < 1.8100873:
                        if input[1] < 0.5750759:
                            var3 = -0.030374894
                        else:
                            var3 = 0.14898556
                    else:
                        if input[7] < 1.5997853:
                            var3 = -0.14079227
                        else:
                            var3 = 0.29781985
            else:
                if input[3] < -0.35117662:
                    if input[0] < -1.1569732:
                        if input[7] < 1.0687221:
                            var3 = -0.10968221
                        else:
                            var3 = 0.2242278
                    else:
                        if input[2] < 1.0299541:
                            var3 = -0.25858432
                        else:
                            var3 = -0.13343538
                else:
                    if input[1] < 0.5750759:
                        if input[3] < -0.09819516:
                            var3 = 0.27109662
                        else:
                            var3 = -0.116536744
                    else:
                        if input[14] < 1.0:
                            var3 = -0.004858046
                        else:
                            var3 = 0.18472682
        else:
            if input[1] < 0.3850742:
                if input[3] < 0.45116842:
                    if input[7] < -0.6676928:
                        var3 = -0.18989296
                    else:
                        if input[0] < -0.23555654:
                            var3 = 0.20637862
                        else:
                            var3 = -0.013058803
                else:
                    var3 = 0.35397822
            else:
                if input[1] < 2.5700943:
                    var3 = 0.39959252
                else:
                    var3 = 0.11390666
    if input[1] < 0.005070672:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[6] < 0.97067964:
                    if input[11] < 1.0:
                        if input[7] < -0.45604277:
                            var4 = 0.11589891
                        else:
                            var4 = -0.031220585
                    else:
                        if input[9] < -0.9255175:
                            var4 = -0.21565421
                        else:
                            var4 = -0.018002767
                else:
                    if input[7] < 1.1123637:
                        if input[11] < 1.0:
                            var4 = -0.10113558
                        else:
                            var4 = -0.20688176
                    else:
                        if input[1] < -0.08993021:
                            var4 = 0.037019916
                        else:
                            var4 = -0.2710073
            else:
                if input[8] < -0.030567229:
                    if input[9] < 1.3400646:
                        if input[7] < -1.6840237:
                            var4 = -0.0079361
                        else:
                            var4 = -0.26784548
                    else:
                        var4 = 0.05599262
                else:
                    if input[1] < -0.18493108:
                        if input[13] < 1.0:
                            var4 = -0.18705283
                        else:
                            var4 = -0.056185186
                    else:
                        if input[8] < -0.025396056:
                            var4 = 0.0910645
                        else:
                            var4 = -0.15355143
        else:
            if input[8] < -0.028330084:
                if input[5] < 0.64104193:
                    if input[7] < -0.2725314:
                        var4 = 0.053597704
                    else:
                        var4 = 0.27024227
                else:
                    if input[9] < -0.8168937:
                        if input[13] < 1.0:
                            var4 = -0.051638465
                        else:
                            var4 = 0.22865811
                    else:
                        if input[11] < 1.0:
                            var4 = -0.25782812
                        else:
                            var4 = 0.020770121
            else:
                var4 = 0.3045374
    else:
        if input[14] < 1.0:
            if input[12] < 1.0:
                if input[3] < 1.4322927:
                    if input[0] < -0.7221474:
                        if input[7] < 0.022111539:
                            var4 = -0.08629851
                        else:
                            var4 = 0.104843356
                    else:
                        if input[4] < 2.5279171:
                            var4 = -0.1331068
                        else:
                            var4 = 0.17101608
                else:
                    if input[0] < -0.13202658:
                        if input[9] < 0.059855595:
                            var4 = -0.21489818
                        else:
                            var4 = 0.12716004
                    else:
                        if input[6] < 0.97067964:
                            var4 = 0.47835925
                        else:
                            var4 = 0.09056079
            else:
                if input[3] < 0.32922727:
                    if input[9] < 0.09864981:
                        if input[7] < -0.61021817:
                            var4 = -0.24790318
                        else:
                            var4 = 0.118457
                    else:
                        if input[1] < 1.335083:
                            var4 = -0.3828861
                        else:
                            var4 = -0.0992873
                else:
                    if input[3] < 0.7597055:
                        if input[9] < -0.8168937:
                            var4 = 0.52870786
                        else:
                            var4 = 0.23117161
                    else:
                        if input[4] < 0.8088304:
                            var4 = 0.10541227
                        else:
                            var4 = -0.14628607
        else:
            if input[4] < 2.5279171:
                if input[4] < 0.8088304:
                    if input[8] < -0.028894376:
                        if input[5] < 0.64104193:
                            var4 = 0.3624326
                        else:
                            var4 = 0.13684204
                    else:
                        if input[12] < 1.0:
                            var4 = 0.022055864
                        else:
                            var4 = 0.17606643
                else:
                    if input[0] < -1.4882691:
                        if input[8] < -0.02462842:
                            var4 = 0.11883319
                        else:
                            var4 = 0.62914217
                    else:
                        if input[8] < -0.030960822:
                            var4 = -0.12854283
                        else:
                            var4 = 0.050484776
            else:
                if input[1] < 0.2900733:
                    if input[8] < -0.031136286:
                        var4 = 0.039422393
                    else:
                        var4 = 0.26404348
                else:
                    var4 = 0.3498599
    if input[1] < 0.5750759:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[0] < -2.4407449:
                    var5 = 0.6205736
                else:
                    if input[14] < 1.0:
                        if input[1] < -0.27993196:
                            var5 = -0.12916897
                        else:
                            var5 = -0.023897348
                    else:
                        if input[3] < 1.6430904:
                            var5 = 0.0036519482
                        else:
                            var5 = 0.33867744
            else:
                if input[8] < -0.030062638:
                    if input[14] < 1.0:
                        if input[7] < -1.6840237:
                            var5 = 0.05220006
                        else:
                            var5 = -0.27374485
                    else:
                        if input[9] < 0.71935725:
                            var5 = -0.17330061
                        else:
                            var5 = 0.017985605
                else:
                    if input[8] < -0.029904474:
                        var5 = 0.36052322
                    else:
                        if input[7] < 1.342763:
                            var5 = -0.095012866
                        else:
                            var5 = -0.27822495
        else:
            if input[8] < -0.028330084:
                if input[7] < -0.6676928:
                    if input[6] < 0.97067964:
                        var5 = 0.05536786
                    else:
                        var5 = -0.23012668
                else:
                    if input[9] < 0.19175592:
                        if input[10] < 1.2975454:
                            var5 = -0.06911815
                        else:
                            var5 = 0.1939732
                    else:
                        if input[7] < -0.2725314:
                            var5 = 0.052976385
                        else:
                            var5 = 0.35500932
            else:
                if input[3] < 0.45116842:
                    var5 = 0.0810288
                else:
                    if input[2] < -1.041433:
                        var5 = 0.09997848
                    else:
                        var5 = 0.3341075
    else:
        if input[6] < 0.97067964:
            if input[1] < 1.4300839:
                if input[12] < 1.0:
                    if input[0] < -0.9292073:
                        if input[7] < 0.38036832:
                            var5 = 0.07464324
                        else:
                            var5 = 0.2571784
                    else:
                        if input[0] < -0.3390865:
                            var5 = -0.22869156
                        else:
                            var5 = 0.1039366
                else:
                    if input[1] < 1.2400821:
                        if input[9] < -1.1505239:
                            var5 = -0.10794687
                        else:
                            var5 = 0.22577322
                    else:
                        if input[7] < 0.35555807:
                            var5 = -0.16845502
                        else:
                            var5 = 0.24974208
            else:
                if input[1] < 2.855097:
                    if input[0] < 1.6072768:
                        if input[7] < -1.6840237:
                            var5 = 0.020209763
                        else:
                            var5 = 0.30458724
                    else:
                        if input[9] < 0.20727362:
                            var5 = -0.2153992
                        else:
                            var5 = 0.2665463
                else:
                    if input[14] < 1.0:
                        var5 = -0.22460794
                    else:
                        if input[1] < 3.2351005:
                            var5 = 0.25099325
                        else:
                            var5 = 0.03580803
        else:
            if input[1] < 1.8100873:
                if input[7] < -0.9472609:
                    if input[13] < 1.0:
                        if input[3] < 0.9687012:
                            var5 = 0.32509875
                        else:
                            var5 = 0.0655436
                    else:
                        if input[3] < 0.5637478:
                            var5 = 0.11343224
                        else:
                            var5 = -0.2858659
                else:
                    if input[1] < 0.8600786:
                        if input[7] < -0.3796405:
                            var5 = -0.2616538
                        else:
                            var5 = 0.007679478
                    else:
                        if input[14] < 1.0:
                            var5 = -0.030057112
                        else:
                            var5 = 0.19799422
            else:
                if input[9] < -0.9798294:
                    if input[3] < 1.1227999:
                        if input[2] < -1.3866642:
                            var5 = -0.10769815
                        else:
                            var5 = 0.28182024
                    else:
                        var5 = -0.253588
                else:
                    if input[1] < 3.1400995:
                        if input[1] < 3.0450988:
                            var5 = -0.1390966
                        else:
                            var5 = 0.1386233
                    else:
                        if input[0] < -1.0741493:
                            var5 = -0.064501435
                        else:
                            var5 = -0.31687355
    if input[1] < -0.18493108:
        if input[4] < 0.8088304:
            if input[11] < 1.0:
                if input[9] < 0.9676402:
                    if input[3] < 1.055667:
                        if input[8] < -0.012035764:
                            var6 = 0.009471083
                        else:
                            var6 = 0.20232393
                    else:
                        if input[0] < 0.98609704:
                            var6 = -0.17781934
                        else:
                            var6 = 0.073815055
                else:
                    if input[3] < 0.8783539:
                        var6 = -0.302564
                    else:
                        var6 = -0.03514
            else:
                if input[3] < 1.5820119:
                    if input[3] < -0.5277329:
                        if input[7] < 1.4377079:
                            var6 = -0.06591962
                        else:
                            var6 = 0.37515658
                    else:
                        if input[0] < -2.140508:
                            var6 = 0.17938836
                        else:
                            var6 = -0.19669332
                else:
                    if input[9] < -1.2513889:
                        var6 = -0.206111
                    else:
                        if input[14] < 1.0:
                            var6 = 0.016544232
                        else:
                            var6 = 0.603083
        else:
            if input[4] < 2.5279171:
                if input[3] < 0.5095043:
                    if input[2] < -0.6962018:
                        if input[14] < 1.0:
                            var6 = -0.23064642
                        else:
                            var6 = -0.028176546
                    else:
                        if input[0] < -1.7781531:
                            var6 = -0.054043688
                        else:
                            var6 = -0.24885432
                else:
                    if input[3] < 0.5267485:
                        var6 = 0.5475213
                    else:
                        if input[8] < 0.017801737:
                            var6 = -0.1478285
                        else:
                            var6 = 0.12254163
            else:
                if input[6] < 0.97067964:
                    if input[3] < -0.63909185:
                        if input[9] < -0.65395796:
                            var6 = -0.055967566
                        else:
                            var6 = 0.15127456
                    else:
                        if input[0] < -0.58755845:
                            var6 = 0.062075857
                        else:
                            var6 = 0.274186
                else:
                    if input[0] < 0.0025623667:
                        var6 = 0.16092484
                    else:
                        if input[10] < 2.8915195:
                            var6 = -0.1656968
                        else:
                            var6 = 0.055724304
    else:
        if input[4] < 2.5279171:
            if input[4] < 0.8088304:
                if input[6] < 0.97067964:
                    if input[1] < 1.2400821:
                        if input[9] < 1.1538525:
                            var6 = 0.039214715
                        else:
                            var6 = 0.13170207
                    else:
                        if input[1] < 2.4750936:
                            var6 = 0.23206386
                        else:
                            var6 = 0.016934762
                else:
                    if input[12] < 1.0:
                        if input[3] < 0.29981324:
                            var6 = 0.041371435
                        else:
                            var6 = -0.10912213
                    else:
                        if input[3] < 1.2736435:
                            var6 = 0.11264419
                        else:
                            var6 = -0.297753
            else:
                if input[3] < -0.35117662:
                    if input[14] < 1.0:
                        if input[7] < -0.9472609:
                            var6 = -0.060228433
                        else:
                            var6 = -0.242411
                    else:
                        if input[7] < 0.8663735:
                            var6 = -0.13450468
                        else:
                            var6 = 0.09377202
                else:
                    if input[0] < 1.4623349:
                        if input[3] < 0.8488668:
                            var6 = 0.06541055
                        else:
                            var6 = -0.075536385
                    else:
                        if input[13] < 1.0:
                            var6 = -0.3071236
                        else:
                            var6 = 0.040874854
        else:
            if input[8] < -0.03078074:
                if input[1] < 0.3850742:
                    if input[0] < -0.4115575:
                        if input[6] < 0.97067964:
                            var6 = 0.2943868
                        else:
                            var6 = -0.023954064
                    else:
                        if input[6] < 0.97067964:
                            var6 = -0.21059933
                        else:
                            var6 = 0.090539545
                else:
                    if input[7] < -0.29495046:
                        if input[0] < -0.0906146:
                            var6 = -0.03667435
                        else:
                            var6 = 0.093607455
                    else:
                        var6 = 0.29962832
            else:
                if input[7] < -1.42103:
                    var6 = 0.117955126
                else:
                    var6 = 0.3437043
    if input[1] < -0.37493283:
        if input[3] < 0.45116842:
            if input[9] < 0.09864981:
                if input[10] < -0.006615333:
                    if input[6] < 0.97067964:
                        if input[1] < -0.9449381:
                            var7 = -0.12436414
                        else:
                            var7 = 0.14155602
                    else:
                        if input[2] < -0.35097063:
                            var7 = 0.09398272
                        else:
                            var7 = -0.18656269
                else:
                    if input[10] < 2.8915195:
                        if input[4] < 2.5279171:
                            var7 = -0.2358693
                        else:
                            var7 = 0.046733595
                    else:
                        if input[14] < 1.0:
                            var7 = -0.1204241
                        else:
                            var7 = 0.2559551
            else:
                if input[1] < -0.5649346:
                    if input[4] < 2.5279171:
                        if input[7] < 1.4498934:
                            var7 = -0.27448162
                        else:
                            var7 = -0.08951888
                    else:
                        var7 = -0.01055373
                else:
                    if input[10] < -0.71982825:
                        if input[7] < -0.40280506:
                            var7 = -0.18326433
                        else:
                            var7 = 0.29868224
                    else:
                        if input[7] < -1.1768137:
                            var7 = -0.019795101
                        else:
                            var7 = -0.2677765
        else:
            if input[11] < 1.0:
                if input[3] < 0.5267485:
                    if input[1] < -1.2299408:
                        var7 = -0.088858515
                    else:
                        if input[9] < -0.6074049:
                            var7 = 0.11464751
                        else:
                            var7 = 0.45509705
                else:
                    if input[2] < -1.3866642:
                        if input[7] < 0.04761827:
                            var7 = 0.5206467
                        else:
                            var7 = -0.088968426
                    else:
                        if input[9] < -1.049659:
                            var7 = -0.18421362
                        else:
                            var7 = -0.012556377
            else:
                if input[3] < 1.1172676:
                    if input[10] < -0.34624052:
                        if input[9] < -0.65395796:
                            var7 = 0.3326604
                        else:
                            var7 = -0.16323927
                    else:
                        var7 = -0.27174065
                else:
                    if input[0] < -0.049202614:
                        if input[1] < -0.9449381:
                            var7 = -0.24445443
                        else:
                            var7 = 0.3895489
                    else:
                        if input[3] < 1.7584945:
                            var7 = -0.16659556
                        else:
                            var7 = 0.21740335
    else:
        if input[4] < 2.5279171:
            if input[6] < 0.97067964:
                if input[1] < 1.4300839:
                    if input[14] < 1.0:
                        if input[3] < 0.45116842:
                            var7 = -0.085992575
                        else:
                            var7 = 0.05218838
                    else:
                        if input[1] < -0.27993196:
                            var7 = 0.2994222
                        else:
                            var7 = 0.045679394
                else:
                    if input[3] < 0.29352525:
                        if input[10] < 1.1481103:
                            var7 = 0.30905482
                        else:
                            var7 = -0.027904257
                    else:
                        if input[5] < 0.64104193:
                            var7 = 0.27360508
                        else:
                            var7 = 0.04142402
            else:
                if input[4] < 0.8088304:
                    if input[0] < -0.11132059:
                        if input[9] < -0.74706405:
                            var7 = 0.21876453
                        else:
                            var7 = -0.017617347
                    else:
                        if input[9] < -0.7936171:
                            var7 = -0.14518122
                        else:
                            var7 = -0.02301408
                else:
                    if input[9] < -1.049659:
                        if input[7] < 0.5943842:
                            var7 = 0.18660848
                        else:
                            var7 = -0.17892331
                    else:
                        if input[14] < 1.0:
                            var7 = -0.20480718
                        else:
                            var7 = -0.045114197
        else:
            if input[8] < -0.03078074:
                if input[4] < 4.247004:
                    if input[7] < 0.9084869:
                        if input[7] < -0.33451837:
                            var7 = 0.08631093
                        else:
                            var7 = -0.0745536
                    else:
                        var7 = 0.20663682
                else:
                    var7 = 0.28240237
            else:
                if input[7] < -1.42103:
                    var7 = 0.10130438
                else:
                    var7 = 0.3235423
    if input[1] < 0.7650777:
        if input[6] < 0.97067964:
            if input[0] < -2.4407449:
                var8 = 0.39878926
            else:
                if input[4] < 2.5279171:
                    if input[4] < 0.8088304:
                        if input[5] < 0.64104193:
                            var8 = -0.041492183
                        else:
                            var8 = 0.031586226
                    else:
                        if input[0] < 1.224216:
                            var8 = -0.045296196
                        else:
                            var8 = -0.2276561
                else:
                    if input[3] < 0.45116842:
                        if input[7] < -0.23367912:
                            var8 = -0.04437247
                        else:
                            var8 = 0.14960007
                    else:
                        var8 = 0.27069274
        else:
            if input[14] < 1.0:
                if input[7] < 1.3641307:
                    if input[7] < 0.16707173:
                        if input[7] < 0.008812051:
                            var8 = -0.09841795
                        else:
                            var8 = 0.08252351
                    else:
                        if input[1] < 0.10007155:
                            var8 = -0.22012293
                        else:
                            var8 = -0.10704791
                else:
                    if input[0] < -0.0906146:
                        if input[2] < 1.0299541:
                            var8 = 0.26414412
                        else:
                            var8 = -0.14066026
                    else:
                        if input[5] < 0.64104193:
                            var8 = 0.14685461
                        else:
                            var8 = -0.21353279
            else:
                if input[7] < 0.4870541:
                    if input[7] < -0.44317603:
                        if input[2] < -1.3866642:
                            var8 = 0.31021723
                        else:
                            var8 = -0.021866694
                    else:
                        if input[8] < -0.02449371:
                            var8 = -0.08450422
                        else:
                            var8 = -0.3032211
                else:
                    if input[10] < 0.4009349:
                        if input[7] < 1.342763:
                            var8 = 0.14718316
                        else:
                            var8 = -0.07173952
                    else:
                        if input[3] < 1.2051187:
                            var8 = -0.20054024
                        else:
                            var8 = 0.17907579
    else:
        if input[1] < 2.5700943:
            if input[3] < 1.8621627:
                if input[9] < 0.5098685:
                    if input[3] < 0.99953645:
                        if input[10] < 0.61441356:
                            var8 = 0.17943476
                        else:
                            var8 = 0.03498162
                    else:
                        if input[7] < -0.03285734:
                            var8 = -0.20485409
                        else:
                            var8 = 0.12885228
                else:
                    if input[9] < 1.5883477:
                        if input[7] < -0.080064:
                            var8 = 0.021956187
                        else:
                            var8 = -0.10935635
                    else:
                        if input[3] < 0.4278236:
                            var8 = -0.034521293
                        else:
                            var8 = 0.13329229
            else:
                var8 = 0.5528152
        else:
            if input[0] < -1.2397972:
                if input[8] < -0.028158316:
                    var8 = 0.2713095
                else:
                    var8 = -0.22601311
            else:
                if input[7] < 1.5997853:
                    if input[8] < -0.026346205:
                        if input[6] < 0.97067964:
                            var8 = -0.028013093
                        else:
                            var8 = -0.30350518
                    else:
                        if input[7] < -0.58626974:
                            var8 = -0.21065037
                        else:
                            var8 = 0.14177006
                else:
                    var8 = 0.13361625
    if input[4] < 2.5279171:
        if input[4] < 0.8088304:
            if input[0] < -2.4407449:
                if input[14] < 1.0:
                    var9 = 0.45408896
                else:
                    var9 = 0.09228013
            else:
                if input[12] < 1.0:
                    if input[8] < -0.030344337:
                        if input[0] < -0.6496764:
                            var9 = -0.02213504
                        else:
                            var9 = 0.094140925
                    else:
                        if input[3] < 1.4931163:
                            var9 = -0.07955363
                        else:
                            var9 = 0.11974345
                else:
                    if input[3] < 0.18023762:
                        if input[9] < 1.0452287:
                            var9 = -0.26884174
                        else:
                            var9 = -0.025569271
                    else:
                        if input[3] < 1.4018602:
                            var9 = 0.085318856
                        else:
                            var9 = -0.26266694
        else:
            if input[3] < -0.35117662:
                if input[9] < 1.1383348:
                    if input[14] < 1.0:
                        if input[7] < -1.6840237:
                            var9 = 0.11879541
                        else:
                            var9 = -0.22529444
                    else:
                        if input[0] < 0.8100961:
                            var9 = -0.13633204
                        else:
                            var9 = 0.0028677632
                else:
                    if input[5] < 0.64104193:
                        if input[7] < 0.008812051:
                            var9 = -0.13512844
                        else:
                            var9 = 0.30774868
                    else:
                        if input[7] < 1.0687221:
                            var9 = -0.022155466
                        else:
                            var9 = -0.254789
            else:
                if input[7] < 1.57172:
                    if input[8] < -0.024956916:
                        if input[0] < 0.975744:
                            var9 = 0.093075275
                        else:
                            var9 = -0.11281154
                    else:
                        if input[9] < -1.1117297:
                            var9 = 0.11986495
                        else:
                            var9 = -0.07993133
                else:
                    if input[0] < 0.8929201:
                        var9 = -0.24797796
                    else:
                        var9 = -0.070694305
    else:
        if input[1] < 0.3850742:
            if input[8] < -0.028330084:
                if input[7] < 0.608219:
                    if input[0] < 0.012915363:
                        if input[7] < 0.20974475:
                            var9 = 0.14500335
                        else:
                            var9 = -0.11586523
                    else:
                        if input[9] < -0.83241135:
                            var9 = 0.00899572
                        else:
                            var9 = -0.25045088
                else:
                    if input[12] < 1.0:
                        if input[7] < 1.1829834:
                            var9 = 0.03437904
                        else:
                            var9 = 0.26798245
                    else:
                        var9 = -0.018962763
            else:
                if input[3] < 0.5189618:
                    var9 = 0.029434336
                else:
                    if input[9] < -1.0419002:
                        var9 = 0.07213482
                    else:
                        var9 = 0.25853693
        else:
            if input[1] < 2.5700943:
                var9 = 0.28338572
            else:
                var9 = 0.021384541
    if input[1] < -0.37493283:
        if input[3] < 0.5010245:
            if input[0] < 0.2613873:
                if input[3] < -0.08204605:
                    if input[4] < 0.8088304:
                        if input[9] < -1.2669066:
                            var10 = -0.24739897
                        else:
                            var10 = 0.06692103
                    else:
                        if input[0] < -1.7781531:
                            var10 = 0.043987688
                        else:
                            var10 = -0.23445345
                else:
                    if input[1] < -1.3249416:
                        if input[12] < 1.0:
                            var10 = -0.19711566
                        else:
                            var10 = 0.230532
                    else:
                        if input[8] < -0.025942342:
                            var10 = -0.28944752
                        else:
                            var10 = -0.14424098
            else:
                if input[0] < 0.60303617:
                    if input[7] < 0.78405994:
                        if input[7] < -0.5564235:
                            var10 = -0.057619892
                        else:
                            var10 = 0.3878431
                    else:
                        if input[10] < -0.27831548:
                            var10 = -0.24284081
                        else:
                            var10 = -0.01767542
                else:
                    if input[7] < 1.2880503:
                        if input[2] < -1.3866642:
                            var10 = 0.24213077
                        else:
                            var10 = -0.15814741
                    else:
                        if input[1] < -0.6599355:
                            var10 = -0.072149724
                        else:
                            var10 = 0.33902434
        else:
            if input[3] < 0.5189618:
                if input[5] < 0.64104193:
                    var10 = 0.46828952
                else:
                    if input[10] < -0.42926002:
                        var10 = 0.1195003
                    else:
                        var10 = -0.05833842
            else:
                if input[9] < -1.0186236:
                    if input[2] < -1.3866642:
                        if input[6] < 0.97067964:
                            var10 = 0.27974686
                        else:
                            var10 = -0.20384634
                    else:
                        if input[7] < -1.4387897:
                            var10 = 0.13762692
                        else:
                            var10 = -0.2190664
                else:
                    if input[7] < -0.9217739:
                        if input[7] < -1.2830763:
                            var10 = -0.009428554
                        else:
                            var10 = -0.20860222
                    else:
                        if input[7] < -0.6676928:
                            var10 = 0.23283315
                        else:
                            var10 = -0.011894241
    else:
        if input[4] < 2.5279171:
            if input[14] < 1.0:
                if input[0] < -2.4407449:
                    var10 = 0.32333064
                else:
                    if input[2] < 1.7204164:
                        if input[1] < 2.760096:
                            var10 = -0.014384946
                        else:
                            var10 = -0.2192273
                    else:
                        if input[7] < -0.704771:
                            var10 = 0.10101496
                        else:
                            var10 = -0.27247512
            else:
                if input[7] < 0.54616344:
                    if input[9] < -0.8944821:
                        if input[9] < -1.2203535:
                            var10 = -0.057063658
                        else:
                            var10 = 0.21263003
                    else:
                        if input[10] < 0.61441356:
                            var10 = -0.008047346
                        else:
                            var10 = -0.31729773
                else:
                    if input[7] < 1.3543655:
                        if input[0] < 0.27174026:
                            var10 = 0.17443986
                        else:
                            var10 = 0.025414975
                    else:
                        if input[8] < -0.029662345:
                            var10 = 0.05233815
                        else:
                            var10 = -0.1622188
        else:
            if input[8] < -0.03078074:
                if input[4] < 4.247004:
                    if input[7] < -0.4824063:
                        if input[7] < -0.75954294:
                            var10 = 0.066322885
                        else:
                            var10 = -0.21757089
                    else:
                        if input[13] < 1.0:
                            var10 = 0.0006449155
                        else:
                            var10 = 0.18702328
                else:
                    var10 = 0.23617454
            else:
                if input[7] < -1.42103:
                    var10 = 0.048450533
                else:
                    var10 = 0.29185495
    if input[1] < 0.3850742:
        if input[6] < 0.97067964:
            if input[0] < 0.37527025:
                if input[7] < -0.87855613:
                    if input[7] < -1.6840237:
                        if input[11] < 1.0:
                            var11 = 0.3872059
                        else:
                            var11 = -0.17723732
                    else:
                        if input[8] < 0.06511255:
                            var11 = -0.17958608
                        else:
                            var11 = 0.084278665
                else:
                    if input[8] < -0.020337362:
                        if input[0] < -0.18379156:
                            var11 = 0.025914686
                        else:
                            var11 = -0.12820937
                    else:
                        if input[0] < -0.4322635:
                            var11 = 0.036603693
                        else:
                            var11 = 0.3301967
            else:
                if input[0] < 0.4477412:
                    if input[4] < 0.8088304:
                        if input[1] < 0.005070672:
                            var11 = 0.59709704
                        else:
                            var11 = 0.13335298
                    else:
                        if input[8] < -0.029464947:
                            var11 = 0.21402949
                        else:
                            var11 = -0.16909976
                else:
                    if input[7] < -1.5747947:
                        if input[10] < 0.1874562:
                            var11 = -0.31432384
                        else:
                            var11 = -0.060766328
                    else:
                        if input[7] < -1.1183978:
                            var11 = 0.2057985
                        else:
                            var11 = 0.006808295
        else:
            if input[7] < -0.44317603:
                if input[1] < -1.0399389:
                    if input[7] < -0.704771:
                        if input[3] < 1.2553455:
                            var11 = -0.28559166
                        else:
                            var11 = -0.020291205
                    else:
                        var11 = 0.059706654
                else:
                    if input[10] < 1.1481103:
                        if input[7] < -1.0203258:
                            var11 = -0.06459141
                        else:
                            var11 = 0.05285188
                    else:
                        if input[7] < -1.0934299:
                            var11 = 0.39989242
                        else:
                            var11 = -0.00840461
            else:
                if input[7] < 0.15701915:
                    if input[1] < -0.9449381:
                        if input[9] < 0.1684794:
                            var11 = -0.11365583
                        else:
                            var11 = 0.28543895
                    else:
                        if input[8] < -0.032779966:
                            var11 = -0.08859749
                        else:
                            var11 = -0.25684226
                else:
                    if input[14] < 1.0:
                        if input[4] < 0.8088304:
                            var11 = -0.048202794
                        else:
                            var11 = -0.22694628
                    else:
                        if input[10] < -0.71982825:
                            var11 = 0.20257385
                        else:
                            var11 = -0.027841503
    else:
        if input[1] < 3.1400995:
            if input[4] < 2.5279171:
                if input[12] < 1.0:
                    if input[3] < 1.8128457:
                        if input[0] < -1.0741493:
                            var11 = 0.09339834
                        else:
                            var11 = -0.022405386
                    else:
                        if input[9] < -0.16515085:
                            var11 = 0.087446034
                        else:
                            var11 = 0.3869287
                else:
                    if input[3] < 0.17009737:
                        if input[9] < -0.041009367:
                            var11 = -0.024272434
                        else:
                            var11 = -0.28629014
                    else:
                        if input[3] < 1.4619124:
                            var11 = 0.1000736
                        else:
                            var11 = -0.2572556
            else:
                var11 = 0.23989893
        else:
            if input[0] < -1.0741493:
                var11 = 0.023052108
            else:
                if input[3] < 0.94771826:
                    var11 = -0.28344688
                else:
                    var11 = -0.069726236
    if input[4] < 2.5279171:
        if input[1] < -0.18493108:
            if input[9] < 0.9676402:
                if input[10] < -0.761338:
                    if input[0] < 1.2966869:
                        if input[0] < -1.2708561:
                            var12 = 0.30168986
                        else:
                            var12 = -0.04171966
                    else:
                        var12 = 0.31595775
                else:
                    if input[2] < 1.3751853:
                        if input[14] < 1.0:
                            var12 = -0.068456165
                        else:
                            var12 = -0.004766673
                    else:
                        if input[0] < -1.1052083:
                            var12 = 0.13495423
                        else:
                            var12 = -0.24689652
            else:
                if input[3] < -0.63909185:
                    if input[14] < 1.0:
                        var12 = 0.089046076
                    else:
                        var12 = -0.18964866
                else:
                    if input[3] < 1.0212783:
                        var12 = -0.2843353
                    else:
                        var12 = -0.04258627
        else:
            if input[6] < 0.97067964:
                if input[1] < 1.6200856:
                    if input[7] < 0.35555807:
                        if input[7] < -0.23367912:
                            var12 = 0.014456108
                        else:
                            var12 = -0.068028174
                    else:
                        if input[7] < 1.6563303:
                            var12 = 0.069660105
                        else:
                            var12 = -0.11663168
                else:
                    if input[0] < -1.3743862:
                        if input[0] < -1.5193281:
                            var12 = 0.05683871
                        else:
                            var12 = -0.20704807
                    else:
                        if input[0] < -0.0906146:
                            var12 = 0.3238128
                        else:
                            var12 = 0.09576353
            else:
                if input[7] < -1.133428:
                    if input[9] < 0.385727:
                        if input[3] < 0.94295037:
                            var12 = 0.20097305
                        else:
                            var12 = -0.11540406
                    else:
                        if input[8] < 0.1384076:
                            var12 = -0.117618024
                        else:
                            var12 = 0.15661922
                else:
                    if input[5] < 0.64104193:
                        if input[1] < 1.9050882:
                            var12 = 0.05139608
                        else:
                            var12 = -0.17236714
                    else:
                        if input[0] < -2.0680368:
                            var12 = 0.22659527
                        else:
                            var12 = -0.06621633
    else:
        if input[8] < -0.028330084:
            if input[7] < 0.608219:
                if input[10] < 0.89905185:
                    if input[9] < 0.23055014:
                        if input[14] < 1.0:
                            var12 = -0.30866137
                        else:
                            var12 = -0.07092727
                    else:
                        if input[7] < -0.2725314:
                            var12 = -0.030910635
                        else:
                            var12 = 0.2130845
                else:
                    if input[1] < -0.08993021:
                        var12 = -0.036592614
                    else:
                        var12 = 0.18683359
            else:
                if input[3] < 0.5674046:
                    var12 = 0.20536052
                else:
                    var12 = -0.0023399745
        else:
            if input[3] < 0.45116842:
                var12 = 0.058179848
            else:
                var12 = 0.2544641
    if input[10] < 2.8915195:
        if input[6] < 0.97067964:
            if input[1] < 1.4300839:
                if input[1] < -1.3249416:
                    if input[3] < 0.286282:
                        if input[7] < -0.93434393:
                            var13 = 0.10560357
                        else:
                            var13 = -0.2044035
                    else:
                        if input[9] < -0.42895153:
                            var13 = 0.432831
                        else:
                            var13 = 0.018458113
                else:
                    if input[1] < -1.0399389:
                        if input[7] < 0.7475207:
                            var13 = -0.24196441
                        else:
                            var13 = 0.05834089
                    else:
                        if input[3] < 1.5820119:
                            var13 = 0.0032598379
                        else:
                            var13 = 0.13467576
            else:
                if input[0] < -0.22520356:
                    if input[0] < -1.2087382:
                        if input[1] < 2.4750936:
                            var13 = 0.11687361
                        else:
                            var13 = -0.14083871
                    else:
                        var13 = 0.3198398
                else:
                    if input[0] < 0.8929201:
                        if input[2] < -0.35097063:
                            var13 = 0.20689806
                        else:
                            var13 = -0.14269908
                    else:
                        if input[3] < 0.5545477:
                            var13 = 0.3171044
                        else:
                            var13 = -0.017805176
        else:
            if input[3] < 2.0235312:
                if input[9] < -1.2513889:
                    if input[1] < -0.27993196:
                        if input[3] < -0.63909185:
                            var13 = -0.076011516
                        else:
                            var13 = -0.29215252
                    else:
                        if input[7] < -0.12399654:
                            var13 = 0.15644927
                        else:
                            var13 = -0.15564938
                else:
                    if input[0] < 2.0628088:
                        if input[4] < 0.8088304:
                            var13 = -0.0010574923
                        else:
                            var13 = -0.05394448
                    else:
                        if input[2] < 1.3751853:
                            var13 = -0.2723354
                        else:
                            var13 = 0.07128474
            else:
                var13 = 0.3220408
    else:
        if input[7] < -0.9653717:
            if input[11] < 1.0:
                var13 = 0.52833104
            else:
                var13 = 0.10809107
        else:
            if input[8] < -0.026715819:
                if input[3] < 0.20736732:
                    if input[0] < 0.61338913:
                        if input[4] < 2.5279171:
                            var13 = -0.2300429
                        else:
                            var13 = 0.057512153
                    else:
                        var13 = 0.17566614
                else:
                    if input[1] < -0.27993196:
                        var13 = -0.006659488
                    else:
                        if input[3] < 0.671927:
                            var13 = 0.46765792
                        else:
                            var13 = 0.09870521
            else:
                var13 = -0.1936118
    if input[4] < 2.5279171:
        if input[14] < 1.0:
            if input[4] < 0.8088304:
                if input[8] < -0.032779966:
                    if input[0] < -0.9499133:
                        if input[0] < -1.1466203:
                            var14 = 0.019880498
                        else:
                            var14 = -0.30423665
                    else:
                        if input[7] < 1.2062398:
                            var14 = 0.07712464
                        else:
                            var14 = 0.30198237
                else:
                    if input[3] < 0.4385279:
                        if input[9] < 1.6271418:
                            var14 = -0.072763026
                        else:
                            var14 = -0.30955443
                    else:
                        if input[8] < -0.020580398:
                            var14 = -0.037578627
                        else:
                            var14 = 0.057296127
            else:
                if input[8] < -0.030344337:
                    if input[0] < -1.1569732:
                        if input[0] < -1.3122681:
                            var14 = -0.15859193
                        else:
                            var14 = 0.25683218
                    else:
                        if input[7] < -1.6606406:
                            var14 = 0.116103835
                        else:
                            var14 = -0.20703727
                else:
                    if input[0] < -1.0948552:
                        if input[9] < -1.1272473:
                            var14 = 0.20519684
                        else:
                            var14 = -0.20574874
                    else:
                        if input[9] < 1.821113:
                            var14 = 0.033329267
                        else:
                            var14 = -0.23168173
        else:
            if input[9] < 1.4874827:
                if input[3] < 2.0235312:
                    if input[0] < 2.0628088:
                        if input[9] < 1.3633412:
                            var14 = 0.007296322
                        else:
                            var14 = -0.15766427
                    else:
                        if input[8] < 0.017801737:
                            var14 = -0.26200792
                        else:
                            var14 = 0.14971776
                else:
                    var14 = 0.33037817
            else:
                if input[1] < 1.335083:
                    if input[8] < -0.026346205:
                        if input[3] < 0.90806395:
                            var14 = 0.31073797
                        else:
                            var14 = 0.021570995
                    else:
                        if input[7] < -1.3359233:
                            var14 = 0.29872403
                        else:
                            var14 = -0.14872645
                else:
                    if input[8] < -0.030013282:
                        if input[3] < 0.286282:
                            var14 = -0.05622695
                        else:
                            var14 = -0.36506575
                    else:
                        if input[1] < 1.9050882:
                            var14 = -0.101461805
                        else:
                            var14 = 0.21964587
    else:
        if input[8] < -0.028330084:
            if input[7] < -0.5700874:
                if input[6] < 0.97067964:
                    var14 = 0.08166685
                else:
                    var14 = -0.2422308
            else:
                if input[8] < -0.029004993:
                    if input[7] < 1.1829834:
                        if input[7] < -0.33451837:
                            var14 = 0.1982349
                        else:
                            var14 = 0.0044605103
                    else:
                        if input[9] < -0.8944821:
                            var14 = 0.06158666
                        else:
                            var14 = 0.2537207
                else:
                    var14 = -0.09233728
        else:
            if input[8] < 0.008285442:
                if input[5] < 0.64104193:
                    var14 = 0.05685917
                else:
                    var14 = 0.2674462
            else:
                var14 = 0.045374595
    if input[1] < 0.7650777:
        if input[0] < -2.306156:
            if input[7] < -0.45604277:
                var15 = -0.08651611
            else:
                if input[4] < 0.8088304:
                    var15 = 0.31356525
                else:
                    var15 = 0.08169837
        else:
            if input[7] < 1.2062398:
                if input[7] < 0.8763027:
                    if input[12] < 1.0:
                        if input[0] < 1.089627:
                            var15 = -0.015800484
                        else:
                            var15 = -0.11939613
                    else:
                        if input[10] < -0.595299:
                            var15 = 0.12250366
                        else:
                            var15 = -0.021464687
                else:
                    if input[8] < -0.026769944:
                        if input[0] < -0.8981483:
                            var15 = 0.011206267
                        else:
                            var15 = -0.16413482
                    else:
                        if input[3] < 1.5324236:
                            var15 = 0.34206495
                        else:
                            var15 = -0.177645
            else:
                if input[7] < 1.223257:
                    var15 = 0.40185544
                else:
                    if input[3] < 0.7009286:
                        if input[5] < 0.64104193:
                            var15 = 0.16628721
                        else:
                            var15 = 0.0031812738
                    else:
                        if input[7] < 1.6285735:
                            var15 = 0.0028076507
                        else:
                            var15 = -0.24748157
    else:
        if input[0] < 0.7376251:
            if input[0] < 0.1992693:
                if input[7] < 0.66183734:
                    if input[3] < 0.82312626:
                        if input[3] < 0.44567034:
                            var15 = -0.022637188
                        else:
                            var15 = 0.165076
                    else:
                        if input[3] < 1.2132308:
                            var15 = -0.18010564
                        else:
                            var15 = 0.027419794
                else:
                    if input[7] < 0.9514669:
                        if input[3] < 0.25296:
                            var15 = 0.047854576
                        else:
                            var15 = 0.34608066
                    else:
                        if input[14] < 1.0:
                            var15 = -0.06395258
                        else:
                            var15 = 0.15479541
            else:
                if input[0] < 0.5512712:
                    if input[6] < 0.97067964:
                        if input[10] < -0.4956756:
                            var15 = 0.16678795
                        else:
                            var15 = -0.15059018
                    else:
                        if input[9] < 0.8202222:
                            var15 = -0.12987149
                        else:
                            var15 = -0.34882858
                else:
                    if input[0] < 0.62374216:
                        if input[7] < 1.1354:
                            var15 = 0.25463828
                        else:
                            var15 = -0.026958084
                    else:
                        if input[7] < -0.4678239:
                            var15 = 0.07434241
                        else:
                            var15 = -0.24794033
        else:
            if input[0] < 0.8515081:
                if input[8] < -0.023085767:
                    var15 = 0.36481705
                else:
                    if input[0] < 0.7893901:
                        var15 = -0.17350072
                    else:
                        var15 = 0.16629668
            else:
                if input[0] < 0.9136261:
                    if input[7] < 0.8349633:
                        var15 = -0.32430518
                    else:
                        var15 = 0.06450511
                else:
                    if input[7] < -1.2713257:
                        if input[9] < -0.74706405:
                            var15 = 0.01775536
                        else:
                            var15 = 0.34444705
                    else:
                        if input[7] < -0.9653717:
                            var15 = -0.16103561
                        else:
                            var15 = 0.093705066
    if input[4] < 2.5279171:
        if input[1] < 3.1400995:
            if input[1] < 0.7650777:
                if input[8] < 0.1384076:
                    if input[8] < -0.020580398:
                        if input[8] < -0.02449371:
                            var16 = -0.009851326
                        else:
                            var16 = -0.08917902
                    else:
                        if input[7] < -0.71973884:
                            var16 = -0.0040224576
                        else:
                            var16 = 0.11428863
                else:
                    if input[0] < -1.1052083:
                        if input[8] < 0.39041746:
                            var16 = -0.032242317
                        else:
                            var16 = 0.34718475
                    else:
                        if input[1] < 0.3850742:
                            var16 = -0.27206948
                        else:
                            var16 = -0.0034121228
            else:
                if input[9] < 0.26934436:
                    if input[9] < -0.5142988:
                        if input[8] < -0.016679041:
                            var16 = 0.0505266
                        else:
                            var16 = -0.15584388
                    else:
                        if input[1] < 1.8100873:
                            var16 = 0.17157242
                        else:
                            var16 = -0.008270584
                else:
                    if input[0] < 0.7065661:
                        if input[0] < 0.17856331:
                            var16 = 0.0046667918
                        else:
                            var16 = -0.1306562
                    else:
                        if input[14] < 1.0:
                            var16 = -0.044051338
                        else:
                            var16 = 0.15842155
        else:
            if input[0] < -1.0741493:
                var16 = 0.036243714
            else:
                var16 = -0.23081076
    else:
        if input[4] < 4.247004:
            if input[8] < -0.028330084:
                if input[9] < 0.23055014:
                    if input[9] < -1.2048358:
                        var16 = 0.14775161
                    else:
                        if input[7] < 1.1829834:
                            var16 = -0.14326006
                        else:
                            var16 = 0.05510691
                else:
                    if input[7] < -0.2725314:
                        if input[9] < 1.0452287:
                            var16 = 0.09407211
                        else:
                            var16 = -0.13083354
                    else:
                        var16 = 0.26948214
            else:
                if input[8] < -0.021797404:
                    var16 = 0.22990419
                else:
                    var16 = 0.06084005
        else:
            var16 = 0.24083623
    if input[4] < 2.5279171:
        if input[0] < -1.4365041:
            if input[10] < -0.006615333:
                if input[0] < -2.306156:
                    if input[7] < -0.40280506:
                        var17 = -0.10745436
                    else:
                        if input[3] < 0.3463231:
                            var17 = 0.31578368
                        else:
                            var17 = 0.050246723
                else:
                    if input[8] < -0.023865093:
                        if input[7] < 1.1354:
                            var17 = -0.2266791
                        else:
                            var17 = -0.0349409
                    else:
                        if input[11] < 1.0:
                            var17 = -0.112749584
                        else:
                            var17 = 0.17827524
            else:
                if input[1] < 0.10007155:
                    if input[12] < 1.0:
                        var17 = -0.2368164
                    else:
                        var17 = 0.13175113
                else:
                    if input[7] < -0.40280506:
                        var17 = 0.3729007
                    else:
                        if input[7] < 0.022111539:
                            var17 = -0.3731786
                        else:
                            var17 = 0.18761656
        else:
            if input[0] < -1.1776792:
                if input[9] < -1.24363:
                    if input[14] < 1.0:
                        var17 = -0.029185006
                    else:
                        var17 = -0.30784643
                else:
                    if input[9] < -0.8867233:
                        if input[8] < -0.019266702:
                            var17 = 0.38049498
                        else:
                            var17 = -0.014493243
                    else:
                        if input[7] < 0.54616344:
                            var17 = -0.019665226
                        else:
                            var17 = 0.16065642
            else:
                if input[12] < 1.0:
                    if input[3] < 1.5582843:
                        if input[3] < 0.30654135:
                            var17 = 0.007720886
                        else:
                            var17 = -0.056260705
                    else:
                        if input[0] < -0.049202614:
                            var17 = -0.037345253
                        else:
                            var17 = 0.19975336
                else:
                    if input[3] < 0.17009737:
                        if input[9] < -0.14963317:
                            var17 = -0.09211505
                        else:
                            var17 = -0.26515135
                    else:
                        if input[3] < 1.2736435:
                            var17 = 0.055369135
                        else:
                            var17 = -0.18370135
    else:
        if input[4] < 4.247004:
            if input[8] < -0.028330084:
                if input[9] < 0.23055014:
                    if input[9] < 0.059855595:
                        if input[1] < 0.3850742:
                            var17 = -0.029495416
                        else:
                            var17 = 0.17649561
                    else:
                        var17 = -0.17589773
                else:
                    if input[7] < -0.2725314:
                        if input[9] < 1.0452287:
                            var17 = 0.07905938
                        else:
                            var17 = -0.11046024
                    else:
                        var17 = 0.24363114
            else:
                if input[8] < -0.021797404:
                    var17 = 0.21201982
                else:
                    var17 = 0.05005293
        else:
            var17 = 0.22227593
    if input[6] < 0.97067964:
        if input[1] < 1.6200856:
            if input[7] < -0.71973884:
                if input[0] < 1.5762178:
                    if input[10] < -0.42926002:
                        if input[3] < 0.8783539:
                            var18 = -0.022359606
                        else:
                            var18 = -0.24617678
                    else:
                        if input[3] < 0.8941428:
                            var18 = -0.041567005
                        else:
                            var18 = 0.12753373
                else:
                    if input[8] < -0.0066573843:
                        if input[9] < 0.09864981:
                            var18 = 0.16823734
                        else:
                            var18 = -0.13675466
                    else:
                        if input[10] < -0.5500156:
                            var18 = 0.55228704
                        else:
                            var18 = 0.009433659
            else:
                if input[8] < -0.022184744:
                    if input[0] < 1.3691579:
                        if input[3] < 1.0300175:
                            var18 = 0.031015676
                        else:
                            var18 = -0.067446254
                    else:
                        if input[7] < 1.376414:
                            var18 = -0.17060927
                        else:
                            var18 = 0.10444633
                else:
                    if input[10] < -0.595299:
                        if input[3] < 0.7803133:
                            var18 = -0.09048067
                        else:
                            var18 = 0.3163263
                    else:
                        if input[9] < -0.49102226:
                            var18 = 0.17037508
                        else:
                            var18 = -0.13029206
        else:
            if input[7] < 1.2988641:
                if input[0] < -1.4261512:
                    var18 = -0.08993366
                else:
                    if input[4] < 0.8088304:
                        if input[1] < 2.855097:
                            var18 = 0.30044222
                        else:
                            var18 = 0.043407127
                    else:
                        if input[0] < 0.2096223:
                            var18 = 0.18258691
                        else:
                            var18 = -0.18744367
            else:
                if input[7] < 1.4498934:
                    var18 = -0.3679163
                else:
                    var18 = 0.22252181
    else:
        if input[1] < -1.2299408:
            if input[0] < -0.03884962:
                if input[3] < 1.0123969:
                    if input[8] < -0.031374626:
                        if input[0] < -0.80497134:
                            var18 = -0.12143954
                        else:
                            var18 = 0.38105488
                    else:
                        var18 = -0.26472926
                else:
                    var18 = 0.26693973
            else:
                var18 = -0.28538626
        else:
            if input[1] < 2.3800926:
                if input[10] < 2.8915195:
                    if input[0] < -0.6289704:
                        if input[9] < 0.47107428:
                            var18 = 0.0050483723
                        else:
                            var18 = -0.14584544
                    else:
                        if input[0] < -0.028496623:
                            var18 = 0.070300356
                        else:
                            var18 = -0.026920848
                else:
                    if input[7] < -0.9653717:
                        var18 = 0.44387677
                    else:
                        if input[8] < -0.02681526:
                            var18 = 0.13917916
                        else:
                            var18 = -0.22217397
            else:
                if input[3] < 0.61084086:
                    if input[2] < 1.0299541:
                        if input[0] < -1.2397972:
                            var18 = -0.067326345
                        else:
                            var18 = -0.30659452
                    else:
                        if input[9] < 2.9849393:
                            var18 = 0.17415151
                        else:
                            var18 = -0.19626285
                else:
                    if input[3] < 1.0300175:
                        if input[7] < -0.24950548:
                            var18 = -0.07568387
                        else:
                            var18 = 0.29572865
                    else:
                        var18 = -0.23397398
    if input[0] < 0.7893901:
        if input[1] < 2.4750936:
            if input[0] < 0.7583311:
                if input[1] < -1.6099442:
                    if input[5] < 0.64104193:
                        var19 = 0.0065507134
                    else:
                        var19 = -0.24028455
                else:
                    if input[8] < -0.013475031:
                        if input[8] < -0.015660465:
                            var19 = -0.005334071
                        else:
                            var19 = -0.17477162
                    else:
                        if input[9] < -0.0022151496:
                            var19 = 0.092650324
                        else:
                            var19 = -0.027515851
            else:
                if input[10] < -0.4956756:
                    if input[7] < 0.5943842:
                        var19 = -0.35594124
                    else:
                        var19 = -0.03786169
                else:
                    if input[10] < -0.19680543:
                        var19 = 0.35544956
                    else:
                        var19 = -0.21244274
        else:
            if input[8] < -0.029541105:
                if input[0] < -1.3950921:
                    var19 = -0.057261158
                else:
                    var19 = -0.2373389
            else:
                if input[8] < -0.028158316:
                    if input[0] < -0.9292073:
                        var19 = 0.24016981
                    else:
                        var19 = -0.03286191
                else:
                    if input[0] < 0.16821031:
                        if input[4] < 0.8088304:
                            var19 = -0.22444353
                        else:
                            var19 = -0.024295455
                    else:
                        var19 = 0.048156746
    else:
        if input[0] < 0.8100961:
            if input[8] < -0.027020918:
                if input[7] < 1.0826854:
                    var19 = -0.09898523
                else:
                    var19 = 0.26031542
            else:
                var19 = 0.5692026
        else:
            if input[10] < -0.5500156:
                if input[1] < -1.4199425:
                    var19 = 0.3886172
                else:
                    if input[12] < 1.0:
                        if input[6] < 0.97067964:
                            var19 = 0.0920263
                        else:
                            var19 = -0.09146046
                    else:
                        if input[6] < 0.97067964:
                            var19 = 0.022224583
                        else:
                            var19 = 0.26937765
            else:
                if input[0] < 1.4830408:
                    if input[8] < -0.015036962:
                        if input[7] < 1.6715614:
                            var19 = 0.07047229
                        else:
                            var19 = -0.28114942
                    else:
                        if input[0] < 1.2035099:
                            var19 = -0.20561786
                        else:
                            var19 = 0.041515384
                else:
                    if input[7] < -0.6532165:
                        if input[7] < -0.87855613:
                            var19 = -0.03391564
                        else:
                            var19 = 0.37232614
                    else:
                        if input[1] < 0.8600786:
                            var19 = -0.2412541
                        else:
                            var19 = -0.047575083
    if input[4] < 2.5279171:
        if input[10] < 0.61441356:
            if input[9] < -1.24363:
                if input[13] < 1.0:
                    if input[1] < -0.9449381:
                        if input[8] < -0.0227347:
                            var20 = -0.2081335
                        else:
                            var20 = 0.17617498
                    else:
                        if input[0] < -0.9499133:
                            var20 = -0.06103879
                        else:
                            var20 = -0.29525965
                else:
                    var20 = 0.11985189
            else:
                if input[9] < -0.94103515:
                    if input[8] < -0.023290314:
                        if input[3] < 0.6153049:
                            var20 = 0.03668277
                        else:
                            var20 = 0.20829506
                    else:
                        if input[13] < 1.0:
                            var20 = 0.03771001
                        else:
                            var20 = -0.26439008
                else:
                    if input[0] < -1.3433272:
                        if input[13] < 1.0:
                            var20 = -0.018344276
                        else:
                            var20 = -0.15906039
                    else:
                        if input[0] < -1.0741493:
                            var20 = 0.101594545
                        else:
                            var20 = -0.0016813572
        else:
            if input[9] < -0.7936171:
                if input[7] < 0.608219:
                    if input[3] < 0.5055981:
                        if input[8] < -0.024182342:
                            var20 = 0.004131688
                        else:
                            var20 = -0.22148941
                    else:
                        if input[3] < 0.5495229:
                            var20 = 0.43035877
                        else:
                            var20 = 0.0487147
                else:
                    if input[7] < 1.342763:
                        if input[13] < 1.0:
                            var20 = -0.27537936
                        else:
                            var20 = -0.029081946
                    else:
                        if input[8] < -0.030110784:
                            var20 = 0.18435541
                        else:
                            var20 = -0.124965645
            else:
                if input[1] < 1.5250847:
                    var20 = -0.3183449
                else:
                    var20 = -0.074136846
    else:
        if input[1] < 0.3850742:
            if input[1] < 0.10007155:
                if input[0] < 0.023268359:
                    if input[1] < -0.8499372:
                        var20 = 0.017316826
                    else:
                        var20 = 0.21327035
                else:
                    if input[7] < 0.14232793:
                        if input[7] < -0.45604277:
                            var20 = 0.003750052
                        else:
                            var20 = -0.14051965
                    else:
                        if input[6] < 0.97067964:
                            var20 = 0.22974366
                        else:
                            var20 = -0.017968137
            else:
                if input[0] < -0.4115575:
                    var20 = 0.08325595
                else:
                    if input[6] < 0.97067964:
                        var20 = -0.21116859
                    else:
                        var20 = 0.047713522
        else:
            if input[0] < -0.84638333:
                var20 = 0.033411168
            else:
                var20 = 0.20139012
    if input[1] < 0.7650777:
        if input[10] < -0.761338:
            if input[0] < -1.747094:
                if input[7] < -0.065822795:
                    var21 = 0.09482133
                else:
                    var21 = 0.34161946
            else:
                if input[8] < -0.023085767:
                    if input[7] < 0.2887667:
                        if input[0] < -0.3701455:
                            var21 = 0.041066542
                        else:
                            var21 = -0.19483425
                    else:
                        if input[14] < 1.0:
                            var21 = -0.105378464
                        else:
                            var21 = 0.15040478
                else:
                    if input[0] < -1.2087382:
                        var21 = -0.18640336
                    else:
                        if input[7] < -0.33451837:
                            var21 = 0.072890416
                        else:
                            var21 = 0.3116793
        else:
            if input[10] < -0.66645855:
                if input[0] < 0.27174026:
                    if input[0] < 0.16821031:
                        if input[9] < 1.122817:
                            var21 = -0.059047338
                        else:
                            var21 = 0.12446558
                    else:
                        if input[3] < 0.32362035:
                            var21 = 0.50972116
                        else:
                            var21 = 0.0049788477
                else:
                    if input[9] < 0.781428:
                        if input[8] < -0.01822945:
                            var21 = 0.02737412
                        else:
                            var21 = -0.22061343
                    else:
                        if input[0] < 1.3484519:
                            var21 = -0.29627708
                        else:
                            var21 = 0.023696665
            else:
                if input[10] < -0.5500156:
                    if input[1] < 0.3850742:
                        if input[0] < 1.0792739:
                            var21 = 0.037514813
                        else:
                            var21 = 0.20617278
                    else:
                        if input[8] < -0.030154988:
                            var21 = 0.108963594
                        else:
                            var21 = -0.20614634
                else:
                    if input[0] < 1.4830408:
                        if input[3] < 0.5095043:
                            var21 = -0.03286318
                        else:
                            var21 = 0.018552804
                    else:
                        if input[7] < -0.5700874:
                            var21 = 0.01839014
                        else:
                            var21 = -0.21775906
    else:
        if input[3] < 1.8621627:
            if input[0] < 0.5512712:
                if input[0] < 0.1992693:
                    if input[3] < 1.4619124:
                        if input[0] < 0.106092334:
                            var21 = 0.018448193
                        else:
                            var21 = 0.21474567
                    else:
                        if input[1] < 1.2400821:
                            var21 = -0.33471635
                        else:
                            var21 = -0.0051644286
                else:
                    if input[6] < 0.97067964:
                        if input[7] < 0.78405994:
                            var21 = -0.10382731
                        else:
                            var21 = 0.18189418
                    else:
                        if input[7] < 1.2988641:
                            var21 = -0.23429911
                        else:
                            var21 = 0.055344757
            else:
                if input[7] < 0.39287364:
                    if input[1] < 1.335083:
                        if input[0] < 0.7790371:
                            var21 = 0.34267327
                        else:
                            var21 = 0.083508044
                    else:
                        if input[0] < 0.7893901:
                            var21 = -0.16252673
                        else:
                            var21 = 0.077872194
                else:
                    if input[7] < 0.9084869:
                        if input[5] < 0.64104193:
                            var21 = 0.07110649
                        else:
                            var21 = -0.33481532
                    else:
                        if input[7] < 1.2604674:
                            var21 = 0.2543847
                        else:
                            var21 = -0.025544038
        else:
            var21 = 0.2773655
    if input[4] < 2.5279171:
        if input[1] < -0.18493108:
            if input[13] < 1.0:
                if input[0] < 1.141392:
                    if input[0] < 0.92397904:
                        if input[0] < 0.2613873:
                            var22 = -0.06855625
                        else:
                            var22 = 0.009021463
                    else:
                        if input[1] < -0.9449381:
                            var22 = 0.06147563
                        else:
                            var22 = -0.2626715
                else:
                    if input[0] < 1.2035099:
                        if input[10] < -0.595299:
                            var22 = 0.06257144
                        else:
                            var22 = 0.4284885
                    else:
                        if input[9] < -1.0186236:
                            var22 = -0.16477515
                        else:
                            var22 = 0.08111076
            else:
                if input[0] < 1.058568:
                    if input[9] < -0.9798294:
                        if input[0] < -0.049202614:
                            var22 = 0.080858335
                        else:
                            var22 = 0.28513175
                    else:
                        if input[0] < 0.1889163:
                            var22 = 0.083633155
                        else:
                            var22 = -0.100908756
                else:
                    if input[7] < -0.9653717:
                        var22 = -0.06756653
                    else:
                        var22 = -0.2710416
        else:
            if input[10] < 0.61441356:
                if input[3] < 1.195201:
                    if input[3] < 1.0757194:
                        if input[10] < -0.006615333:
                            var22 = -0.00087176426
                        else:
                            var22 = 0.065681815
                    else:
                        if input[11] < 1.0:
                            var22 = 0.03838183
                        else:
                            var22 = 0.2756387
                else:
                    if input[1] < 0.005070672:
                        if input[0] < -1.0534433:
                            var22 = -0.029190965
                        else:
                            var22 = -0.260081
                    else:
                        if input[8] < -0.026769944:
                            var22 = -0.16942887
                        else:
                            var22 = 0.022757906
            else:
                if input[9] < -0.7936171:
                    if input[7] < -0.2725314:
                        if input[8] < 0.07376749:
                            var22 = 0.09497455
                        else:
                            var22 = -0.2533544
                    else:
                        if input[3] < -0.19682488:
                            var22 = -0.21067919
                        else:
                            var22 = -0.011257658
                else:
                    if input[1] < 1.5250847:
                        var22 = -0.28447047
                    else:
                        var22 = -0.07359781
    else:
        if input[3] < 0.8180369:
            if input[7] < 0.608219:
                if input[6] < 0.97067964:
                    if input[0] < -0.31838053:
                        var22 = 0.19261687
                    else:
                        if input[0] < 0.62374216:
                            var22 = -0.11583398
                        else:
                            var22 = 0.080678985
                else:
                    if input[9] < 0.7659103:
                        if input[9] < -1.2125946:
                            var22 = 0.060094867
                        else:
                            var22 = -0.18003088
                    else:
                        var22 = 0.058552165
            else:
                if input[12] < 1.0:
                    if input[0] < -0.3908515:
                        var22 = 0.016802322
                    else:
                        var22 = 0.21662581
                else:
                    var22 = 0.012255407
        else:
            var22 = 0.19075297
    if input[14] < 1.0:
        if input[7] < 1.3543655:
            if input[7] < 0.73314714:
                if input[0] < 1.8246897:
                    if input[0] < 1.182804:
                        if input[0] < 0.98609704:
                            var23 = -0.009515954
                        else:
                            var23 = 0.13255772
                    else:
                        if input[3] < 1.103888:
                            var23 = -0.12222454
                        else:
                            var23 = 0.109957345
                else:
                    if input[3] < 0.594254:
                        if input[9] < -0.553093:
                            var23 = -0.09591829
                        else:
                            var23 = 0.28853375
                    else:
                        if input[6] < 0.97067964:
                            var23 = 0.045795225
                        else:
                            var23 = -0.14159086
            else:
                if input[9] < 0.19175592:
                    if input[7] < 1.1220839:
                        if input[8] < -0.027242165:
                            var23 = -0.23629132
                        else:
                            var23 = -0.0018212812
                    else:
                        if input[7] < 1.1829834:
                            var23 = 0.18602395
                        else:
                            var23 = -0.1464352
                else:
                    if input[9] < 0.26934436:
                        var23 = 0.25119317
                    else:
                        if input[3] < 0.5895688:
                            var23 = -0.13232537
                        else:
                            var23 = 0.038885698
        else:
            if input[10] < -0.66645855:
                if input[3] < -0.63909185:
                    var23 = 0.1904407
                else:
                    if input[8] < -0.029952338:
                        var23 = -0.30340967
                    else:
                        if input[3] < 0.6426471:
                            var23 = 0.33131725
                        else:
                            var23 = -0.16570628
            else:
                if input[10] < -0.5500156:
                    if input[13] < 1.0:
                        if input[1] < 0.67007685:
                            var23 = 0.4559878
                        else:
                            var23 = 0.029749304
                    else:
                        var23 = -0.07633349
                else:
                    if input[7] < 1.6966289:
                        if input[0] < -1.1776792:
                            var23 = 0.29232284
                        else:
                            var23 = 0.062008794
                    else:
                        if input[1] < 0.3850742:
                            var23 = -0.23691732
                        else:
                            var23 = 0.00034862274
    else:
        if input[0] < 2.0628088:
            if input[7] < 0.54616344:
                if input[0] < 0.106092334:
                    if input[7] < 0.15701915:
                        if input[7] < 0.07269609:
                            var23 = -0.044017475
                        else:
                            var23 = -0.25508454
                    else:
                        if input[7] < 0.3281733:
                            var23 = 0.1823065
                        else:
                            var23 = -0.06484221
                else:
                    if input[7] < -1.1183978:
                        if input[3] < 0.9126434:
                            var23 = 0.19095823
                        else:
                            var23 = -0.076104224
                    else:
                        if input[0] < 0.17856331:
                            var23 = 0.2587456
                        else:
                            var23 = -0.024400568
            else:
                if input[8] < -0.027456515:
                    if input[0] < -0.21485056:
                        if input[8] < -0.029375087:
                            var23 = 0.12121129
                        else:
                            var23 = -0.007847133
                    else:
                        if input[0] < -0.06990861:
                            var23 = -0.24262173
                        else:
                            var23 = -0.006161585
                else:
                    if input[10] < -0.71982825:
                        if input[6] < 0.97067964:
                            var23 = 0.10255906
                        else:
                            var23 = -0.25684145
                    else:
                        if input[0] < -0.3390865:
                            var23 = 0.07527141
                        else:
                            var23 = 0.3161219
        else:
            if input[9] < -0.95655286:
                var23 = 0.17949106
            else:
                if input[9] < 1.2081643:
                    if input[7] < -1.2938153:
                        var23 = -0.09394448
                    else:
                        var23 = -0.35418668
                else:
                    var23 = 0.0009490585
    if input[6] < 0.97067964:
        if input[1] < 1.2400821:
            if input[1] < -1.3249416:
                if input[0] < -0.9499133:
                    if input[3] < 0.32362035:
                        var24 = -0.022841454
                    else:
                        var24 = -0.20166695
                else:
                    if input[8] < -0.028330084:
                        if input[0] < 0.8308021:
                            var24 = -0.10522804
                        else:
                            var24 = 0.17722079
                    else:
                        if input[8] < -0.019869125:
                            var24 = 0.38883594
                        else:
                            var24 = 0.015494929
            else:
                if input[1] < -1.2299408:
                    var24 = -0.25868043
                else:
                    if input[7] < -1.2938153:
                        if input[3] < 1.0757194:
                            var24 = -0.07589322
                        else:
                            var24 = 0.10105487
                    else:
                        if input[7] < -1.2378846:
                            var24 = 0.22766529
                        else:
                            var24 = 0.0040612766
        else:
            if input[0] < -0.47367546:
                if input[10] < 1.2975454:
                    if input[7] < 1.4206333:
                        if input[0] < -1.4261512:
                            var24 = 0.085245185
                        else:
                            var24 = 0.2978513
                    else:
                        var24 = -0.046612643
                else:
                    var24 = -0.0830234
            else:
                if input[8] < -0.028844493:
                    if input[10] < -0.5500156:
                        var24 = 0.26552343
                    else:
                        if input[7] < 0.8908117:
                            var24 = 0.096722655
                        else:
                            var24 = -0.16341364
                else:
                    if input[3] < 0.9687012:
                        if input[10] < -0.34624052:
                            var24 = -0.2529519
                        else:
                            var24 = 0.07229511
                    else:
                        if input[7] < 0.34157342:
                            var24 = 0.2634371
                        else:
                            var24 = -0.004924781
    else:
        if input[8] < 0.27596393:
            if input[7] < -1.6440885:
                if input[9] < -0.8401702:
                    var24 = 0.06822497
                else:
                    var24 = -0.30525404
            else:
                if input[7] < -1.4827619:
                    if input[7] < -1.5337794:
                        if input[2] < 0.68472284:
                            var24 = 0.08348288
                        else:
                            var24 = -0.20330888
                    else:
                        if input[14] < 1.0:
                            var24 = -0.020013925
                        else:
                            var24 = 0.455031
                else:
                    if input[1] < 1.8100873:
                        if input[1] < 0.10007155:
                            var24 = -0.037605673
                        else:
                            var24 = 0.015604873
                    else:
                        if input[3] < 0.980734:
                            var24 = -0.039113007
                        else:
                            var24 = -0.2173077
        else:
            if input[1] < 0.3850742:
                var24 = -0.008259483
            else:
                if input[11] < 1.0:
                    var24 = 0.33256343
                else:
                    var24 = 0.017232276
    if input[4] < 2.5279171:
        if input[4] < 0.8088304:
            if input[8] < -0.027789427:
                if input[8] < -0.028330084:
                    if input[8] < -0.028445441:
                        if input[9] < 0.47107428:
                            var25 = 0.041551784
                        else:
                            var25 = -0.017844288
                    else:
                        if input[0] < -0.82567734:
                            var25 = -0.06810901
                        else:
                            var25 = -0.2742724
                else:
                    if input[8] < -0.028158316:
                        if input[7] < 1.2988641:
                            var25 = 0.41702962
                        else:
                            var25 = -0.025693221
                    else:
                        if input[8] < -0.028055904:
                            var25 = -0.23218271
                        else:
                            var25 = 0.16420148
            else:
                if input[8] < -0.027137408:
                    if input[7] < 0.16707173:
                        if input[6] < 0.97067964:
                            var25 = 0.29833695
                        else:
                            var25 = -0.16857383
                    else:
                        if input[9] < -0.7858583:
                            var25 = 0.0053123455
                        else:
                            var25 = -0.22381625
                else:
                    if input[1] < 1.0500803:
                        if input[1] < 0.95507944:
                            var25 = -0.0061405483
                        else:
                            var25 = -0.2358026
                    else:
                        if input[0] < -1.2915622:
                            var25 = -0.14381863
                        else:
                            var25 = 0.08199342
        else:
            if input[8] < -0.030567229:
                if input[9] < 0.71935725:
                    if input[0] < -1.6021521:
                        if input[7] < 0.8908117:
                            var25 = -0.15566757
                        else:
                            var25 = 0.3089259
                    else:
                        if input[9] < -0.8944821:
                            var25 = -0.0108937835
                        else:
                            var25 = -0.17355368
                else:
                    if input[0] < 1.058568:
                        if input[11] < 1.0:
                            var25 = -0.09214105
                        else:
                            var25 = 0.11492678
                    else:
                        if input[1] < 1.2400821:
                            var25 = -0.22212358
                        else:
                            var25 = -0.03342835
            else:
                if input[8] < -0.029606093:
                    if input[7] < 1.5132883:
                        if input[0] < 0.8722141:
                            var25 = 0.30155012
                        else:
                            var25 = -0.089005835
                    else:
                        if input[3] < 0.5674046:
                            var25 = -0.16873991
                        else:
                            var25 = 0.01730349
                else:
                    if input[13] < 1.0:
                        if input[3] < 0.8488668:
                            var25 = 0.013470176
                        else:
                            var25 = -0.09222502
                    else:
                        if input[3] < 1.2736435:
                            var25 = 0.0056024236
                        else:
                            var25 = 0.35378614
    else:
        if input[0] < 1.224216:
            if input[4] < 4.247004:
                if input[8] < -0.028330084:
                    if input[9] < 0.23055014:
                        if input[13] < 1.0:
                            var25 = -0.10325702
                        else:
                            var25 = 0.03947444
                    else:
                        if input[7] < -0.2725314:
                            var25 = -0.031230276
                        else:
                            var25 = 0.19252427
                else:
                    if input[0] < -0.20449756:
                        var25 = 0.17784628
                    else:
                        var25 = 0.032541063
            else:
                var25 = 0.18631408
        else:
            var25 = 0.19725007
    if input[0] < -2.4407449:
        if input[14] < 1.0:
            if input[10] < -0.595299:
                var26 = 0.2572766
            else:
                var26 = 0.07072967
        else:
            var26 = -0.016796082
    else:
        if input[1] < 3.4251022:
            if input[9] < 1.4331708:
                if input[0] < -1.923095:
                    if input[9] < -0.0022151496:
                        if input[9] < -0.18066853:
                            var26 = -0.078593045
                        else:
                            var26 = 0.3310281
                    else:
                        if input[0] < -2.140508:
                            var26 = -0.010711102
                        else:
                            var26 = -0.29127783
                else:
                    if input[8] < 0.1384076:
                        if input[8] < 0.05595688:
                            var26 = -0.0032142792
                        else:
                            var26 = 0.11425753
                    else:
                        if input[0] < -1.1052083:
                            var26 = 0.18704653
                        else:
                            var26 = -0.15334344
            else:
                if input[3] < 0.8433095:
                    if input[9] < 1.5573123:
                        if input[7] < -1.2026373:
                            var26 = -0.08861051
                        else:
                            var26 = 0.28501627
                    else:
                        if input[7] < 1.1123637:
                            var26 = 0.070218526
                        else:
                            var26 = -0.09762563
                else:
                    if input[5] < 0.64104193:
                        if input[14] < 1.0:
                            var26 = -0.0016304364
                        else:
                            var26 = 0.23807195
                    else:
                        if input[0] < -0.3908515:
                            var26 = 0.012201802
                        else:
                            var26 = -0.25935915
        else:
            var26 = -0.2166584
    if input[1] < -1.6099442:
        if input[5] < 0.64104193:
            var27 = 0.032707013
        else:
            if input[12] < 1.0:
                var27 = -0.22364925
            else:
                var27 = -0.064425066
    else:
        if input[1] < -1.5149434:
            if input[8] < -0.027423343:
                if input[0] < -0.6393234:
                    var27 = 0.040242095
                else:
                    var27 = -0.18560301
            else:
                if input[8] < -0.022858713:
                    var27 = 0.46128413
                else:
                    var27 = -0.05201831
        else:
            if input[1] < -1.4199425:
                if input[8] < -0.025015872:
                    if input[8] < -0.028330084:
                        var27 = -0.1279237
                    else:
                        var27 = 0.13690819
                else:
                    var27 = -0.2381087
            else:
                if input[1] < -1.3249416:
                    if input[10] < -0.42926002:
                        if input[8] < -0.02477459:
                            var27 = -0.23094413
                        else:
                            var27 = 0.12065727
                    else:
                        if input[6] < 0.97067964:
                            var27 = 0.38144293
                        else:
                            var27 = 0.043948002
                else:
                    if input[1] < -1.2299408:
                        if input[8] < -0.019266702:
                            var27 = -0.27589265
                        else:
                            var27 = 0.010887591
                    else:
                        if input[10] < 0.4009349:
                            var27 = 0.00608842
                        else:
                            var27 = -0.018126303
    if input[4] < 2.5279171:
        if input[0] < -2.4407449:
            if input[7] < 0.45228475:
                var28 = 0.0037377262
            else:
                var28 = 0.21123807
        else:
            if input[1] < 3.4251022:
                if input[10] < -0.761338:
                    if input[13] < 1.0:
                        if input[0] < 1.2966869:
                            var28 = 0.020461883
                        else:
                            var28 = 0.18972094
                    else:
                        if input[9] < 0.87453413:
                            var28 = 0.22962977
                        else:
                            var28 = -0.1296406
                else:
                    if input[7] < 1.7370887:
                        if input[2] < 1.3751853:
                            var28 = -0.0019266076
                        else:
                            var28 = -0.060761984
                    else:
                        var28 = -0.19442049
            else:
                var28 = -0.19117036
    else:
        if input[1] < 0.3850742:
            if input[1] < 0.10007155:
                if input[0] < 0.023268359:
                    if input[1] < -0.8499372:
                        var28 = 0.015422287
                    else:
                        var28 = 0.18612504
                else:
                    if input[0] < 0.35456425:
                        var28 = -0.13225959
                    else:
                        if input[3] < -0.63909185:
                            var28 = -0.013611668
                        else:
                            var28 = 0.19537976
            else:
                if input[0] < -0.4115575:
                    var28 = 0.08712515
                else:
                    if input[14] < 1.0:
                        var28 = -0.16234311
                    else:
                        var28 = -0.0072005233
        else:
            if input[7] < -0.29495046:
                var28 = 0.045677125
            else:
                var28 = 0.19474477
    if input[10] < 2.8915195:
        if input[9] < -1.142765:
            if input[3] < 1.2936667:
                if input[3] < 1.1531873:
                    if input[12] < 1.0:
                        if input[7] < -0.28583017:
                            var29 = -0.0065793097
                        else:
                            var29 = -0.14199857
                    else:
                        if input[3] < 0.5010245:
                            var29 = -0.11102826
                        else:
                            var29 = 0.14863689
                else:
                    if input[0] < -0.45296946:
                        var29 = 0.5535608
                    else:
                        var29 = -0.019838843
            else:
                if input[0] < 0.5098592:
                    var29 = -0.32695267
                else:
                    var29 = 0.026167067
        else:
            if input[9] < -1.1117297:
                if input[3] < 0.7803133:
                    if input[6] < 0.97067964:
                        var29 = 0.33562204
                    else:
                        if input[0] < -0.19414456:
                            var29 = 0.17998424
                        else:
                            var29 = -0.09672693
                else:
                    if input[7] < -0.35611662:
                        var29 = -0.22361083
                    else:
                        var29 = 0.034565646
            else:
                if input[7] < 0.67438555:
                    if input[0] < 1.9282197:
                        if input[7] < 0.5360101:
                            var29 = -0.00023557064
                        else:
                            var29 = -0.06760726
                    else:
                        if input[8] < -0.009021918:
                            var29 = -0.14320703
                        else:
                            var29 = 0.12081062
                else:
                    if input[8] < -0.026769944:
                        if input[3] < 1.2051187:
                            var29 = 0.01709763
                        else:
                            var29 = -0.14407504
                    else:
                        if input[0] < -0.14237958:
                            var29 = -0.053978413
                        else:
                            var29 = 0.31550926
    else:
        if input[7] < -1.0934299:
            var29 = 0.2733178
        else:
            if input[0] < 0.58233017:
                if input[8] < -0.027758067:
                    if input[1] < 0.8600786:
                        if input[9] < -1.2591478:
                            var29 = -0.24610047
                        else:
                            var29 = -0.001914992
                    else:
                        var29 = 0.059963148
                else:
                    if input[7] < 0.14232793:
                        var29 = -0.072600126
                    else:
                        var29 = 0.2356559
            else:
                if input[7] < 0.15701915:
                    var29 = -0.11651301
                else:
                    var29 = 0.3320366
    if input[1] < -1.6099442:
        if input[10] < -0.66645855:
            var30 = 0.08191386
        else:
            if input[7] < 1.1922786:
                var30 = -0.19910766
            else:
                var30 = -0.017351285
    else:
        if input[4] < 4.247004:
            if input[6] < 0.97067964:
                if input[1] < 2.0000892:
                    if input[0] < -0.7014414:
                        if input[2] < 1.0299541:
                            var30 = -0.008732497
                        else:
                            var30 = 0.1586174
                    else:
                        if input[0] < -0.5772054:
                            var30 = -0.1521803
                        else:
                            var30 = 0.0064145885
                else:
                    if input[1] < 2.4750936:
                        if input[3] < 1.1531873:
                            var30 = 0.24683487
                        else:
                            var30 = 0.042657036
                    else:
                        if input[3] < 0.19150281:
                            var30 = 0.10486072
                        else:
                            var30 = -0.111185975
            else:
                if input[8] < 0.27596393:
                    if input[7] < -1.6440885:
                        if input[9] < -0.8401702:
                            var30 = 0.060819756
                        else:
                            var30 = -0.27477968
                    else:
                        if input[8] < -0.02462842:
                            var30 = 0.0031078055
                        else:
                            var30 = -0.03338272
                else:
                    if input[10] < -0.34624052:
                        if input[9] < 0.6029746:
                            var30 = -0.13841896
                        else:
                            var30 = 0.21317278
                    else:
                        var30 = 0.28541866
        else:
            var30 = 0.16960125
    if input[4] < 2.5279171:
        if input[4] < 0.8088304:
            if input[3] < 0.096733235:
                if input[13] < 1.0:
                    if input[7] < 1.2448369:
                        if input[7] < 1.004733:
                            var31 = -0.0032573754
                        else:
                            var31 = -0.19073261
                    else:
                        if input[5] < 0.64104193:
                            var31 = 0.30979225
                        else:
                            var31 = 0.008464278
                else:
                    if input[8] < -0.031136286:
                        if input[7] < 0.5360101:
                            var31 = 0.12520881
                        else:
                            var31 = -0.054759383
                    else:
                        if input[1] < 0.8600786:
                            var31 = 0.39581388
                        else:
                            var31 = -0.058193713
            else:
                if input[3] < 0.18023762:
                    if input[9] < -0.46774572:
                        if input[5] < 0.64104193:
                            var31 = 0.23931433
                        else:
                            var31 = -0.20435815
                    else:
                        if input[3] < 0.10490314:
                            var31 = 0.026799908
                        else:
                            var31 = -0.32913575
                else:
                    if input[13] < 1.0:
                        if input[8] < -0.030154988:
                            var31 = 0.15648963
                        else:
                            var31 = 0.005399658
                    else:
                        if input[1] < -0.6599355:
                            var31 = 0.15131922
                        else:
                            var31 = -0.1006479
        else:
            if input[8] < -0.030567229:
                if input[14] < 1.0:
                    if input[7] < 1.4206333:
                        if input[7] < -1.6727308:
                            var31 = 0.111626945
                        else:
                            var31 = -0.15824893
                    else:
                        if input[11] < 1.0:
                            var31 = -0.11945123
                        else:
                            var31 = 0.20076776
                else:
                    if input[11] < 1.0:
                        if input[0] < -0.30802754:
                            var31 = -0.22722344
                        else:
                            var31 = -0.0076009883
                    else:
                        if input[7] < -0.99528897:
                            var31 = -0.10369075
                        else:
                            var31 = 0.057023954
            else:
                if input[9] < -0.65395796:
                    if input[9] < -0.9875882:
                        if input[1] < -0.6599355:
                            var31 = -0.12802558
                        else:
                            var31 = 0.063466765
                    else:
                        if input[0] < 0.57197714:
                            var31 = -0.22109286
                        else:
                            var31 = 0.011103995
                else:
                    if input[3] < -0.09819516:
                        if input[0] < 0.5202122:
                            var31 = -0.027219767
                        else:
                            var31 = 0.42688116
                    else:
                        if input[0] < 1.5762178:
                            var31 = 0.033866696
                        else:
                            var31 = -0.1818898
    else:
        if input[0] < 1.224216:
            if input[0] < -0.8774423:
                var31 = 0.1461229
            else:
                if input[0] < -0.58755845:
                    var31 = -0.10137942
                else:
                    if input[0] < -0.10096759:
                        if input[13] < 1.0:
                            var31 = 0.18068415
                        else:
                            var31 = -0.010473721
                    else:
                        if input[12] < 1.0:
                            var31 = 0.05090447
                        else:
                            var31 = -0.10923464
        else:
            var31 = 0.16387989
    if input[1] < -1.0399389:
        if input[8] < -0.018854083:
            if input[9] < -1.0186236:
                if input[7] < 0.2508246:
                    if input[7] < -0.03285734:
                        if input[7] < -0.67884547:
                            var32 = 0.0052335663
                        else:
                            var32 = -0.1916849
                    else:
                        var32 = 0.20258392
                else:
                    if input[0] < -0.82567734:
                        var32 = -0.023628173
                    else:
                        var32 = -0.25708148
            else:
                if input[3] < 0.7186383:
                    if input[8] < -0.023202173:
                        if input[0] < -0.028496623:
                            var32 = 0.06007242
                        else:
                            var32 = -0.18375802
                    else:
                        var32 = 0.29704803
                else:
                    if input[8] < -0.027789427:
                        if input[3] < 0.94295037:
                            var32 = 0.47760054
                        else:
                            var32 = -0.044282217
                    else:
                        if input[1] < -1.5149434:
                            var32 = 0.21131477
                        else:
                            var32 = -0.06361649
        else:
            if input[10] < -0.19680543:
                if input[11] < 1.0:
                    var32 = -0.2941756
                else:
                    if input[0] < 0.31315225:
                        var32 = -0.20193066
                    else:
                        var32 = 0.05710323
            else:
                if input[4] < 0.8088304:
                    var32 = -0.09102027
                else:
                    var32 = 0.067987375
    else:
        if input[7] < -0.5418341:
            if input[7] < -0.61021817:
                if input[1] < 2.6650953:
                    if input[2] < 1.7204164:
                        if input[9] < 0.7115984:
                            var32 = 0.0242281
                        else:
                            var32 = -0.039206684
                    else:
                        if input[1] < 0.19507243:
                            var32 = 0.22944988
                        else:
                            var32 = -0.014567621
                else:
                    if input[0] < 0.58233017:
                        var32 = -0.21092787
                    else:
                        var32 = -0.030588433
            else:
                if input[1] < -0.08993021:
                    if input[12] < 1.0:
                        if input[0] < -0.8981483:
                            var32 = 0.0457804
                        else:
                            var32 = -0.24835907
                    else:
                        var32 = 0.22344048
                else:
                    if input[0] < -0.8981483:
                        var32 = 0.43578684
                    else:
                        if input[10] < -0.42926002:
                            var32 = -0.106362365
                        else:
                            var32 = 0.30949998
        else:
            if input[7] < -0.16876806:
                if input[9] < 1.3633412:
                    if input[9] < 0.25382668:
                        if input[3] < 0.36641937:
                            var32 = 0.036530197
                        else:
                            var32 = -0.15780148
                    else:
                        if input[8] < -0.019266702:
                            var32 = -0.01299165
                        else:
                            var32 = 0.24857877
                else:
                    if input[8] < -0.022054886:
                        if input[3] < -0.13747577:
                            var32 = -0.06355965
                        else:
                            var32 = -0.37362233
                    else:
                        if input[3] < 0.8783539:
                            var32 = 0.29108268
                        else:
                            var32 = -0.16081512
            else:
                if input[7] < -0.12399654:
                    if input[1] < -0.08993021:
                        if input[3] < 0.33524093:
                            var32 = 0.7192888
                        else:
                            var32 = -0.025808077
                    else:
                        if input[0] < 0.23032829:
                            var32 = -0.18158695
                        else:
                            var32 = 0.16635539
                else:
                    if input[1] < 0.10007155:
                        if input[0] < 1.5140998:
                            var32 = -0.013443639
                        else:
                            var32 = -0.19324884
                    else:
                        if input[1] < 0.19507243:
                            var32 = 0.12382447
                        else:
                            var32 = 0.0024466186
    if input[1] < 0.3850742:
        if input[8] < 0.1384076:
            if input[0] < 0.2510343:
                if input[0] < 0.1889163:
                    if input[3] < 0.91767496:
                        if input[11] < 1.0:
                            var33 = 0.012869784
                        else:
                            var33 = -0.07870385
                    else:
                        if input[0] < -0.3597925:
                            var33 = -0.04755203
                        else:
                            var33 = 0.17643926
                else:
                    if input[3] < -0.43135172:
                        if input[0] < 0.2096223:
                            var33 = 0.10838012
                        else:
                            var33 = -0.13483483
                    else:
                        var33 = -0.34591368
            else:
                if input[0] < 0.4477412:
                    if input[7] < 0.34157342:
                        if input[9] < -0.49102226:
                            var33 = 0.35757387
                        else:
                            var33 = 0.06780734
                    else:
                        if input[3] < 0.21962981:
                            var33 = 0.07660165
                        else:
                            var33 = -0.24261297
                else:
                    if input[7] < 0.35555807:
                        if input[7] < -0.44317603:
                            var33 = -0.0007963194
                        else:
                            var33 = -0.12071133
                    else:
                        if input[7] < 0.70739216:
                            var33 = 0.2171772
                        else:
                            var33 = -0.0005789263
        else:
            if input[0] < -1.1052083:
                var33 = 0.09692424
            else:
                if input[3] < 0.4278236:
                    var33 = -0.01044408
                else:
                    var33 = -0.28306332
    else:
        if input[0] < 0.17856331:
            if input[0] < 0.095739335:
                if input[3] < 1.4619124:
                    if input[3] < 1.2132308:
                        if input[3] < 1.1601992:
                            var33 = 0.027072037
                        else:
                            var33 = -0.2224393
                    else:
                        if input[7] < 1.1584231:
                            var33 = 0.19752233
                        else:
                            var33 = -0.10818325
                else:
                    if input[3] < 1.8128457:
                        if input[1] < 1.1450812:
                            var33 = -0.2872662
                        else:
                            var33 = -0.007830922
                    else:
                        var33 = 0.08287398
            else:
                if input[7] < -0.15285553:
                    if input[9] < 0.16072056:
                        var33 = -0.24389392
                    else:
                        var33 = 0.18525213
                else:
                    if input[3] < 0.96368194:
                        if input[5] < 0.64104193:
                            var33 = 0.2716444
                        else:
                            var33 = 0.027357288
                    else:
                        var33 = 0.48981255
        else:
            if input[0] < 0.5512712:
                if input[3] < 1.4018602:
                    if input[3] < 1.1227999:
                        if input[3] < 1.0172395:
                            var33 = -0.1225319
                        else:
                            var33 = 0.37837595
                    else:
                        var33 = -0.29878518
                else:
                    if input[5] < 0.64104193:
                        var33 = 0.011198914
                    else:
                        var33 = 0.19555162
            else:
                if input[11] < 1.0:
                    if input[7] < 1.5132883:
                        if input[7] < -0.42702612:
                            var33 = 0.014883761
                        else:
                            var33 = 0.14178032
                    else:
                        if input[10] < -0.42926002:
                            var33 = 0.022274986
                        else:
                            var33 = -0.2942409
                else:
                    if input[7] < 0.036785312:
                        if input[4] < 0.8088304:
                            var33 = 0.12468757
                        else:
                            var33 = -0.12559809
                    else:
                        if input[7] < 1.0982982:
                            var33 = -0.2570184
                        else:
                            var33 = 0.0075750533
    if input[0] < -2.306156:
        if input[7] < -0.40280506:
            var34 = -0.1361777
        else:
            if input[4] < 0.8088304:
                if input[8] < -0.0280959:
                    var34 = 0.2858071
                else:
                    var34 = 0.07189144
            else:
                var34 = -0.013595161
    else:
        if input[1] < 3.4251022:
            if input[0] < -1.923095:
                if input[7] < -1.0814095:
                    var34 = 0.15451616
                else:
                    if input[1] < 1.335083:
                        if input[10] < -0.761338:
                            var34 = 0.15365873
                        else:
                            var34 = -0.19221315
                    else:
                        if input[7] < 0.7202354:
                            var34 = 0.1461627
                        else:
                            var34 = -0.017386468
            else:
                if input[0] < -1.747094:
                    if input[9] < 0.59521574:
                        if input[7] < 1.4377079:
                            var34 = 0.02592188
                        else:
                            var34 = -0.25184485
                    else:
                        if input[11] < 1.0:
                            var34 = 0.12206889
                        else:
                            var34 = 0.45763612
                else:
                    if input[0] < -1.4675632:
                        if input[2] < -0.005739468:
                            var34 = 0.061596543
                        else:
                            var34 = -0.18623663
                    else:
                        if input[0] < -1.1983852:
                            var34 = 0.05018628
                        else:
                            var34 = -0.0020561812
        else:
            var34 = -0.18390913
    if input[9] < -1.142765:
        if input[3] < 0.42386827:
            if input[6] < 0.97067964:
                if input[0] < 0.37527025:
                    if input[3] < 0.22722906:
                        if input[13] < 1.0:
                            var35 = -0.30553466
                        else:
                            var35 = -0.11801765
                    else:
                        var35 = -0.09663042
                else:
                    if input[3] < 0.27665573:
                        if input[5] < 0.64104193:
                            var35 = -0.16899902
                        else:
                            var35 = 0.20439829
                    else:
                        var35 = -0.24087769
            else:
                if input[8] < -0.024886819:
                    if input[7] < -0.12399654:
                        if input[0] < 0.94468504:
                            var35 = 0.22774464
                        else:
                            var35 = -0.040913664
                    else:
                        if input[0] < 0.106092334:
                            var35 = 0.0027932832
                        else:
                            var35 = -0.22875893
                else:
                    if input[0] < -0.7014414:
                        var35 = -0.035834357
                    else:
                        var35 = -0.23237918
        else:
            if input[3] < 1.2936667:
                if input[3] < 0.47035775:
                    if input[0] < 0.1992693:
                        if input[1] < 0.10007155:
                            var35 = -0.09321975
                        else:
                            var35 = 0.14421737
                    else:
                        var35 = 0.38962096
                else:
                    if input[0] < 1.265628:
                        if input[3] < 1.1531873:
                            var35 = 0.029348925
                        else:
                            var35 = 0.22759025
                    else:
                        if input[5] < 0.64104193:
                            var35 = 0.015016963
                        else:
                            var35 = -0.2637698
            else:
                if input[0] < 0.5098592:
                    if input[4] < 0.8088304:
                        var35 = -0.28541043
                    else:
                        var35 = -0.02985409
                else:
                    var35 = 0.020927925
    else:
        if input[9] < -1.1117297:
            if input[3] < 0.5495229:
                if input[3] < 0.049261205:
                    var35 = 0.07344593
                else:
                    var35 = 0.3150467
            else:
                if input[14] < 1.0:
                    var35 = -0.16082694
                else:
                    var35 = 0.10349877
        else:
            if input[7] < -1.7251737:
                if input[11] < 1.0:
                    var35 = 0.2608464
                else:
                    var35 = -0.06392015
            else:
                if input[7] < -1.5337794:
                    if input[11] < 1.0:
                        if input[0] < 0.57197714:
                            var35 = 0.10608398
                        else:
                            var35 = -0.15231967
                    else:
                        if input[8] < 0.116589285:
                            var35 = -0.24755543
                        else:
                            var35 = -0.020804599
                else:
                    if input[7] < -1.4827619:
                        if input[12] < 1.0:
                            var35 = 0.23601617
                        else:
                            var35 = -0.058598015
                    else:
                        if input[7] < -1.0354191:
                            var35 = -0.037733447
                        else:
                            var35 = 0.0054525696
    if input[6] < 0.97067964:
        if input[1] < 1.4300839:
            if input[7] < -0.86889863:
                if input[4] < 0.8088304:
                    if input[0] < 0.5409182:
                        if input[1] < 0.67007685:
                            var36 = -0.07544422
                        else:
                            var36 = 0.08230905
                    else:
                        if input[7] < -1.5516653:
                            var36 = -0.19379766
                        else:
                            var36 = 0.1499335
                else:
                    if input[3] < 1.0442176:
                        if input[0] < -0.9706193:
                            var36 = 0.0380503
                        else:
                            var36 = -0.18326381
                    else:
                        if input[1] < 0.3850742:
                            var36 = -0.038695894
                        else:
                            var36 = 0.24496962
            else:
                if input[7] < -0.811972:
                    if input[12] < 1.0:
                        if input[1] < 0.10007155:
                            var36 = 0.41959757
                        else:
                            var36 = 0.014086852
                    else:
                        if input[5] < 0.64104193:
                            var36 = -0.18157274
                        else:
                            var36 = 0.09819863
                else:
                    if input[8] < -0.022478675:
                        if input[8] < -0.02615307:
                            var36 = 0.014593483
                        else:
                            var36 = -0.059297793
                    else:
                        if input[3] < 0.87363386:
                            var36 = 0.124805346
                        else:
                            var36 = 0.009848734
        else:
            if input[7] < -0.75954294:
                if input[3] < 0.60240114:
                    var36 = 0.2558836
                else:
                    if input[14] < 1.0:
                        var36 = -0.09157243
                    else:
                        var36 = 0.18000962
            else:
                if input[2] < -0.005739468:
                    if input[2] < -0.35097063:
                        if input[0] < -1.2087382:
                            var36 = -0.11834314
                        else:
                            var36 = 0.15953211
                    else:
                        var36 = -0.28882167
                else:
                    if input[8] < -0.028055904:
                        if input[9] < 2.7444153:
                            var36 = 0.25394014
                        else:
                            var36 = 0.029037599
                    else:
                        if input[7] < 0.26626915:
                            var36 = -0.11987075
                        else:
                            var36 = 0.08472863
    else:
        if input[8] < 0.27596393:
            if input[7] < -1.6440885:
                if input[9] < -0.8401702:
                    var36 = 0.007693537
                else:
                    var36 = -0.2421487
            else:
                if input[7] < -1.133428:
                    if input[3] < 0.94295037:
                        if input[0] < -1.3433272:
                            var36 = -0.14526384
                        else:
                            var36 = 0.09493837
                    else:
                        if input[11] < 1.0:
                            var36 = -0.21928251
                        else:
                            var36 = 0.06474772
                else:
                    if input[7] < -1.0354191:
                        if input[10] < 1.1481103:
                            var36 = -0.24959289
                        else:
                            var36 = 0.11650946
                    else:
                        if input[7] < -0.9472609:
                            var36 = 0.16237225
                        else:
                            var36 = -0.018990811
        else:
            if input[0] < 0.095739335:
                var36 = -0.008819253
            else:
                if input[14] < 1.0:
                    var36 = 0.04718825
                else:
                    var36 = 0.26938587
    if input[4] < 2.5279171:
        if input[1] < -0.75493634:
            if input[9] < -0.72378755:
                if input[7] < -1.4387897:
                    if input[6] < 0.97067964:
                        var37 = 0.23064944
                    else:
                        var37 = -0.047344837
                else:
                    if input[1] < -1.3249416:
                        if input[1] < -1.4199425:
                            var37 = -0.09915918
                        else:
                            var37 = 0.14675905
                    else:
                        if input[7] < 0.16707173:
                            var37 = -0.09756963
                        else:
                            var37 = -0.22973391
            else:
                if input[7] < -0.78532803:
                    if input[9] < 0.59521574:
                        if input[0] < 0.29244626:
                            var37 = -0.22501458
                        else:
                            var37 = -0.027364325
                    else:
                        var37 = 0.18995228
                else:
                    if input[7] < -0.4824063:
                        if input[3] < 0.8141936:
                            var37 = 0.47035655
                        else:
                            var37 = -0.004040749
                    else:
                        if input[3] < 0.7937028:
                            var37 = -0.07571428
                        else:
                            var37 = 0.1360112
        else:
            if input[3] < 0.68110025:
                if input[3] < 0.6426471:
                    if input[1] < 2.3800926:
                        if input[7] < 0.110421926:
                            var37 = -0.012546136
                        else:
                            var37 = 0.026610734
                    else:
                        if input[9] < 2.3952672:
                            var37 = -0.19909234
                        else:
                            var37 = 0.01451853
                else:
                    if input[9] < 0.20727362:
                        if input[0] < -0.3701455:
                            var37 = 0.04234117
                        else:
                            var37 = 0.3400506
                    else:
                        if input[3] < 0.665922:
                            var37 = -0.11650171
                        else:
                            var37 = 0.10768183
            else:
                if input[7] < 1.6285735:
                    if input[7] < 1.5864803:
                        if input[0] < -0.26661554:
                            var37 = -0.039090443
                        else:
                            var37 = 0.0073018433
                    else:
                        if input[1] < -0.27993196:
                            var37 = -0.13139047
                        else:
                            var37 = 0.35506856
                else:
                    if input[0] < -0.7325004:
                        var37 = 0.11073101
                    else:
                        if input[0] < 0.8722141:
                            var37 = -0.31196696
                        else:
                            var37 = -0.0024315198
    else:
        if input[8] < -0.03078074:
            if input[7] < 1.1829834:
                if input[0] < -0.6910884:
                    var37 = -0.14918096
                else:
                    if input[0] < -0.46332246:
                        var37 = 0.17481503
                    else:
                        if input[7] < -0.33451837:
                            var37 = 0.05100512
                        else:
                            var37 = -0.0878228
            else:
                var37 = 0.13790052
        else:
            if input[12] < 1.0:
                var37 = 0.19460382
            else:
                if input[1] < -0.37493283:
                    var37 = -0.044116907
                else:
                    var37 = 0.12043705
    if input[0] < -0.12167359:
        if input[0] < -0.16308558:
            if input[9] < 1.6969715:
                if input[9] < 1.6271418:
                    if input[7] < 1.2721516:
                        if input[1] < 1.7150865:
                            var38 = -0.0031404572
                        else:
                            var38 = -0.09763311
                    else:
                        if input[7] < 1.4636902:
                            var38 = 0.15085053
                        else:
                            var38 = -0.016076306
                else:
                    if input[3] < 0.7086714:
                        var38 = -0.27447924
                    else:
                        var38 = -0.057514478
            else:
                if input[0] < -1.2708561:
                    if input[1] < 1.335083:
                        if input[3] < -0.63909185:
                            var38 = 0.011807495
                        else:
                            var38 = 0.1875931
                    else:
                        if input[6] < 0.97067964:
                            var38 = 0.014582658
                        else:
                            var38 = -0.27082735
                else:
                    if input[8] < 0.0037976594:
                        if input[1] < 1.8100873:
                            var38 = 0.09398406
                        else:
                            var38 = 0.28655657
                    else:
                        var38 = -0.14195015
        else:
            if input[3] < 0.5229495:
                if input[7] < -0.704771:
                    var38 = 0.12915617
                else:
                    var38 = -0.22835462
            else:
                if input[7] < 0.93511486:
                    if input[8] < -0.02462842:
                        var38 = 0.5671942
                    else:
                        if input[5] < 0.64104193:
                            var38 = 0.29913574
                        else:
                            var38 = -0.068321764
                else:
                    var38 = 0.02451527
    else:
        if input[0] < -0.06990861:
            if input[3] < 1.055667:
                if input[10] < -0.761338:
                    var38 = -0.045642827
                else:
                    if input[8] < -0.020045163:
                        if input[1] < -0.27993196:
                            var38 = -0.11937434
                        else:
                            var38 = -0.35674426
                    else:
                        if input[1] < -0.18493108:
                            var38 = -0.20014895
                        else:
                            var38 = 0.00715982
            else:
                if input[11] < 1.0:
                    var38 = -0.15986696
                else:
                    var38 = 0.2516529
        else:
            if input[0] < -0.049202614:
                if input[8] < -0.024557525:
                    if input[10] < -0.4956756:
                        if input[9] < 0.4943508:
                            var38 = 0.21203478
                        else:
                            var38 = -0.016156835
                    else:
                        var38 = 0.43917444
                else:
                    if input[7] < -1.4827619:
                        var38 = 0.13653201
                    else:
                        var38 = -0.19113795
            else:
                if input[3] < 1.6430904:
                    if input[0] < 0.37527025:
                        if input[9] < 0.0055436934:
                            var38 = 0.01144916
                        else:
                            var38 = -0.08524427
                    else:
                        if input[0] < 0.4477412:
                            var38 = 0.1524913
                        else:
                            var38 = -0.0066161356
                else:
                    if input[0] < 0.33385825:
                        var38 = 0.31511015
                    else:
                        if input[13] < 1.0:
                            var38 = -0.13994323
                        else:
                            var38 = 0.15918113
    if input[0] < -2.0680368:
        if input[9] < 2.0538783:
            if input[10] < -0.761338:
                var39 = 0.25327823
            else:
                if input[9] < 0.036579065:
                    if input[7] < 1.0826854:
                        if input[6] < 0.97067964:
                            var39 = 0.23459563
                        else:
                            var39 = 0.020888526
                    else:
                        var39 = -0.07713196
                else:
                    if input[9] < 0.40900353:
                        var39 = -0.20384966
                    else:
                        if input[2] < 1.0299541:
                            var39 = 0.17991138
                        else:
                            var39 = -0.023515722
        else:
            var39 = -0.14236994
    else:
        if input[0] < -1.923095:
            if input[1] < -0.46993372:
                var39 = 0.086510025
            else:
                if input[7] < 0.36911884:
                    var39 = 0.034111403
                else:
                    var39 = -0.28555366
        else:
            if input[1] < 0.7650777:
                if input[0] < -1.747094:
                    if input[9] < 0.59521574:
                        if input[8] < -0.0186616:
                            var39 = -0.098014735
                        else:
                            var39 = 0.24230596
                    else:
                        var39 = 0.28701448
                else:
                    if input[9] < 1.8366307:
                        if input[0] < -1.4675632:
                            var39 = -0.078618474
                        else:
                            var39 = -0.0037587353
                    else:
                        if input[0] < -0.24590954:
                            var39 = -0.046792563
                        else:
                            var39 = -0.24311501
            else:
                if input[9] < 0.54090387:
                    if input[1] < 1.1450812:
                        if input[8] < -0.015660465:
                            var39 = 0.1279578
                        else:
                            var39 = -0.050461546
                    else:
                        if input[7] < 0.5360101:
                            var39 = 0.041190434
                        else:
                            var39 = -0.07578294
                else:
                    if input[3] < 1.2936667:
                        if input[3] < 0.68110025:
                            var39 = 0.015878873
                        else:
                            var39 = -0.08524382
                    else:
                        if input[9] < 1.2081643:
                            var39 = 0.29031312
                        else:
                            var39 = 0.011487432
    if input[9] < -1.142765:
        if input[3] < 0.42386827:
            if input[6] < 0.97067964:
                if input[0] < 0.37527025:
                    if input[9] < -1.2203535:
                        var40 = -0.2632313
                    else:
                        if input[9] < -1.197077:
                            var40 = 0.046465002
                        else:
                            var40 = -0.1669088
                else:
                    if input[0] < 1.0792739:
                        if input[5] < 0.64104193:
                            var40 = -0.15572865
                        else:
                            var40 = 0.16459946
                    else:
                        if input[1] < 0.2900733:
                            var40 = -0.22712576
                        else:
                            var40 = 0.0034226484
            else:
                if input[0] < -1.3433272:
                    if input[5] < 0.64104193:
                        var40 = 0.26633152
                    else:
                        var40 = -0.0015669994
                else:
                    if input[0] < -0.7325004:
                        var40 = -0.25755543
                    else:
                        if input[0] < 0.2613873:
                            var40 = 0.093795225
                        else:
                            var40 = -0.07964912
        else:
            if input[3] < 1.2936667:
                if input[8] < -0.0287114:
                    if input[8] < -0.029305013:
                        if input[1] < 0.3850742:
                            var40 = -0.07947895
                        else:
                            var40 = 0.23458034
                    else:
                        var40 = -0.31485304
                else:
                    if input[6] < 0.97067964:
                        if input[4] < 0.8088304:
                            var40 = 0.15132323
                        else:
                            var40 = -0.06741825
                    else:
                        if input[1] < -0.37493283:
                            var40 = -0.22148795
                        else:
                            var40 = 0.045791585
            else:
                if input[1] < -0.27993196:
                    var40 = 0.027464936
                else:
                    var40 = -0.21458788
    else:
        if input[8] < 0.05595688:
            if input[8] < 0.044666257:
                if input[9] < -0.94103515:
                    if input[8] < -0.031854544:
                        if input[9] < -1.0651766:
                            var40 = -0.049487133
                        else:
                            var40 = 0.29733327
                    else:
                        if input[0] < -0.8774423:
                            var40 = 0.15344644
                        else:
                            var40 = -0.059654683
                else:
                    if input[7] < -1.5337794:
                        if input[7] < -1.6840237:
                            var40 = 0.15812835
                        else:
                            var40 = -0.18432172
                    else:
                        if input[7] < -1.4827619:
                            var40 = 0.12753975
                        else:
                            var40 = -0.0016068903
            else:
                var40 = -0.25803506
        else:
            if input[2] < -0.005739468:
                if input[2] < -0.35097063:
                    if input[3] < 0.32922727:
                        var40 = -0.11941836
                    else:
                        if input[3] < 0.9028802:
                            var40 = 0.27250904
                        else:
                            var40 = -0.057005674
                else:
                    if input[1] < 0.3850742:
                        var40 = -0.26207042
                    else:
                        var40 = -0.07010147
            else:
                if input[12] < 1.0:
                    if input[7] < -1.6440885:
                        if input[9] < 1.0685052:
                            var40 = -0.22845604
                        else:
                            var40 = 0.02036201
                    else:
                        if input[2] < 1.0299541:
                            var40 = 0.23596092
                        else:
                            var40 = -0.06404677
                else:
                    if input[1] < 0.3850742:
                        if input[0] < -0.10096759:
                            var40 = 0.2648167
                        else:
                            var40 = -0.08282751
                    else:
                        var40 = 0.28650424
    if input[4] < 2.5279171:
        if input[10] < -0.19680543:
            if input[0] < -0.54614645:
                if input[0] < -0.7014414:
                    if input[9] < -0.08756243:
                        if input[8] < -0.0186616:
                            var41 = -0.1293849
                        else:
                            var41 = 0.12524386
                    else:
                        if input[9] < 0.9676402:
                            var41 = 0.06926226
                        else:
                            var41 = -0.034160253
                else:
                    if input[3] < 0.7339476:
                        if input[1] < 0.005070672:
                            var41 = 0.1290362
                        else:
                            var41 = -0.13502215
                    else:
                        if input[9] < 1.1383348:
                            var41 = -0.36297077
                        else:
                            var41 = 0.11662612
            else:
                if input[7] < -1.133428:
                    if input[9] < -0.5142988:
                        if input[9] < -0.6772345:
                            var41 = 0.031721972
                        else:
                            var41 = -0.2271825
                    else:
                        if input[8] < 0.0009902425:
                            var41 = 0.1654759
                        else:
                            var41 = 0.022192726
                else:
                    if input[7] < -1.0203258:
                        if input[0] < -0.24590954:
                            var41 = -0.0291533
                        else:
                            var41 = -0.2789739
                    else:
                        if input[8] < -0.011607501:
                            var41 = 0.015100125
                        else:
                            var41 = -0.11452574
        else:
            if input[0] < -1.2605032:
                if input[1] < 1.7150865:
                    if input[1] < -0.27993196:
                        if input[7] < 0.8663735:
                            var41 = -0.14613813
                        else:
                            var41 = 0.14539114
                    else:
                        if input[0] < -1.674623:
                            var41 = 0.013306423
                        else:
                            var41 = 0.23150724
                else:
                    if input[9] < -1.0419002:
                        var41 = -0.24449168
                    else:
                        var41 = -0.041290123
            else:
                if input[9] < 0.25382668:
                    if input[9] < 0.16072056:
                        if input[3] < 1.418603:
                            var41 = -0.034604806
                        else:
                            var41 = 0.08901864
                    else:
                        var41 = 0.32645702
                else:
                    if input[6] < 0.97067964:
                        if input[8] < -0.029258993:
                            var41 = 0.04512506
                        else:
                            var41 = -0.13171679
                    else:
                        var41 = -0.2312233
    else:
        if input[8] < -0.028330084:
            if input[7] < -0.4824063:
                if input[6] < 0.97067964:
                    var41 = 0.05468859
                else:
                    var41 = -0.17274073
            else:
                if input[12] < 1.0:
                    if input[14] < 1.0:
                        if input[0] < -0.4219105:
                            var41 = 0.11517576
                        else:
                            var41 = -0.053371727
                    else:
                        if input[9] < -0.6461991:
                            var41 = 0.050742038
                        else:
                            var41 = 0.17025946
                else:
                    var41 = -0.042119034
        else:
            var41 = 0.14134824
    if input[10] < 2.8915195:
        if input[9] < -1.142765:
            if input[4] < 0.8088304:
                if input[8] < 0.07376749:
                    if input[7] < -1.4665563:
                        var42 = 0.22889082
                    else:
                        if input[1] < 1.6200856:
                            var42 = -0.00009901293
                        else:
                            var42 = -0.21291034
                else:
                    var42 = -0.22944225
            else:
                if input[8] < -0.025518332:
                    if input[7] < -1.2486452:
                        var42 = -0.042115465
                    else:
                        var42 = -0.27375436
                else:
                    if input[8] < -0.020045163:
                        if input[0] < -0.3701455:
                            var42 = 0.036595345
                        else:
                            var42 = 0.3482553
                    else:
                        if input[6] < 0.97067964:
                            var42 = -0.2137914
                        else:
                            var42 = -0.030441504
        else:
            if input[9] < -0.9875882:
                if input[8] < -0.013150221:
                    if input[0] < 1.4830408:
                        if input[1] < -0.8499372:
                            var42 = -0.044691086
                        else:
                            var42 = 0.11731299
                    else:
                        var42 = -0.16148138
                else:
                    if input[3] < 0.8783539:
                        if input[3] < 0.5189618:
                            var42 = -0.115937
                        else:
                            var42 = 0.14343576
                    else:
                        var42 = -0.18087941
            else:
                if input[10] < 0.4009349:
                    if input[10] < 0.10206473:
                        if input[8] < 0.05595688:
                            var42 = -0.004593459
                        else:
                            var42 = 0.06712129
                    else:
                        if input[7] < 1.3641307:
                            var42 = 0.1264926
                        else:
                            var42 = -0.20712173
                else:
                    if input[0] < -1.6021521:
                        if input[0] < -2.140508:
                            var42 = 0.04535565
                        else:
                            var42 = 0.26407835
                    else:
                        if input[0] < -0.6910884:
                            var42 = -0.23975398
                        else:
                            var42 = -0.023812527
    else:
        if input[7] < -1.1905584:
            var42 = 0.19906601
        else:
            if input[7] < 0.060869616:
                if input[8] < -0.01967467:
                    var42 = -0.13219604
                else:
                    var42 = 0.07396994
            else:
                if input[0] < 0.57197714:
                    if input[8] < -0.027758067:
                        if input[1] < 0.67007685:
                            var42 = -0.18650109
                        else:
                            var42 = 0.026444755
                    else:
                        var42 = 0.17738584
                else:
                    var42 = 0.21140075
    if input[4] < 2.5279171:
        if input[1] < -1.6099442:
            if input[11] < 1.0:
                if input[5] < 0.64104193:
                    var43 = 0.14504814
                else:
                    var43 = -0.09942492
            else:
                var43 = -0.20381941
        else:
            if input[10] < -0.19680543:
                if input[9] < -0.94103515:
                    var43 = 0.2193226
                else:
                    if input[1] < -1.2299408:
                        if input[1] < -1.5149434:
                            var43 = 0.074479215
                        else:
                            var43 = -0.14794484
                    else:
                        if input[9] < -0.0022151496:
                            var43 = 0.029290223
                        else:
                            var43 = -0.003662535
            else:
                if input[9] < 0.20727362:
                    if input[9] < 0.16072056:
                        if input[2] < -0.005739468:
                            var43 = -0.004532859
                        else:
                            var43 = -0.124472
                    else:
                        var43 = 0.30625048
                else:
                    if input[8] < -0.015036962:
                        if input[9] < 0.3314151:
                            var43 = -0.28107187
                        else:
                            var43 = -0.0779247
                    else:
                        var43 = 0.043138806
    else:
        if input[3] < -0.63909185:
            if input[7] < 1.1123637:
                if input[7] < 0.31350702:
                    if input[7] < -0.4824063:
                        if input[6] < 0.97067964:
                            var43 = 0.048286688
                        else:
                            var43 = -0.13705854
                    else:
                        if input[7] < -0.33451837:
                            var43 = 0.17104852
                        else:
                            var43 = -0.0040326663
                else:
                    var43 = -0.11522286
            else:
                var43 = 0.14184317
        else:
            if input[0] < 0.31315225:
                if input[0] < -0.10096759:
                    var43 = 0.13027017
                else:
                    var43 = -0.084502846
            else:
                var43 = 0.19957525
    if input[4] < 2.5279171:
        if input[0] < -2.4407449:
            if input[14] < 1.0:
                var44 = 0.14905208
            else:
                var44 = -0.026532913
        else:
            if input[1] < 3.1400995:
                if input[1] < 3.0450988:
                    if input[9] < 2.5349264:
                        if input[9] < 1.4331708:
                            var44 = -0.0044063753
                        else:
                            var44 = 0.026521968
                    else:
                        if input[0] < -0.16308558:
                            var44 = 0.015433639
                        else:
                            var44 = -0.12975217
                else:
                    var44 = 0.14481641
            else:
                if input[8] < -0.023402806:
                    var44 = -0.15841724
                else:
                    var44 = 0.0033352936
    else:
        if input[3] < 0.45116842:
            if input[9] < -0.7082699:
                if input[9] < -0.95655286:
                    var44 = 0.039756037
                else:
                    var44 = 0.14597328
            else:
                if input[14] < 1.0:
                    if input[2] < 1.0299541:
                        var44 = -0.14034942
                    else:
                        var44 = 0.04545297
                else:
                    if input[1] < 0.19507243:
                        if input[11] < 1.0:
                            var44 = -0.10237495
                        else:
                            var44 = 0.06737241
                    else:
                        var44 = 0.10764667
        else:
            if input[1] < -0.18493108:
                var44 = 0.022050645
            else:
                var44 = 0.1590546
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[9] < 0.9676402:
        if input[9] < 0.928846:
            if input[9] < 0.8590164:
                if input[9] < 0.8202222:
                    if input[8] < -0.030154988:
                        if input[3] < 0.42386827:
                            var46 = 0.010924274
                        else:
                            var46 = 0.27256376
                    else:
                        if input[8] < -0.029904474:
                            var46 = -0.18054602
                        else:
                            var46 = -0.002917875
                else:
                    if input[7] < -0.32233608:
                        if input[0] < -0.9706193:
                            var46 = 0.47060257
                        else:
                            var46 = 0.10320277
                    else:
                        if input[6] < 0.97067964:
                            var46 = -0.2064644
                        else:
                            var46 = 0.2062516
            else:
                if input[0] < -0.3701455:
                    if input[7] < 0.5579357:
                        if input[8] < -0.021582942:
                            var46 = 0.2796058
                        else:
                            var46 = -0.05176245
                    else:
                        var46 = -0.092544675
                else:
                    if input[0] < 1.317393:
                        if input[12] < 1.0:
                            var46 = -0.2744058
                        else:
                            var46 = -0.05375227
                    else:
                        var46 = 0.036694948
        else:
            if input[3] < 0.5095043:
                if input[8] < -0.030248145:
                    var46 = 0.04430537
                else:
                    var46 = -0.08883156
            else:
                if input[6] < 0.97067964:
                    var46 = 0.33516005
                else:
                    var46 = -0.0018032229
    else:
        if input[9] < 0.9986756:
            if input[0] < -0.99132526:
                var46 = -0.010613179
            else:
                var46 = -0.26898625
        else:
            if input[7] < 1.7218465:
                if input[7] < 1.6563303:
                    if input[0] < -1.2708561:
                        if input[0] < -1.747094:
                            var46 = 0.043246683
                        else:
                            var46 = -0.19775443
                    else:
                        if input[1] < -0.18493108:
                            var46 = -0.16466731
                        else:
                            var46 = 0.024211412
                else:
                    var46 = -0.32846272
            else:
                var46 = 0.301347
    if input[6] < 0.97067964:
        if input[1] < 2.0000892:
            if input[7] < -0.73191154:
                if input[0] < 1.5762178:
                    if input[0] < -1.747094:
                        if input[7] < -1.3495861:
                            var47 = -0.10279073
                        else:
                            var47 = 0.24332319
                    else:
                        if input[0] < -1.2087382:
                            var47 = -0.14469455
                        else:
                            var47 = -0.02580414
                else:
                    if input[8] < -0.0066573843:
                        if input[9] < 0.26934436:
                            var47 = 0.12695359
                        else:
                            var47 = -0.16420513
                    else:
                        if input[10] < -0.5500156:
                            var47 = 0.34692556
                        else:
                            var47 = -0.0131846415
            else:
                if input[7] < -0.67884547:
                    if input[3] < 0.9687012:
                        if input[1] < 0.005070672:
                            var47 = -0.085187644
                        else:
                            var47 = 0.21033216
                    else:
                        var47 = 0.3320948
                else:
                    if input[8] < -0.016129123:
                        if input[8] < -0.024266273:
                            var47 = 0.0016723513
                        else:
                            var47 = 0.054370057
                    else:
                        if input[10] < -0.19680543:
                            var47 = -0.24825467
                        else:
                            var47 = -0.022390522
        else:
            if input[7] < 0.36911884:
                if input[1] < 2.855097:
                    var47 = 0.24163562
                else:
                    var47 = 0.035153583
            else:
                if input[1] < 2.4750936:
                    if input[7] < 0.9883554:
                        var47 = -0.058268614
                    else:
                        var47 = 0.18958974
                else:
                    var47 = -0.10739684
    else:
        if input[3] < 1.4322927:
            if input[3] < 1.2460401:
                if input[7] < -0.44317603:
                    if input[9] < 0.7659103:
                        if input[3] < 0.6612899:
                            var47 = 0.0017140746
                        else:
                            var47 = 0.11868072
                    else:
                        if input[9] < 1.2004055:
                            var47 = -0.13820958
                        else:
                            var47 = 0.023052108
                else:
                    if input[8] < -0.0227347:
                        if input[3] < 1.1227999:
                            var47 = -0.010675124
                        else:
                            var47 = -0.17991675
                    else:
                        if input[9] < 1.3400646:
                            var47 = -0.28963965
                        else:
                            var47 = 0.017761124
            else:
                if input[8] < -0.020045163:
                    if input[9] < 0.69608074:
                        if input[9] < -0.9099998:
                            var47 = 0.041571796
                        else:
                            var47 = 0.4276025
                    else:
                        var47 = -0.041325126
                else:
                    if input[3] < 1.3683784:
                        var47 = -0.27259842
                    else:
                        var47 = 0.041563366
        else:
            if input[3] < 1.6893907:
                if input[8] < -0.025742803:
                    if input[0] < 0.23032829:
                        var47 = -0.070416965
                    else:
                        var47 = 0.17838988
                else:
                    if input[0] < -1.1052083:
                        var47 = -0.02880572
                    else:
                        if input[9] < -0.95655286:
                            var47 = -0.08275126
                        else:
                            var47 = -0.2907563
            else:
                if input[8] < -0.015036962:
                    if input[7] < 0.5204659:
                        var47 = -0.20413813
                    else:
                        if input[9] < -0.041009367:
                            var47 = 0.10293806
                        else:
                            var47 = -0.08549002
                else:
                    if input[0] < 0.33385825:
                        if input[7] < -0.99528897:
                            var47 = 0.30432975
                        else:
                            var47 = 0.054574005
                    else:
                        var47 = -0.046168145
    if input[4] < 2.5279171:
        if input[1] < -1.6099442:
            if input[11] < 1.0:
                if input[10] < -0.42926002:
                    var48 = 0.13946931
                else:
                    var48 = -0.11018739
            else:
                var48 = -0.18809873
        else:
            if input[0] < 1.4623349:
                if input[0] < 1.4209229:
                    if input[0] < 1.3691579:
                        if input[7] < 1.7370887:
                            var48 = 0.0011751787
                        else:
                            var48 = -0.13018925
                    else:
                        if input[7] < -0.811972:
                            var48 = 0.12525083
                        else:
                            var48 = -0.23611046
                else:
                    if input[1] < -0.5649346:
                        var48 = -0.19703206
                    else:
                        if input[7] < 0.35555807:
                            var48 = 0.010514997
                        else:
                            var48 = 0.35359114
            else:
                if input[7] < -1.2378846:
                    if input[4] < 0.8088304:
                        if input[7] < -1.3645813:
                            var48 = 0.04891419
                        else:
                            var48 = 0.339379
                    else:
                        var48 = -0.081412494
                else:
                    if input[9] < 0.3314151:
                        if input[7] < 1.5132883:
                            var48 = -0.1678612
                        else:
                            var48 = 0.14316483
                    else:
                        if input[9] < 0.9676402:
                            var48 = 0.18320143
                        else:
                            var48 = -0.10021581
    else:
        if input[8] < -0.028330084:
            if input[7] < 0.608219:
                if input[1] < -0.5649346:
                    var48 = -0.1021763
                else:
                    if input[9] < -0.3513631:
                        var48 = 0.107523344
                    else:
                        if input[7] < -0.4824063:
                            var48 = -0.10059481
                        else:
                            var48 = 0.042631127
            else:
                if input[9] < -0.65395796:
                    var48 = -0.0021487754
                else:
                    var48 = 0.12666139
        else:
            var48 = 0.11422841
    if input[0] < 1.8868077:
        if input[0] < 1.4623349:
            if input[7] < -1.1768137:
                if input[7] < -1.2378846:
                    if input[0] < 0.7272721:
                        if input[0] < 0.31315225:
                            var49 = -0.009139091
                        else:
                            var49 = 0.09800261
                    else:
                        if input[1] < 0.3850742:
                            var49 = -0.17895803
                        else:
                            var49 = 0.024704942
                else:
                    if input[8] < -0.032779966:
                        if input[1] < 0.5750759:
                            var49 = -0.14730619
                        else:
                            var49 = 0.21833958
                    else:
                        if input[1] < -0.08993021:
                            var49 = -0.03938685
                        else:
                            var49 = -0.26040787
            else:
                if input[7] < -1.133428:
                    if input[4] < 0.8088304:
                        if input[1] < -0.18493108:
                            var49 = -0.009064871
                        else:
                            var49 = 0.3208977
                    else:
                        var49 = -0.11559599
                else:
                    if input[7] < -1.0354191:
                        if input[1] < 0.3850742:
                            var49 = -0.18125515
                        else:
                            var49 = 0.005701064
                    else:
                        if input[7] < -0.9472609:
                            var49 = 0.10533702
                        else:
                            var49 = 0.0014365279
        else:
            if input[3] < 1.0922755:
                if input[3] < 0.71319413:
                    if input[9] < 0.9676402:
                        if input[8] < -0.027922574:
                            var49 = -0.07065012
                        else:
                            var49 = 0.14456667
                    else:
                        if input[3] < 0.5267485:
                            var49 = -0.20244922
                        else:
                            var49 = 0.013247247
                else:
                    if input[9] < 0.9055695:
                        var49 = -0.29740593
                    else:
                        var49 = -0.05435182
            else:
                if input[10] < -0.5500156:
                    var49 = 0.3141893
                else:
                    var49 = -0.11502907
    else:
        if input[3] < 0.37825713:
            if input[10] < -0.006615333:
                if input[7] < -1.0090576:
                    var49 = -0.036060233
                else:
                    if input[1] < 0.10007155:
                        var49 = 0.038528927
                    else:
                        var49 = 0.4565554
            else:
                var49 = -0.09583809
        else:
            if input[14] < 1.0:
                if input[12] < 1.0:
                    if input[9] < 0.6572865:
                        if input[2] < -0.005739468:
                            var49 = -0.018176032
                        else:
                            var49 = -0.196015
                    else:
                        var49 = 0.1322604
                else:
                    if input[3] < 0.8783539:
                        var49 = 0.28259814
                    else:
                        var49 = 0.023858191
            else:
                if input[9] < -0.95655286:
                    var49 = 0.13221613
                else:
                    if input[0] < 1.9903376:
                        var49 = -0.07280682
                    else:
                        var49 = -0.291986
    if input[0] < 0.7893901:
        if input[0] < 0.4580942:
            if input[0] < 0.37527025:
                if input[0] < 0.1889163:
                    if input[8] < -0.02615307:
                        if input[8] < -0.026938703:
                            var50 = 0.011059478
                        else:
                            var50 = 0.11446503
                    else:
                        if input[1] < 0.2900733:
                            var50 = -0.05277979
                        else:
                            var50 = 0.021466825
                else:
                    if input[8] < -0.020337362:
                        if input[11] < 1.0:
                            var50 = -0.19359507
                        else:
                            var50 = -0.026369907
                    else:
                        if input[3] < 0.5637478:
                            var50 = 0.2553453
                        else:
                            var50 = 0.008942434
            else:
                if input[3] < 0.3736695:
                    if input[6] < 0.97067964:
                        if input[7] < -0.49881262:
                            var50 = -0.018424854
                        else:
                            var50 = 0.43171933
                    else:
                        if input[0] < 0.4270352:
                            var50 = 0.20018329
                        else:
                            var50 = -0.19749503
                else:
                    if input[1] < -0.08993021:
                        if input[1] < -0.37493283:
                            var50 = -0.040431116
                        else:
                            var50 = 0.3447429
                    else:
                        if input[9] < -0.801376:
                            var50 = 0.08838493
                        else:
                            var50 = -0.2252957
        else:
            if input[3] < 0.47035775:
                if input[9] < -1.2048358:
                    var50 = -0.21422224
                else:
                    if input[9] < -1.096212:
                        if input[1] < 0.3850742:
                            var50 = 0.4068645
                        else:
                            var50 = 0.010751901
                    else:
                        if input[7] < -0.28583017:
                            var50 = -0.09672353
                        else:
                            var50 = 0.06626238
            else:
                if input[10] < -0.006615333:
                    if input[8] < -0.023776902:
                        if input[3] < 1.4619124:
                            var50 = -0.26373294
                        else:
                            var50 = 0.1387189
                    else:
                        if input[1] < 0.5750759:
                            var50 = -0.10605872
                        else:
                            var50 = 0.16528985
                else:
                    if input[0] < 0.6755071:
                        if input[3] < 1.1227999:
                            var50 = 0.2544557
                        else:
                            var50 = -0.07725705
                    else:
                        if input[3] < 0.86054796:
                            var50 = -0.20319474
                        else:
                            var50 = -0.047698066
    else:
        if input[0] < 0.8100961:
            if input[1] < -0.37493283:
                var50 = -0.0791843
            else:
                if input[8] < -0.027020918:
                    var50 = 0.056798723
                else:
                    var50 = 0.5347061
        else:
            if input[12] < 1.0:
                if input[8] < -0.016378978:
                    if input[6] < 0.97067964:
                        if input[7] < 1.1123637:
                            var50 = 0.0064621842
                        else:
                            var50 = 0.16998792
                    else:
                        if input[8] < -0.026213264:
                            var50 = -0.116441645
                        else:
                            var50 = 0.118492015
                else:
                    if input[0] < 1.5762178:
                        if input[1] < 0.7650777:
                            var50 = -0.24869892
                        else:
                            var50 = -0.024218677
                    else:
                        if input[0] < 1.8246897:
                            var50 = 0.2053962
                        else:
                            var50 = -0.10436144
            else:
                if input[3] < 0.037335813:
                    var50 = -0.25248006
                else:
                    if input[6] < 0.97067964:
                        if input[7] < 0.7475207:
                            var50 = 0.06942507
                        else:
                            var50 = -0.15501288
                    else:
                        if input[9] < 0.059855595:
                            var50 = 0.027666574
                        else:
                            var50 = 0.23517759
    if input[1] < 2.3800926:
        if input[10] < 2.8915195:
            if input[14] < 1.0:
                if input[2] < 1.7204164:
                    if input[10] < -0.27831548:
                        if input[7] < -0.86889863:
                            var51 = -0.038299963
                        else:
                            var51 = 0.024218904
                    else:
                        if input[1] < 0.3850742:
                            var51 = -0.065518536
                        else:
                            var51 = 0.018837197
                else:
                    if input[7] < -0.704771:
                        if input[1] < 0.19507243:
                            var51 = 0.23233534
                        else:
                            var51 = -0.08019536
                    else:
                        if input[1] < -0.75493634:
                            var51 = -0.000114916336
                        else:
                            var51 = -0.22905211
            else:
                if input[7] < 0.54616344:
                    if input[7] < -0.0044453996:
                        if input[7] < -0.15285553:
                            var51 = -0.0025132848
                        else:
                            var51 = 0.14554898
                    else:
                        if input[9] < -0.9875882:
                            var51 = 0.119208485
                        else:
                            var51 = -0.102857456
                else:
                    if input[7] < 1.2988641:
                        if input[1] < 0.8600786:
                            var51 = 0.038930804
                        else:
                            var51 = 0.2016798
                    else:
                        if input[0] < -0.4322635:
                            var51 = 0.075104654
                        else:
                            var51 = -0.09580241
        else:
            if input[7] < -1.0934299:
                if input[0] < 0.28209326:
                    var51 = 0.23660243
                else:
                    var51 = 0.04442292
            else:
                if input[7] < 1.1829834:
                    if input[7] < 0.5943842:
                        if input[7] < 0.060869616:
                            var51 = -0.07753921
                        else:
                            var51 = 0.10237209
                    else:
                        var51 = -0.15162787
                else:
                    var51 = 0.13260181
    else:
        if input[3] < 0.7214533:
            if input[6] < 0.97067964:
                if input[3] < 0.19150281:
                    var51 = 0.10231409
                else:
                    var51 = -0.11224752
            else:
                if input[2] < 1.0299541:
                    var51 = -0.2577479
                else:
                    if input[2] < 1.3751853:
                        var51 = 0.06550085
                    else:
                        var51 = -0.12288218
        else:
            if input[8] < -0.022858713:
                if input[7] < 0.38036832:
                    var51 = 0.35008997
                else:
                    if input[0] < -0.0802616:
                        var51 = 0.06130854
                    else:
                        var51 = -0.13468437
            else:
                var51 = -0.093103856
    if input[4] < 2.5279171:
        if input[7] < -0.5418341:
            if input[7] < -0.61021817:
                if input[1] < -1.0399389:
                    if input[8] < -0.01967467:
                        if input[1] < -1.3249416:
                            var52 = 0.16396718
                        else:
                            var52 = -0.07201809
                    else:
                        if input[3] < 0.92170113:
                            var52 = -0.24142052
                        else:
                            var52 = -0.020974174
                else:
                    if input[1] < 0.10007155:
                        if input[9] < 1.3400646:
                            var52 = 0.02282145
                        else:
                            var52 = 0.282719
                    else:
                        if input[0] < -1.5193281:
                            var52 = 0.14842865
                        else:
                            var52 = -0.02502052
            else:
                if input[0] < 1.3691579:
                    if input[1] < -0.46993372:
                        if input[9] < -0.19618623:
                            var52 = -0.14070435
                        else:
                            var52 = 0.035814688
                    else:
                        if input[3] < -0.63909185:
                            var52 = 0.00009489517
                        else:
                            var52 = 0.26258287
                else:
                    var52 = -0.12340104
        else:
            if input[8] < -0.01822945:
                if input[8] < -0.019090505:
                    if input[8] < -0.020045163:
                        if input[7] < -0.4824063:
                            var52 = -0.1241083
                        else:
                            var52 = -0.0030374527
                    else:
                        if input[10] < -0.5500156:
                            var52 = -0.011534859
                        else:
                            var52 = -0.2615537
                else:
                    if input[0] < -0.3287335:
                        var52 = 0.011315698
                    else:
                        if input[3] < 1.3814396:
                            var52 = 0.48457712
                        else:
                            var52 = 0.11651898
            else:
                if input[5] < 0.64104193:
                    var52 = 0.027156206
                else:
                    var52 = -0.25556546
    else:
        if input[0] < 1.224216:
            if input[0] < 0.58233017:
                if input[12] < 1.0:
                    if input[14] < 1.0:
                        if input[9] < 0.1684794:
                            var52 = -0.08584569
                        else:
                            var52 = 0.09187811
                    else:
                        var52 = 0.15840375
                else:
                    if input[9] < -0.37463963:
                        var52 = -0.09583633
                    else:
                        var52 = 0.049377937
            else:
                var52 = -0.05872949
        else:
            var52 = 0.13280635
    if input[0] < -1.4365041:
        if input[8] < -0.023865093:
            if input[3] < 0.3463231:
                if input[7] < -0.019357089:
                    if input[10] < 0.1874562:
                        if input[5] < 0.64104193:
                            var53 = -0.044678174
                        else:
                            var53 = -0.24543749
                    else:
                        if input[9] < -1.049659:
                            var53 = -0.120265655
                        else:
                            var53 = 0.10572792
                else:
                    if input[8] < -0.030062638:
                        if input[1] < 0.5750759:
                            var53 = -0.029730838
                        else:
                            var53 = 0.24064825
                    else:
                        var53 = 0.33802366
            else:
                if input[0] < -2.0680368:
                    if input[14] < 1.0:
                        if input[10] < -0.19680543:
                            var53 = -0.17702377
                        else:
                            var53 = -0.02719021
                    else:
                        var53 = 0.17988439
                else:
                    if input[8] < -0.029576529:
                        var53 = 0.028698547
                    else:
                        if input[3] < 1.3407071:
                            var53 = -0.2677355
                        else:
                            var53 = -0.05710458
        else:
            if input[8] < -0.023085767:
                var53 = 0.35542452
            else:
                if input[5] < 0.64104193:
                    if input[10] < -0.595299:
                        var53 = 0.09022325
                    else:
                        if input[9] < -0.9798294:
                            var53 = -0.024320308
                        else:
                            var53 = -0.26730636
                else:
                    if input[9] < 0.26934436:
                        if input[8] < -0.0128205:
                            var53 = -0.0238528
                        else:
                            var53 = 0.23468973
                    else:
                        if input[6] < 0.97067964:
                            var53 = 0.074515074
                        else:
                            var53 = -0.20165825
    else:
        if input[0] < -1.2708561:
            if input[3] < 0.80357724:
                if input[1] < 1.335083:
                    if input[14] < 1.0:
                        if input[10] < -0.42926002:
                            var53 = 0.4595962
                        else:
                            var53 = 0.0832601
                    else:
                        if input[0] < -1.3536801:
                            var53 = -0.18647301
                        else:
                            var53 = 0.25622407
                else:
                    var53 = -0.18746471
            else:
                if input[9] < -0.801376:
                    var53 = 0.05326616
                else:
                    if input[0] < -1.3950921:
                        var53 = 0.051941887
                    else:
                        var53 = -0.25962743
        else:
            if input[3] < 0.45116842:
                if input[0] < -0.6496764:
                    if input[3] < -0.13747577:
                        if input[5] < 0.64104193:
                            var53 = 0.08098313
                        else:
                            var53 = -0.09917256
                    else:
                        if input[10] < -0.42926002:
                            var53 = -0.26438132
                        else:
                            var53 = -0.047504954
                else:
                    if input[0] < -0.31838053:
                        if input[1] < 0.10007155:
                            var53 = 0.18151829
                        else:
                            var53 = -0.000052975698
                    else:
                        if input[0] < -0.06990861:
                            var53 = -0.14478475
                        else:
                            var53 = 0.0037937586
            else:
                if input[3] < 0.47971871:
                    if input[9] < 0.39348584:
                        if input[0] < 0.7065661:
                            var53 = -0.14869349
                        else:
                            var53 = 0.18077372
                    else:
                        if input[0] < 0.94468504:
                            var53 = 0.39598298
                        else:
                            var53 = 0.0013173801
                else:
                    if input[0] < -1.1983852:
                        if input[1] < 0.005070672:
                            var53 = 0.06772712
                        else:
                            var53 = 0.29476148
                    else:
                        if input[12] < 1.0:
                            var53 = -0.016484166
                        else:
                            var53 = 0.024282945
    if input[2] < 1.3751853:
        if input[7] < 1.7370887:
            if input[7] < 1.57172:
                if input[7] < 1.5329322:
                    if input[3] < 0.29352525:
                        if input[1] < 2.2850916:
                            var54 = 0.021348804
                        else:
                            var54 = -0.19531803
                    else:
                        if input[3] < 0.45116842:
                            var54 = -0.06497982
                        else:
                            var54 = 0.002228129
                else:
                    if input[2] < -0.6962018:
                        if input[3] < 0.5095043:
                            var54 = 0.018555386
                        else:
                            var54 = 0.24997155
                    else:
                        if input[12] < 1.0:
                            var54 = -0.27251562
                        else:
                            var54 = -0.046825983
            else:
                if input[7] < 1.6138473:
                    if input[1] < 1.4300839:
                        if input[7] < 1.5997853:
                            var54 = 0.09716626
                        else:
                            var54 = 0.31075993
                    else:
                        var54 = -0.027767096
                else:
                    if input[3] < 0.6206916:
                        if input[13] < 1.0:
                            var54 = 0.17177622
                        else:
                            var54 = -0.091126524
                    else:
                        if input[2] < -0.6962018:
                            var54 = 0.13675797
                        else:
                            var54 = -0.2564178
        else:
            var54 = -0.16381815
    else:
        if input[3] < 0.36641937:
            if input[8] < -0.027195407:
                if input[8] < -0.028794577:
                    if input[1] < 0.8600786:
                        if input[9] < 0.385727:
                            var54 = 0.10958318
                        else:
                            var54 = -0.109051585
                    else:
                        if input[0] < -0.60826445:
                            var54 = -0.19126819
                        else:
                            var54 = 0.18829595
                else:
                    var54 = 0.26246557
            else:
                if input[7] < -1.380174:
                    var54 = -0.06646846
                else:
                    var54 = -0.30129573
        else:
            if input[8] < -0.02477459:
                if input[8] < -0.026267394:
                    if input[3] < 1.0922755:
                        if input[8] < -0.026938703:
                            var54 = -0.0026997447
                        else:
                            var54 = 0.2842455
                    else:
                        var54 = -0.18610185
                else:
                    if input[8] < -0.025257612:
                        if input[7] < 0.6485844:
                            var54 = -0.28466007
                        else:
                            var54 = -0.072756976
                    else:
                        var54 = -0.04435094
            else:
                if input[7] < 0.022111539:
                    if input[3] < 0.5138537:
                        if input[1] < 0.19507243:
                            var54 = 0.27419132
                        else:
                            var54 = 0.018375898
                    else:
                        if input[9] < 1.2081643:
                            var54 = -0.08574917
                        else:
                            var54 = 0.04162713
                else:
                    if input[7] < 0.19574775:
                        var54 = 0.41318676
                    else:
                        var54 = 0.09914315
    if input[14] < 1.0:
        if input[0] < 1.8868077:
            if input[0] < 1.4830408:
                if input[7] < 1.3543655:
                    if input[7] < 0.7595052:
                        if input[5] < 0.64104193:
                            var55 = -0.038296893
                        else:
                            var55 = 0.018218415
                    else:
                        if input[1] < -0.18493108:
                            var55 = -0.16870171
                        else:
                            var55 = -0.03498086
                else:
                    if input[7] < 1.4636902:
                        if input[9] < -0.0022151496:
                            var55 = 0.24066734
                        else:
                            var55 = 0.010492901
                    else:
                        if input[1] < 1.335083:
                            var55 = -0.045513183
                        else:
                            var55 = 0.15087135
            else:
                if input[10] < -0.66645855:
                    if input[9] < 0.9676402:
                        var55 = 0.159565
                    else:
                        var55 = -0.08949265
                else:
                    if input[7] < 1.0982982:
                        var55 = -0.24484989
                    else:
                        var55 = -0.058091983
        else:
            if input[0] < 1.9282197:
                var55 = 0.33326465
            else:
                if input[0] < 1.9903376:
                    var55 = -0.1754696
                else:
                    if input[1] < 0.48007506:
                        if input[1] < -0.08993021:
                            var55 = 0.073702924
                        else:
                            var55 = -0.10526934
                    else:
                        if input[3] < 0.53883106:
                            var55 = 0.2543646
                        else:
                            var55 = -0.01683833
    else:
        if input[3] < 2.0235312:
            if input[0] < 2.0628088:
                if input[9] < -1.2203535:
                    if input[9] < -1.2901831:
                        if input[1] < 1.6200856:
                            var55 = 0.045881163
                        else:
                            var55 = -0.24925642
                    else:
                        if input[0] < -0.6393234:
                            var55 = 0.01837376
                        else:
                            var55 = -0.23452784
                else:
                    if input[7] < 1.3641307:
                        if input[7] < 1.2062398:
                            var55 = 0.008175986
                        else:
                            var55 = 0.15738714
                    else:
                        if input[7] < 1.4377079:
                            var55 = -0.22169158
                        else:
                            var55 = 0.00051866216
            else:
                if input[9] < -0.95655286:
                    var55 = 0.107833326
                else:
                    if input[9] < 0.7659103:
                        var55 = -0.25415796
                    else:
                        var55 = -0.01078897
        else:
            var55 = 0.18839933
    if input[6] < 0.97067964:
        if input[1] < 1.4300839:
            if input[9] < 1.6271418:
                if input[9] < 1.4874827:
                    if input[9] < 1.0917817:
                        if input[2] < 1.7204164:
                            var56 = 0.007998014
                        else:
                            var56 = -0.15352176
                    else:
                        if input[0] < -1.0534433:
                            var56 = -0.18673064
                        else:
                            var56 = -0.018749777
                else:
                    if input[11] < 1.0:
                        if input[4] < 0.8088304:
                            var56 = 0.3116662
                        else:
                            var56 = 0.09060252
                    else:
                        if input[0] < -0.16308558:
                            var56 = -0.14782716
                        else:
                            var56 = 0.15141553
            else:
                if input[0] < -0.49438146:
                    if input[7] < 0.16707173:
                        var56 = -0.081818506
                    else:
                        if input[7] < 1.1584231:
                            var56 = 0.30737793
                        else:
                            var56 = 0.07393156
                else:
                    if input[9] < 1.9762899:
                        if input[13] < 1.0:
                            var56 = -0.2527997
                        else:
                            var56 = 0.03510974
                    else:
                        if input[4] < 0.8088304:
                            var56 = 0.10811433
                        else:
                            var56 = -0.08926624
        else:
            if input[0] < -0.22520356:
                if input[0] < -1.2087382:
                    if input[9] < -0.1185978:
                        var56 = -0.057483174
                    else:
                        if input[10] < -0.66645855:
                            var56 = -0.0027484512
                        else:
                            var56 = 0.1856664
                else:
                    var56 = 0.2530401
            else:
                if input[0] < 0.8929201:
                    if input[2] < -0.35097063:
                        var56 = 0.16128503
                    else:
                        if input[7] < -1.1486096:
                            var56 = 0.06419873
                        else:
                            var56 = -0.18727931
                else:
                    if input[9] < 0.20727362:
                        var56 = -0.025686229
                    else:
                        if input[8] < -0.012035764:
                            var56 = 0.20818125
                        else:
                            var56 = 0.051098835
    else:
        if input[10] < 0.4009349:
            if input[10] < -0.42926002:
                if input[3] < 0.25296:
                    if input[9] < 1.2779939:
                        if input[7] < -0.4678239:
                            var56 = 0.0054929825
                        else:
                            var56 = -0.15313624
                    else:
                        if input[1] < 1.335083:
                            var56 = 0.14419381
                        else:
                            var56 = -0.121445835
                else:
                    if input[3] < 0.5545477:
                        if input[3] < 0.53883106:
                            var56 = 0.040578377
                        else:
                            var56 = 0.30647874
                    else:
                        if input[3] < 0.71319413:
                            var56 = -0.14042203
                        else:
                            var56 = 0.010238251
            else:
                if input[3] < 0.7086714:
                    if input[0] < -0.9188543:
                        if input[7] < 0.93511486:
                            var56 = -0.17776446
                        else:
                            var56 = 0.1363677
                    else:
                        if input[0] < -0.028496623:
                            var56 = 0.18449472
                        else:
                            var56 = 0.04960774
                else:
                    if input[8] < -0.0128205:
                        if input[7] < 0.69357884:
                            var56 = -0.17963842
                        else:
                            var56 = 0.07151334
                    else:
                        if input[1] < 0.7650777:
                            var56 = 0.17962097
                        else:
                            var56 = -0.108086176
        else:
            if input[7] < 0.67438555:
                if input[9] < -0.9798294:
                    if input[8] < -0.023085767:
                        if input[3] < 1.1227999:
                            var56 = 0.111932755
                        else:
                            var56 = -0.21671508
                    else:
                        if input[0] < -0.7014414:
                            var56 = 0.054974705
                        else:
                            var56 = -0.12621276
                else:
                    if input[3] < 0.5336792:
                        if input[7] < 0.2779922:
                            var56 = -0.23297592
                        else:
                            var56 = -0.037642866
                    else:
                        if input[0] < -0.22520356:
                            var56 = -0.22284555
                        else:
                            var56 = 0.20269008
            else:
                if input[3] < 1.2051187:
                    if input[1] < 0.5750759:
                        if input[7] < 1.3641307:
                            var56 = -0.26931357
                        else:
                            var56 = -0.07598911
                    else:
                        if input[3] < -0.0009882716:
                            var56 = -0.19671123
                        else:
                            var56 = 0.04125829
                else:
                    if input[8] < -0.026645351:
                        var56 = 0.16485997
                    else:
                        var56 = -0.035586145
    if input[10] < -0.19680543:
        if input[3] < 1.4018602:
            if input[3] < 0.93833226:
                if input[3] < 0.92594856:
                    if input[7] < 1.6966289:
                        if input[7] < 1.6715614:
                            var57 = 0.0005120297
                        else:
                            var57 = -0.17610732
                    else:
                        if input[10] < -0.595299:
                            var57 = 0.2426098
                        else:
                            var57 = -0.08060354
                else:
                    if input[7] < -0.71973884:
                        var57 = -0.061907493
                    else:
                        var57 = -0.23923045
            else:
                if input[9] < -0.73930526:
                    if input[1] < -0.75493634:
                        var57 = 0.042651806
                    else:
                        var57 = 0.33652812
                else:
                    if input[8] < -0.021682225:
                        if input[2] < -0.35097063:
                            var57 = -0.1530706
                        else:
                            var57 = 0.104800485
                    else:
                        if input[8] < -0.019266702:
                            var57 = -0.17553839
                        else:
                            var57 = 0.01254322
        else:
            if input[12] < 1.0:
                if input[9] < -0.37463963:
                    var57 = -0.24427389
                else:
                    if input[7] < -0.053549092:
                        if input[9] < 0.62625116:
                            var57 = -0.1515514
                        else:
                            var57 = 0.053454533
                    else:
                        if input[3] < 1.4931163:
                            var57 = -0.043447245
                        else:
                            var57 = 0.21779497
            else:
                if input[0] < 0.32350525:
                    var57 = -0.2711902
                else:
                    var57 = -0.09825324
    else:
        if input[0] < -1.2605032:
            if input[1] < 1.7150865:
                if input[7] < -1.5208627:
                    var57 = -0.1480954
                else:
                    if input[7] < -0.8552864:
                        var57 = 0.24534167
                    else:
                        if input[10] < 0.61441356:
                            var57 = 0.10332454
                        else:
                            var57 = -0.10255979
            else:
                var57 = -0.13074878
        else:
            if input[3] < 1.418603:
                if input[0] < -0.9499133:
                    if input[1] < 1.2400821:
                        if input[7] < 1.4974321:
                            var57 = -0.19660258
                        else:
                            var57 = 0.15098484
                    else:
                        if input[9] < -1.0186236:
                            var57 = 0.27612534
                        else:
                            var57 = -0.13039878
                else:
                    if input[0] < -0.8774423:
                        if input[8] < -0.025742803:
                            var57 = 0.28624022
                        else:
                            var57 = -0.042036843
                    else:
                        if input[3] < 1.1227999:
                            var57 = -0.012793146
                        else:
                            var57 = -0.108204216
            else:
                if input[10] < 0.23489591:
                    if input[0] < 0.4477412:
                        if input[13] < 1.0:
                            var57 = 0.42154965
                        else:
                            var57 = 0.065306045
                    else:
                        var57 = -0.012046865
                else:
                    if input[0] < -0.049202614:
                        var57 = -0.20099619
                    else:
                        if input[12] < 1.0:
                            var57 = 0.090504065
                        else:
                            var57 = -0.11759114
    if input[4] < 2.5279171:
        if input[4] < 0.8088304:
            if input[8] < -0.027789427:
                if input[8] < -0.028330084:
                    if input[8] < -0.028445441:
                        if input[1] < -0.75493634:
                            var58 = -0.055736132
                        else:
                            var58 = 0.02095057
                    else:
                        var58 = -0.22175863
                else:
                    if input[9] < -0.27377465:
                        if input[0] < -0.13202658:
                            var58 = 0.11532961
                        else:
                            var58 = -0.15692341
                    else:
                        if input[1] < 0.48007506:
                            var58 = 0.32321328
                        else:
                            var58 = -0.033412468
            else:
                if input[8] < -0.027456515:
                    if input[9] < 0.3314151:
                        if input[9] < -1.0806943:
                            var58 = -0.00060454465
                        else:
                            var58 = -0.29754496
                    else:
                        if input[9] < 0.6029746:
                            var58 = 0.2356645
                        else:
                            var58 = -0.1518149
                else:
                    if input[13] < 1.0:
                        if input[3] < 0.32362035:
                            var58 = -0.08916505
                        else:
                            var58 = 0.018499998
                    else:
                        if input[3] < 0.067967534:
                            var58 = 0.22053209
                        else:
                            var58 = -0.07341076
        else:
            if input[8] < -0.030567229:
                if input[11] < 1.0:
                    if input[7] < -1.3935872:
                        if input[9] < -0.19618623:
                            var58 = -0.0152106825
                        else:
                            var58 = 0.2626781
                    else:
                        if input[9] < 2.2866435:
                            var58 = -0.1690659
                        else:
                            var58 = 0.124489404
                else:
                    if input[1] < 0.5750759:
                        if input[7] < -0.15285553:
                            var58 = -0.08370292
                        else:
                            var58 = 0.08490436
                    else:
                        if input[0] < 0.106092334:
                            var58 = 0.0045433864
                        else:
                            var58 = -0.27913082
            else:
                if input[8] < -0.019266702:
                    if input[7] < -0.5418341:
                        if input[0] < 0.35456425:
                            var58 = 0.06695984
                        else:
                            var58 = 0.3159191
                    else:
                        if input[0] < 0.975744:
                            var58 = 0.045653097
                        else:
                            var58 = -0.15792385
                else:
                    if input[3] < 0.77152056:
                        if input[0] < 0.30279925:
                            var58 = -0.19936581
                        else:
                            var58 = -0.005017767
                    else:
                        if input[3] < 0.8141936:
                            var58 = 0.38151228
                        else:
                            var58 = -0.03461623
    else:
        if input[3] < 0.45116842:
            if input[9] < -0.7082699:
                if input[9] < -0.95655286:
                    var58 = 0.03276713
                else:
                    var58 = 0.1310085
            else:
                if input[7] < 0.608219:
                    if input[1] < 0.3850742:
                        if input[0] < -0.31838053:
                            var58 = 0.021544278
                        else:
                            var58 = -0.18792857
                    else:
                        var58 = 0.035475325
                else:
                    var58 = 0.05435229
        else:
            var58 = 0.12850079
    if input[0] < 0.7893901:
        if input[9] < 0.067614436:
            if input[8] < 0.00018711267:
                if input[3] < 1.613749:
                    if input[7] < -1.2713257:
                        if input[1] < 0.2900733:
                            var59 = -0.17779414
                        else:
                            var59 = 0.023819083
                    else:
                        if input[8] < -0.029305013:
                            var59 = 0.033241156
                        else:
                            var59 = -0.010949659
                else:
                    if input[0] < 0.5409182:
                        if input[11] < 1.0:
                            var59 = -0.25489914
                        else:
                            var59 = -0.04800029
                    else:
                        var59 = 0.04991893
            else:
                if input[2] < -0.005739468:
                    if input[3] < 0.13275805:
                        var59 = -0.21899608
                    else:
                        if input[1] < -0.46993372:
                            var59 = -0.07024542
                        else:
                            var59 = 0.09911936
                else:
                    if input[3] < 0.8833897:
                        if input[1] < -0.75493634:
                            var59 = 0.029196447
                        else:
                            var59 = 0.48000646
                    else:
                        var59 = -0.096398436
        else:
            if input[0] < 0.27174026:
                if input[9] < 0.09864981:
                    if input[13] < 1.0:
                        if input[3] < 0.31213254:
                            var59 = -0.12576158
                        else:
                            var59 = -0.3382896
                    else:
                        var59 = 0.055861283
                else:
                    if input[7] < -1.6840237:
                        if input[5] < 0.64104193:
                            var59 = 0.34504783
                        else:
                            var59 = 0.014367974
                    else:
                        if input[9] < 1.6969715:
                            var59 = -0.007945236
                        else:
                            var59 = 0.06601892
            else:
                if input[9] < 0.40900353:
                    if input[3] < 0.8433095:
                        if input[9] < 0.15296172:
                            var59 = -0.08617139
                        else:
                            var59 = -0.29209954
                    else:
                        if input[8] < -0.019869125:
                            var59 = -0.13027045
                        else:
                            var59 = 0.09120977
                else:
                    if input[9] < 0.47107428:
                        if input[8] < -0.027137408:
                            var59 = -0.0041366406
                        else:
                            var59 = 0.44140455
                    else:
                        if input[0] < 0.35456425:
                            var59 = -0.18044353
                        else:
                            var59 = -0.033078376
    else:
        if input[0] < 0.8100961:
            if input[1] < -0.37493283:
                var59 = -0.06979978
            else:
                if input[8] < -0.027020918:
                    var59 = 0.026552554
                else:
                    var59 = 0.3900537
        else:
            if input[7] < -1.699336:
                var59 = -0.19902758
            else:
                if input[2] < 1.7204164:
                    if input[3] < -0.3058544:
                        if input[7] < 1.542998:
                            var59 = 0.029121565
                        else:
                            var59 = 0.36999452
                    else:
                        if input[12] < 1.0:
                            var59 = -0.044333965
                        else:
                            var59 = 0.048712946
                else:
                    if input[0] < 1.317393:
                        if input[3] < 0.75438815:
                            var59 = -0.23600622
                        else:
                            var59 = -0.040763147
                    else:
                        if input[7] < -0.080064:
                            var59 = -0.116842814
                        else:
                            var59 = 0.15557462
    if input[7] < 1.6285735:
        if input[7] < 1.5997853:
            if input[0] < -0.4012045:
                if input[0] < -0.7014414:
                    if input[8] < -0.02895312:
                        if input[3] < 0.5267485:
                            var60 = -0.014143078
                        else:
                            var60 = -0.21872169
                    else:
                        if input[8] < -0.028399616:
                            var60 = 0.21205744
                        else:
                            var60 = 0.011815024
                else:
                    if input[3] < 0.5189618:
                        if input[1] < 1.4300839:
                            var60 = -0.024982402
                        else:
                            var60 = 0.23741944
                    else:
                        if input[7] < 1.3133167:
                            var60 = -0.17440394
                        else:
                            var60 = 0.15461491
            else:
                if input[0] < -0.12167359:
                    if input[3] < 0.4090033:
                        if input[0] < -0.31838053:
                            var60 = 0.12848434
                        else:
                            var60 = -0.12081556
                    else:
                        if input[0] < -0.23555654:
                            var60 = 0.007335418
                        else:
                            var60 = 0.17381519
                else:
                    if input[0] < -0.06990861:
                        if input[11] < 1.0:
                            var60 = -0.2789739
                        else:
                            var60 = -0.013391401
                    else:
                        if input[0] < -0.049202614:
                            var60 = 0.13493177
                        else:
                            var60 = 0.0010001074
        else:
            if input[1] < -0.27993196:
                var60 = -0.006529619
            else:
                if input[10] < -0.27831548:
                    var60 = 0.2909326
                else:
                    var60 = -0.0015547343
    else:
        if input[3] < 0.6206916:
            if input[10] < -0.5500156:
                if input[2] < 1.3751853:
                    if input[6] < 0.97067964:
                        if input[2] < 0.68472284:
                            var60 = 0.28509724
                        else:
                            var60 = 0.06921286
                    else:
                        var60 = 0.026180211
                else:
                    var60 = -0.08977324
            else:
                if input[10] < 0.61441356:
                    if input[10] < -0.19680543:
                        if input[2] < 0.68472284:
                            var60 = 0.07609171
                        else:
                            var60 = -0.16617624
                    else:
                        var60 = -0.22636327
                else:
                    var60 = 0.1711703
        else:
            if input[0] < -0.7325004:
                if input[1] < -0.08993021:
                    var60 = -0.17635265
                else:
                    var60 = 0.11393947
            else:
                if input[0] < 1.1620979:
                    var60 = -0.25224152
                else:
                    var60 = -0.06474287
    if input[3] < 1.0639395:
        if input[3] < 1.0300175:
            if input[3] < 1.0212783:
                if input[3] < 1.0062785:
                    if input[3] < 0.94771826:
                        if input[12] < 1.0:
                            var61 = -0.011141493
                        else:
                            var61 = 0.013234619
                    else:
                        if input[7] < 1.223257:
                            var61 = 0.10392511
                        else:
                            var61 = -0.1490654
                else:
                    if input[9] < -0.5142988:
                        if input[14] < 1.0:
                            var61 = 0.2820011
                        else:
                            var61 = -0.19530527
                    else:
                        if input[2] < 1.3751853:
                            var61 = -0.2870609
                        else:
                            var61 = 0.06307219
            else:
                var61 = 0.1755291
        else:
            if input[9] < 0.26934436:
                if input[1] < -0.46993372:
                    var61 = -0.05978802
                else:
                    var61 = -0.31479523
            else:
                if input[9] < 0.69608074:
                    var61 = 0.21887028
                else:
                    if input[11] < 1.0:
                        var61 = -0.016055351
                    else:
                        var61 = -0.12539645
    else:
        if input[3] < 1.1227999:
            if input[7] < -0.797749:
                if input[7] < -1.3359233:
                    if input[10] < -0.66645855:
                        var61 = 0.19272497
                    else:
                        var61 = 0.05060623
                else:
                    var61 = -0.23270752
            else:
                if input[8] < -0.025452988:
                    if input[4] < 0.8088304:
                        if input[7] < 1.4206333:
                            var61 = -0.18807946
                        else:
                            var61 = 0.122572295
                    else:
                        var61 = 0.19889721
                else:
                    if input[0] < 0.4684472:
                        if input[0] < -1.0430902:
                            var61 = 0.057958763
                        else:
                            var61 = 0.44096103
                    else:
                        var61 = 0.034176562
        else:
            if input[12] < 1.0:
                if input[9] < 1.0452287:
                    if input[7] < 0.8663735:
                        if input[8] < -0.025199242:
                            var61 = -0.15553704
                        else:
                            var61 = 0.043208987
                    else:
                        if input[1] < -0.6599355:
                            var61 = -0.098510884
                        else:
                            var61 = 0.1891364
                else:
                    if input[9] < 1.821113:
                        if input[3] < 1.6430904:
                            var61 = -0.21764885
                        else:
                            var61 = 0.06964054
                    else:
                        var61 = 0.114302404
            else:
                if input[0] < 1.089627:
                    if input[9] < 1.122817:
                        if input[8] < -0.027789427:
                            var61 = 0.13827887
                        else:
                            var61 = -0.18883702
                    else:
                        if input[3] < 1.4018602:
                            var61 = 0.19456187
                        else:
                            var61 = -0.15538764
                else:
                    if input[5] < 0.64104193:
                        var61 = 0.27397943
                    else:
                        var61 = 0.0052722376
    if input[7] < 0.93511486:
        if input[7] < 0.9238795:
            if input[7] < 0.8763027:
                if input[7] < 0.8663735:
                    if input[7] < 0.8511328:
                        if input[7] < 0.67438555:
                            var62 = -0.0010888305
                        else:
                            var62 = 0.053119443
                    else:
                        if input[3] < 0.5545477:
                            var62 = -0.035160106
                        else:
                            var62 = -0.20126463
                else:
                    if input[10] < -0.5500156:
                        var62 = -0.09976833
                    else:
                        if input[10] < -0.006615333:
                            var62 = 0.38366386
                        else:
                            var62 = 0.073417
            else:
                if input[1] < 0.67007685:
                    if input[3] < 0.9687012:
                        if input[10] < -0.595299:
                            var62 = -0.07971817
                        else:
                            var62 = -0.28035548
                    else:
                        var62 = 0.073995866
                else:
                    if input[6] < 0.97067964:
                        var62 = 0.31652987
                    else:
                        var62 = -0.10439085
        else:
            if input[4] < 0.8088304:
                var62 = 0.367221
            else:
                var62 = -0.061671935
    else:
        if input[7] < 1.0535349:
            if input[1] < 0.8600786:
                if input[7] < 1.004733:
                    if input[9] < 0.20727362:
                        if input[9] < -0.16515085:
                            var62 = -0.14101283
                        else:
                            var62 = 0.34766817
                    else:
                        if input[0] < -0.06990861:
                            var62 = -0.23867555
                        else:
                            var62 = -0.059483994
                else:
                    if input[1] < -0.75493634:
                        var62 = -0.027748976
                    else:
                        if input[0] < 0.61338913:
                            var62 = -0.3240947
                        else:
                            var62 = -0.08369523
            else:
                if input[10] < -0.5500156:
                    var62 = -0.101231165
                else:
                    if input[5] < 0.64104193:
                        var62 = -0.025749495
                    else:
                        var62 = 0.21395333
        else:
            if input[7] < 1.1220839:
                if input[3] < 0.9028802:
                    if input[2] < 1.0299541:
                        if input[13] < 1.0:
                            var62 = -0.06541028
                        else:
                            var62 = 0.25707212
                    else:
                        if input[3] < 0.43356293:
                            var62 = 0.015224284
                        else:
                            var62 = 0.4546345
                else:
                    if input[1] < 0.67007685:
                        var62 = -0.16417533
                    else:
                        var62 = -0.011413118
            else:
                if input[2] < 0.68472284:
                    if input[10] < -0.006615333:
                        if input[0] < -1.0534433:
                            var62 = 0.15856433
                        else:
                            var62 = 0.023836777
                    else:
                        if input[6] < 0.97067964:
                            var62 = 0.029652307
                        else:
                            var62 = -0.09297853
                else:
                    if input[9] < 0.71935725:
                        if input[8] < -0.028014852:
                            var62 = -0.17530239
                        else:
                            var62 = 0.082682215
                    else:
                        if input[5] < 0.64104193:
                            var62 = 0.098978
                        else:
                            var62 = -0.054982666
    if input[3] < 0.30654135:
        if input[12] < 1.0:
            if input[8] < -0.032779966:
                if input[4] < 0.8088304:
                    if input[1] < 0.5750759:
                        if input[7] < -1.42103:
                            var63 = -0.17846182
                        else:
                            var63 = 0.010457394
                    else:
                        if input[7] < -1.050368:
                            var63 = 0.1901115
                        else:
                            var63 = 0.043403093
                else:
                    if input[14] < 1.0:
                        if input[0] < -0.76355934:
                            var63 = 0.008588642
                        else:
                            var63 = -0.11717255
                    else:
                        if input[0] < -0.6910884:
                            var63 = -0.11853154
                        else:
                            var63 = 0.034273524
            else:
                if input[1] < 0.48007506:
                    if input[0] < 0.6755071:
                        if input[10] < 0.10206473:
                            var63 = 0.2261883
                        else:
                            var63 = -0.05691054
                    else:
                        if input[3] < 0.067967534:
                            var63 = 0.03159299
                        else:
                            var63 = -0.26155293
                else:
                    if input[0] < -1.1569732:
                        var63 = 0.20137343
                    else:
                        if input[0] < -0.27696854:
                            var63 = -0.18669152
                        else:
                            var63 = 0.032047417
        else:
            if input[3] < 0.037335813:
                if input[1] < 1.5250847:
                    if input[10] < -0.19680543:
                        if input[2] < 1.3751853:
                            var63 = -0.29133594
                        else:
                            var63 = -0.051466398
                    else:
                        if input[9] < -0.8944821:
                            var63 = -0.18554041
                        else:
                            var63 = 0.08355559
                else:
                    var63 = 0.04393927
            else:
                if input[0] < -1.5503871:
                    var63 = 0.20387696
                else:
                    if input[0] < -0.26661554:
                        if input[8] < -0.028844493:
                            var63 = -0.051273875
                        else:
                            var63 = -0.25751653
                    else:
                        if input[9] < 0.02106138:
                            var63 = 0.107148334
                        else:
                            var63 = -0.068793416
    else:
        if input[3] < 0.43356293:
            if input[13] < 1.0:
                if input[9] < 1.3400646:
                    if input[0] < 1.5140998:
                        if input[0] < 0.955038:
                            var63 = 0.0066529713
                        else:
                            var63 = -0.23384242
                    else:
                        var63 = 0.21608861
                else:
                    if input[4] < 0.8088304:
                        var63 = -0.24877365
                    else:
                        var63 = 0.021899544
            else:
                if input[3] < 0.32362035:
                    var63 = 0.0130447075
                else:
                    if input[0] < 0.92397904:
                        var63 = -0.30185845
                    else:
                        var63 = -0.01850774
        else:
            if input[0] < 1.265628:
                if input[0] < 0.7893901:
                    if input[0] < 0.34421125:
                        if input[5] < 0.64104193:
                            var63 = -0.025935544
                        else:
                            var63 = 0.023581127
                    else:
                        if input[8] < -0.023676272:
                            var63 = -0.11886681
                        else:
                            var63 = -0.0017892481
                else:
                    if input[9] < 0.059855595:
                        if input[8] < -0.020045163:
                            var63 = 0.06243819
                        else:
                            var63 = -0.1510341
                    else:
                        if input[3] < 1.0300175:
                            var63 = 0.22879633
                        else:
                            var63 = -0.04118987
            else:
                if input[8] < -0.006023118:
                    if input[2] < 1.0299541:
                        if input[9] < -0.74706405:
                            var63 = 0.022404145
                        else:
                            var63 = -0.18993905
                    else:
                        if input[7] < -0.33451837:
                            var63 = -0.20396607
                        else:
                            var63 = 0.08425368
                else:
                    if input[8] < 0.1384076:
                        if input[3] < 0.72517794:
                            var63 = 0.009466256
                        else:
                            var63 = 0.21063757
                    else:
                        var63 = -0.13137327
    if input[4] < 2.5279171:
        if input[0] < -1.4365041:
            if input[8] < -0.023865093:
                if input[8] < -0.026715819:
                    if input[3] < 0.5138537:
                        if input[7] < 0.2779922:
                            var64 = -0.10261071
                        else:
                            var64 = 0.093587
                    else:
                        if input[6] < 0.97067964:
                            var64 = -0.1925005
                        else:
                            var64 = 0.024260113
                else:
                    if input[3] < 1.3407071:
                        var64 = -0.26543313
                    else:
                        var64 = 0.011687255
            else:
                if input[8] < -0.023402806:
                    var64 = 0.3149129
                else:
                    if input[3] < 0.7803133:
                        if input[7] < -0.9653717:
                            var64 = 0.0036583764
                        else:
                            var64 = -0.20188802
                    else:
                        if input[1] < 1.5250847:
                            var64 = 0.085534185
                        else:
                            var64 = -0.11947953
        else:
            if input[0] < -1.2087382:
                if input[7] < 0.110421926:
                    if input[8] < -0.007933236:
                        if input[1] < 0.7650777:
                            var64 = -0.14176148
                        else:
                            var64 = 0.056105096
                    else:
                        if input[8] < 0.021998629:
                            var64 = 0.24068756
                        else:
                            var64 = -0.09361547
                else:
                    if input[9] < 0.5486627:
                        if input[10] < -0.34624052:
                            var64 = 0.30976778
                        else:
                            var64 = 0.052284274
                    else:
                        if input[0] < -1.3536801:
                            var64 = -0.18130489
                        else:
                            var64 = 0.11247529
            else:
                if input[0] < -1.1259142:
                    if input[10] < -0.5500156:
                        if input[13] < 1.0:
                            var64 = 0.17073552
                        else:
                            var64 = -0.041937653
                    else:
                        if input[7] < -0.98032284:
                            var64 = -0.022034792
                        else:
                            var64 = -0.28630024
                else:
                    if input[10] < -0.42926002:
                        if input[0] < -0.4115575:
                            var64 = -0.050843135
                        else:
                            var64 = -0.00036937717
                    else:
                        if input[0] < -1.0534433:
                            var64 = 0.23298058
                        else:
                            var64 = 0.0080297515
    else:
        if input[8] < -0.03078074:
            if input[0] < -0.6910884:
                var64 = -0.03555079
            else:
                if input[0] < -0.46332246:
                    var64 = 0.15672807
                else:
                    if input[7] < -0.33451837:
                        var64 = 0.07000097
                    else:
                        if input[7] < 0.36911884:
                            var64 = -0.13009232
                        else:
                            var64 = 0.032907125
        else:
            if input[0] < -0.0906146:
                var64 = 0.026467906
            else:
                var64 = 0.13276008
    if input[7] < 0.39287364:
        if input[7] < 0.35555807:
            if input[9] < 0.9676402:
                if input[9] < 0.8202222:
                    if input[0] < -1.0223843:
                        if input[7] < -0.797749:
                            var65 = 0.05196871
                        else:
                            var65 = -0.087796986
                    else:
                        if input[7] < -0.15285553:
                            var65 = 0.000024797737
                        else:
                            var65 = 0.05014804
                else:
                    if input[0] < -0.84638333:
                        if input[0] < -1.3433272:
                            var65 = 0.0033263613
                        else:
                            var65 = 0.42227545
                    else:
                        if input[3] < 0.5895688:
                            var65 = -0.10901837
                        else:
                            var65 = 0.1531703
            else:
                if input[9] < 1.029711:
                    if input[8] < -0.01822945:
                        var65 = -0.2639499
                    else:
                        var65 = -0.01378967
                else:
                    if input[0] < 1.0792739:
                        if input[8] < -0.016129123:
                            var65 = 0.044107396
                        else:
                            var65 = -0.06813988
                    else:
                        if input[1] < 1.0500803:
                            var65 = -0.17711481
                        else:
                            var65 = 0.030057712
        else:
            if input[2] < 0.68472284:
                if input[10] < -0.19680543:
                    if input[0] < 0.35456425:
                        var65 = 0.09082998
                    else:
                        var65 = 0.3728752
                else:
                    if input[3] < 0.4385279:
                        var65 = -0.1365082
                    else:
                        var65 = 0.17913468
            else:
                if input[9] < 0.781428:
                    var65 = -0.12359769
                else:
                    var65 = 0.024194896
    else:
        if input[7] < 0.4870541:
            if input[1] < 0.19507243:
                if input[9] < 0.98315793:
                    if input[9] < -1.2048358:
                        var65 = -0.027132787
                    else:
                        var65 = -0.30826494
                else:
                    var65 = 0.009400935
            else:
                if input[7] < 0.47282687:
                    if input[1] < 0.7650777:
                        if input[0] < -0.99132526:
                            var65 = -0.013966094
                        else:
                            var65 = 0.2949928
                    else:
                        if input[0] < -0.4322635:
                            var65 = -0.25209633
                        else:
                            var65 = 0.11546102
                else:
                    var65 = -0.25861776
        else:
            if input[7] < 0.5204659:
                if input[3] < 0.41504923:
                    if input[3] < -0.21520005:
                        var65 = -0.031493332
                    else:
                        var65 = -0.120825686
                else:
                    if input[3] < 0.72992915:
                        var65 = 0.37163508
                    else:
                        var65 = -0.04626438
            else:
                if input[14] < 1.0:
                    if input[8] < -0.028158316:
                        if input[0] < -1.1052083:
                            var65 = 0.095828295
                        else:
                            var65 = -0.022676194
                    else:
                        if input[9] < -0.23498043:
                            var65 = -0.24492447
                        else:
                            var65 = -0.043155253
                else:
                    if input[8] < -0.028330084:
                        if input[8] < -0.028824683:
                            var65 = 0.010727597
                        else:
                            var65 = -0.12352049
                    else:
                        if input[1] < -1.0399389:
                            var65 = 0.23831832
                        else:
                            var65 = 0.040405326
    if input[1] < 0.67007685:
        if input[8] < -0.02615307:
            if input[8] < -0.026892679:
                if input[7] < -0.694653:
                    if input[7] < -0.86889863:
                        if input[7] < -0.9472609:
                            var66 = 0.020160105
                        else:
                            var66 = -0.22354689
                    else:
                        if input[4] < 0.8088304:
                            var66 = 0.35172516
                        else:
                            var66 = 0.08208612
                else:
                    if input[7] < -0.5973654:
                        if input[4] < 0.8088304:
                            var66 = -0.26899168
                        else:
                            var66 = -0.021634294
                    else:
                        if input[7] < -0.114853054:
                            var66 = 0.050392345
                        else:
                            var66 = -0.011808447
            else:
                if input[10] < -0.42926002:
                    if input[8] < -0.026715819:
                        if input[3] < 0.79753643:
                            var66 = 0.32777408
                        else:
                            var66 = -0.037177082
                    else:
                        if input[1] < 0.005070672:
                            var66 = -0.2660665
                        else:
                            var66 = 0.063274555
                else:
                    if input[9] < 0.1684794:
                        if input[14] < 1.0:
                            var66 = -0.15388584
                        else:
                            var66 = 0.14829136
                    else:
                        var66 = 0.5542154
        else:
            if input[8] < -0.025588525:
                if input[3] < 1.4719155:
                    if input[9] < -1.2048358:
                        var66 = -0.02282652
                    else:
                        if input[13] < 1.0:
                            var66 = -0.24573673
                        else:
                            var66 = -0.017466241
                else:
                    var66 = 0.03689319
            else:
                if input[0] < -0.4012045:
                    if input[0] < -0.7014414:
                        if input[3] < 1.0922755:
                            var66 = -0.039213277
                        else:
                            var66 = 0.09976063
                    else:
                        if input[1] < 0.3850742:
                            var66 = -0.25481278
                        else:
                            var66 = 0.022672229
                else:
                    if input[8] < -0.024956916:
                        if input[0] < 0.31315225:
                            var66 = 0.35370997
                        else:
                            var66 = -0.07251483
                    else:
                        if input[1] < -0.37493283:
                            var66 = 0.057504285
                        else:
                            var66 = -0.02890517
    else:
        if input[11] < 1.0:
            if input[6] < 0.97067964:
                if input[7] < 0.30071127:
                    if input[3] < 1.0172395:
                        if input[10] < -0.5500156:
                            var66 = -0.10337236
                        else:
                            var66 = 0.0627454
                    else:
                        if input[0] < -0.76355934:
                            var66 = -0.026778908
                        else:
                            var66 = 0.25316647
                else:
                    if input[1] < 1.8100873:
                        if input[9] < 1.0685052:
                            var66 = 0.24252881
                        else:
                            var66 = 0.062047817
                    else:
                        if input[4] < 0.8088304:
                            var66 = -0.14415412
                        else:
                            var66 = 0.07836054
            else:
                if input[9] < 2.0538783:
                    if input[10] < -0.19680543:
                        if input[0] < -1.2397972:
                            var66 = -0.10433526
                        else:
                            var66 = 0.08437912
                    else:
                        if input[0] < 1.8868077:
                            var66 = -0.062332254
                        else:
                            var66 = 0.2092932
                else:
                    if input[1] < 2.855097:
                        if input[9] < 2.3952672:
                            var66 = -0.056272153
                        else:
                            var66 = -0.24234226
                    else:
                        var66 = 0.08498645
        else:
            if input[7] < 1.542998:
                if input[7] < 0.20974475:
                    if input[0] < 0.7376251:
                        if input[0] < 0.064680345:
                            var66 = 0.02654388
                        else:
                            var66 = -0.11922804
                    else:
                        if input[0] < 1.4623349:
                            var66 = 0.17704211
                        else:
                            var66 = -0.05347671
                else:
                    if input[0] < -1.1983852:
                        if input[3] < 0.46102956:
                            var66 = 0.2140726
                        else:
                            var66 = -0.099444136
                    else:
                        if input[3] < 1.1531873:
                            var66 = -0.15847307
                        else:
                            var66 = 0.08881601
            else:
                if input[1] < 1.4300839:
                    var66 = 0.0438284
                else:
                    var66 = 0.24222226
    if input[1] < -0.18493108:
        if input[9] < 0.9676402:
            if input[13] < 1.0:
                if input[0] < 1.141392:
                    if input[0] < 0.8100961:
                        if input[9] < -0.9798294:
                            var67 = -0.08651844
                        else:
                            var67 = -0.006521859
                    else:
                        if input[1] < -0.9449381:
                            var67 = 0.0633096
                        else:
                            var67 = -0.20154813
                else:
                    if input[9] < -1.2669066:
                        var67 = -0.14738527
                    else:
                        if input[8] < -0.013902883:
                            var67 = 0.10903031
                        else:
                            var67 = -0.03202072
            else:
                if input[0] < 1.058568:
                    if input[7] < -1.380174:
                        if input[0] < -0.8981483:
                            var67 = -0.024906082
                        else:
                            var67 = 0.20931415
                    else:
                        if input[7] < 1.0826854:
                            var67 = -0.0154748885
                        else:
                            var67 = 0.1521929
                else:
                    if input[0] < 1.5451589:
                        var67 = -0.22387005
                    else:
                        var67 = -0.0140927555
        else:
            if input[3] < -0.63909185:
                var67 = 0.030516943
            else:
                var67 = -0.2062306
    else:
        if input[13] < 1.0:
            if input[1] < 0.19507243:
                if input[9] < 1.1538525:
                    if input[9] < 0.8590164:
                        if input[0] < 1.7729248:
                            var67 = 0.043429203
                        else:
                            var67 = -0.13476685
                    else:
                        if input[1] < -0.08993021:
                            var67 = 0.05792383
                        else:
                            var67 = -0.15228114
                else:
                    if input[14] < 1.0:
                        if input[6] < 0.97067964:
                            var67 = 0.08756297
                        else:
                            var67 = -0.13530049
                    else:
                        if input[0] < -0.24590954:
                            var67 = 0.023318287
                        else:
                            var67 = 0.27280584
            else:
                if input[7] < 1.6966289:
                    if input[7] < 1.57172:
                        if input[7] < 1.4974321:
                            var67 = 0.001264576
                        else:
                            var67 = -0.12505756
                    else:
                        if input[4] < 0.8088304:
                            var67 = 0.16457234
                        else:
                            var67 = -0.05436715
                else:
                    var67 = -0.21006416
        else:
            if input[7] < 1.2721516:
                if input[8] < -0.02462842:
                    if input[8] < -0.025588525:
                        if input[0] < -0.059555613:
                            var67 = -0.05095505
                        else:
                            var67 = 0.0877958
                    else:
                        var67 = 0.3830873
                else:
                    if input[1] < 0.67007685:
                        if input[3] < 1.6430904:
                            var67 = -0.18840377
                        else:
                            var67 = 0.097435765
                    else:
                        if input[9] < -0.6772345:
                            var67 = -0.19492455
                        else:
                            var67 = 0.09005831
            else:
                if input[7] < 1.6966289:
                    if input[7] < 1.4797068:
                        if input[5] < 0.64104193:
                            var67 = -0.03861174
                        else:
                            var67 = -0.2862304
                    else:
                        if input[14] < 1.0:
                            var67 = -0.20059828
                        else:
                            var67 = 0.009882714
                else:
                    var67 = 0.10070051
    if input[6] < 0.97067964:
        if input[1] < 1.4300839:
            if input[1] < -1.3249416:
                if input[0] < -0.9499133:
                    var68 = -0.12660643
                else:
                    if input[3] < 0.36146417:
                        if input[0] < 0.37527025:
                            var68 = -0.114236474
                        else:
                            var68 = 0.038734004
                    else:
                        if input[11] < 1.0:
                            var68 = 0.25167763
                        else:
                            var68 = 0.0025174096
            else:
                if input[1] < -0.9449381:
                    if input[8] < -0.0227347:
                        if input[7] < 0.7475207:
                            var68 = -0.2695508
                        else:
                            var68 = -0.028802397
                    else:
                        if input[1] < -1.0399389:
                            var68 = -0.113056295
                        else:
                            var68 = 0.2174863
                else:
                    if input[3] < 0.88902324:
                        if input[3] < 0.8348226:
                            var68 = 0.0014772271
                        else:
                            var68 = -0.12860574
                    else:
                        if input[0] < -0.18379156:
                            var68 = 0.081540555
                        else:
                            var68 = -0.012298099
        else:
            if input[0] < -0.22520356:
                if input[1] < 2.4750936:
                    var68 = 0.20827502
                else:
                    var68 = 0.03275096
            else:
                if input[2] < -0.35097063:
                    var68 = 0.14258885
                else:
                    if input[10] < -0.4956756:
                        if input[1] < 1.6200856:
                            var68 = -0.0712265
                        else:
                            var68 = 0.17980643
                    else:
                        if input[0] < 0.7376251:
                            var68 = -0.19486484
                        else:
                            var68 = -0.016398687
    else:
        if input[9] < 0.4943508:
            if input[9] < 0.39348584:
                if input[9] < 0.26934436:
                    if input[9] < 0.16072056:
                        if input[9] < 0.067614436:
                            var68 = -0.0002762771
                        else:
                            var68 = -0.12087765
                    else:
                        if input[14] < 1.0:
                            var68 = -0.012231623
                        else:
                            var68 = 0.24532266
                else:
                    if input[0] < 0.7893901:
                        if input[7] < -1.3359233:
                            var68 = 0.063630186
                        else:
                            var68 = -0.20787121
                    else:
                        if input[14] < 1.0:
                            var68 = -0.12780143
                        else:
                            var68 = 0.14604408
            else:
                if input[14] < 1.0:
                    if input[0] < -0.76355934:
                        var68 = 0.23875459
                    else:
                        if input[3] < 0.92594856:
                            var68 = -0.22794268
                        else:
                            var68 = 0.0590047
                else:
                    if input[3] < 0.5545477:
                        var68 = 0.42655239
                    else:
                        var68 = 0.039764877
        else:
            if input[9] < 0.59521574:
                if input[12] < 1.0:
                    if input[1] < -0.8499372:
                        var68 = -0.04612228
                    else:
                        var68 = -0.29501122
                else:
                    var68 = 0.09799611
            else:
                if input[0] < -0.6703824:
                    if input[0] < -1.0741493:
                        if input[8] < -0.027137408:
                            var68 = -0.095022365
                        else:
                            var68 = 0.13219698
                    else:
                        if input[8] < -0.02124119:
                            var68 = -0.27225325
                        else:
                            var68 = -0.03492694
                else:
                    if input[0] < 0.2510343:
                        if input[8] < -0.024557525:
                            var68 = 0.10917318
                        else:
                            var68 = -0.04698322
                    else:
                        if input[9] < 0.64952767:
                            var68 = 0.18054278
                        else:
                            var68 = -0.05498237
    if input[1] < 3.1400995:
        if input[4] < 2.5279171:
            if input[0] < -1.4365041:
                if input[0] < -1.5503871:
                    if input[9] < 0.20727362:
                        if input[9] < -0.3358454:
                            var69 = -0.040582255
                        else:
                            var69 = 0.14090425
                    else:
                        if input[9] < 0.5796981:
                            var69 = -0.19810893
                        else:
                            var69 = -0.0000886465
                else:
                    if input[9] < -0.94103515:
                        var69 = 0.12548107
                    else:
                        if input[7] < 1.6285735:
                            var69 = -0.21744889
                        else:
                            var69 = 0.084652096
            else:
                if input[1] < 3.0450988:
                    if input[7] < 1.6285735:
                        if input[7] < 1.5997853:
                            var69 = 0.0004606919
                        else:
                            var69 = 0.096487164
                    else:
                        if input[8] < -0.029821312:
                            var69 = -0.0041599106
                        else:
                            var69 = -0.17806648
                else:
                    var69 = 0.12454192
        else:
            if input[1] < 0.3850742:
                if input[1] < 0.10007155:
                    if input[9] < -0.7082699:
                        var69 = 0.1043793
                    else:
                        if input[13] < 1.0:
                            var69 = 0.059421998
                        else:
                            var69 = -0.07793287
                else:
                    if input[0] < -0.4115575:
                        var69 = 0.06140701
                    else:
                        var69 = -0.09390067
            else:
                var69 = 0.12323145
    else:
        if input[0] < -0.3390865:
            var69 = -0.0045063985
        else:
            var69 = -0.13718887
    if input[0] < -2.4407449:
        if input[10] < -0.595299:
            var70 = 0.12849411
        else:
            var70 = 0.011070066
    else:
        if input[0] < -1.923095:
            if input[9] < -0.0022151496:
                if input[9] < -0.3358454:
                    if input[10] < 0.1874562:
                        var70 = -0.19215654
                    else:
                        if input[9] < -1.0419002:
                            var70 = -0.11271199
                        else:
                            var70 = 0.18896562
                else:
                    if input[10] < -0.42926002:
                        var70 = -0.0037997102
                    else:
                        var70 = 0.27699155
            else:
                if input[9] < 0.7659103:
                    if input[3] < -0.63909185:
                        var70 = -0.07385499
                    else:
                        var70 = -0.2560103
                else:
                    if input[8] < -0.026892679:
                        if input[3] < 0.13275805:
                            var70 = -0.14309435
                        else:
                            var70 = -0.03922015
                    else:
                        var70 = 0.10288794
        else:
            if input[0] < -1.87133:
                if input[1] < 0.10007155:
                    var70 = -0.017164292
                else:
                    var70 = 0.17855375
            else:
                if input[1] < 0.67007685:
                    if input[0] < -1.0016782:
                        if input[7] < 1.0982982:
                            var70 = -0.05660132
                        else:
                            var70 = 0.04922532
                    else:
                        if input[0] < -0.7014414:
                            var70 = 0.054121442
                        else:
                            var70 = -0.005670088
                else:
                    if input[9] < 0.64952767:
                        if input[10] < -0.19680543:
                            var70 = 0.08320016
                        else:
                            var70 = -0.004950925
                    else:
                        if input[2] < 1.0299541:
                            var70 = -0.052163728
                        else:
                            var70 = 0.020900778
    if input[9] < 3.3728817:
        if input[7] < -0.44317603:
            if input[7] < -0.4824063:
                if input[7] < -0.51192284:
                    if input[3] < 1.2051187:
                        if input[3] < 1.098279:
                            var71 = 0.007894762
                        else:
                            var71 = 0.13794239
                    else:
                        if input[0] < 0.34421125:
                            var71 = 0.027528547
                        else:
                            var71 = -0.16990344
                else:
                    if input[12] < 1.0:
                        var71 = -0.26978484
                    else:
                        var71 = 0.11022787
            else:
                if input[2] < 1.0299541:
                    if input[3] < 1.1103356:
                        if input[10] < -0.42926002:
                            var71 = 0.35844225
                        else:
                            var71 = 0.10539126
                    else:
                        var71 = -0.08581805
                else:
                    if input[0] < -0.12167359:
                        var71 = 0.03996614
                    else:
                        var71 = -0.28567368
        else:
            if input[7] < -0.3796405:
                if input[13] < 1.0:
                    if input[1] < 0.48007506:
                        if input[3] < -0.63909185:
                            var71 = -0.09889751
                        else:
                            var71 = -0.27244136
                    else:
                        if input[9] < 0.5486627:
                            var71 = 0.13966583
                        else:
                            var71 = -0.13830091
                else:
                    if input[1] < 0.10007155:
                        var71 = -0.052605767
                    else:
                        var71 = 0.18188609
            else:
                if input[7] < -0.3668275:
                    if input[1] < 0.005070672:
                        var71 = 0.3573783
                    else:
                        var71 = -0.00215766
                else:
                    if input[7] < -0.32233608:
                        if input[1] < 0.5750759:
                            var71 = -0.16664806
                        else:
                            var71 = 0.07035729
                    else:
                        if input[8] < -0.022184744:
                            var71 = -0.004562751
                        else:
                            var71 = 0.06627451
    else:
        var71 = -0.110367365
    if input[1] < -1.6099442:
        if input[5] < 0.64104193:
            var72 = 0.024020363
        else:
            var72 = -0.14193857
    else:
        if input[0] < -2.4407449:
            if input[3] < -0.23915213:
                var72 = 0.016789315
            else:
                var72 = 0.111253574
        else:
            if input[0] < -1.923095:
                if input[9] < -0.0022151496:
                    if input[9] < -0.3358454:
                        if input[1] < 0.10007155:
                            var72 = -0.15237455
                        else:
                            var72 = 0.031904396
                    else:
                        if input[10] < -0.42926002:
                            var72 = 0.015730757
                        else:
                            var72 = 0.22990794
                else:
                    if input[9] < 0.928846:
                        if input[0] < -2.140508:
                            var72 = -0.06181148
                        else:
                            var72 = -0.20806965
                    else:
                        if input[8] < -0.029375087:
                            var72 = -0.10929615
                        else:
                            var72 = 0.07458099
            else:
                if input[10] < 2.8915195:
                    if input[7] < -1.4046581:
                        if input[7] < -1.4387897:
                            var72 = -0.011329031
                        else:
                            var72 = -0.14924897
                    else:
                        if input[7] < -1.2378846:
                            var72 = 0.04708601
                        else:
                            var72 = -0.00057608826
                else:
                    if input[7] < -1.050368:
                        var72 = 0.16334268
                    else:
                        if input[12] < 1.0:
                            var72 = 0.052215956
                        else:
                            var72 = -0.08855576
    if input[4] < 2.5279171:
        if input[4] < 0.8088304:
            if input[0] < 1.5762178:
                if input[0] < 1.4623349:
                    if input[7] < 1.0982982:
                        if input[7] < 0.93511486:
                            var73 = 0.002035401
                        else:
                            var73 = -0.123399146
                    else:
                        if input[7] < 1.1680722:
                            var73 = 0.12782875
                        else:
                            var73 = 0.013118828
                else:
                    if input[7] < 0.38036832:
                        if input[3] < 0.5055981:
                            var73 = 0.13176556
                        else:
                            var73 = -0.15439595
                    else:
                        var73 = -0.28024384
            else:
                if input[9] < 0.6572865:
                    if input[7] < -0.9653717:
                        if input[9] < 0.09864981:
                            var73 = 0.22601621
                        else:
                            var73 = -0.027451966
                    else:
                        if input[7] < 0.31350702:
                            var73 = -0.1383487
                        else:
                            var73 = 0.018089112
                else:
                    if input[11] < 1.0:
                        if input[3] < 0.58319753:
                            var73 = -0.088665225
                        else:
                            var73 = 0.1276371
                    else:
                        if input[9] < 1.3400646:
                            var73 = 0.33928403
                        else:
                            var73 = 0.04464989
        else:
            if input[0] < 1.5762178:
                if input[0] < 1.317393:
                    if input[3] < -0.35117662:
                        if input[7] < 1.2331057:
                            var73 = -0.02592833
                        else:
                            var73 = -0.1494128
                    else:
                        if input[7] < 1.57172:
                            var73 = 0.0131099885
                        else:
                            var73 = -0.13306618
                else:
                    if input[7] < 0.3281733:
                        if input[3] < 0.665922:
                            var73 = -0.1666703
                        else:
                            var73 = 0.10843068
                    else:
                        if input[2] < 0.3394917:
                            var73 = 0.3644743
                        else:
                            var73 = 0.09191708
            else:
                if input[0] < 1.9903376:
                    if input[1] < 0.95507944:
                        var73 = -0.24597551
                    else:
                        var73 = -0.05176915
                else:
                    if input[3] < 0.08727838:
                        var73 = 0.11918598
                    else:
                        var73 = -0.07170526
    else:
        if input[8] < -0.028330084:
            if input[7] < -0.5700874:
                var73 = -0.050999034
            else:
                if input[9] < -0.19618623:
                    if input[9] < -0.74706405:
                        if input[11] < 1.0:
                            var73 = -0.0013246578
                        else:
                            var73 = 0.08065914
                    else:
                        var73 = -0.09883644
                else:
                    if input[7] < -0.2725314:
                        var73 = 0.014653298
                    else:
                        var73 = 0.13398056
        else:
            var73 = 0.11699976
    if input[6] < 0.97067964:
        if input[1] < 1.4300839:
            if input[7] < 1.6563303:
                if input[13] < 1.0:
                    if input[7] < -1.5208627:
                        if input[8] < 0.050119616:
                            var74 = -0.21481068
                        else:
                            var74 = -0.008601274
                    else:
                        if input[0] < -0.6289704:
                            var74 = 0.031924162
                        else:
                            var74 = -0.009321042
                else:
                    if input[0] < 0.05432735:
                        if input[7] < 0.22285849:
                            var74 = 0.041507315
                        else:
                            var74 = -0.10884428
                    else:
                        if input[0] < 1.275981:
                            var74 = 0.10621278
                        else:
                            var74 = -0.098106734
            else:
                if input[0] < -0.4115575:
                    if input[0] < -0.5150874:
                        if input[0] < -1.1776792:
                            var74 = 0.08468057
                        else:
                            var74 = -0.21293077
                    else:
                        var74 = 0.25611696
                else:
                    if input[3] < -0.27244106:
                        var74 = -0.027784191
                    else:
                        var74 = -0.18649551
        else:
            if input[0] < -0.22520356:
                if input[0] < -1.2087382:
                    if input[9] < -0.1185978:
                        var74 = -0.05128825
                    else:
                        var74 = 0.11553243
                else:
                    var74 = 0.22241126
            else:
                if input[2] < -0.35097063:
                    var74 = 0.12577987
                else:
                    if input[10] < -0.4956756:
                        if input[1] < 1.6200856:
                            var74 = -0.055049356
                        else:
                            var74 = 0.16274402
                    else:
                        if input[9] < 0.385727:
                            var74 = -0.18485099
                        else:
                            var74 = -0.03492325
    else:
        if input[8] < -0.028158316:
            if input[8] < -0.028330084:
                if input[9] < -0.4599869:
                    if input[10] < 0.1874562:
                        if input[0] < 0.60303617:
                            var74 = 0.17246938
                        else:
                            var74 = -0.054591957
                    else:
                        if input[9] < -1.0419002:
                            var74 = 0.018122213
                        else:
                            var74 = -0.18924142
                else:
                    if input[9] < -0.07980358:
                        if input[8] < -0.029864207:
                            var74 = -0.21674879
                        else:
                            var74 = 0.094885096
                    else:
                        if input[0] < 1.8868077:
                            var74 = -0.009424818
                        else:
                            var74 = 0.20390277
            else:
                if input[7] < 1.2062398:
                    if input[14] < 1.0:
                        var74 = 0.3962107
                    else:
                        var74 = 0.1331926
                else:
                    var74 = -0.044010375
        else:
            if input[8] < -0.027423343:
                if input[7] < 1.1584231:
                    if input[1] < 1.2400821:
                        if input[10] < -0.66645855:
                            var74 = -0.047520597
                        else:
                            var74 = -0.2765545
                    else:
                        if input[14] < 1.0:
                            var74 = 0.14536375
                        else:
                            var74 = -0.0975247
                else:
                    if input[12] < 1.0:
                        var74 = -0.17033693
                    else:
                        var74 = 0.26314273
            else:
                if input[9] < 1.2779939:
                    if input[9] < 1.2081643:
                        if input[0] < -0.22520356:
                            var74 = -0.040665135
                        else:
                            var74 = 0.02156856
                    else:
                        var74 = 0.24222991
                else:
                    if input[10] < -0.66645855:
                        if input[0] < -0.13202658:
                            var74 = 0.061620116
                        else:
                            var74 = -0.08526519
                    else:
                        if input[3] < 0.6206916:
                            var74 = -0.024409922
                        else:
                            var74 = -0.24752091
    if input[1] < 0.3850742:
        if input[1] < 0.19507243:
            if input[8] < -0.026033314:
                if input[1] < 0.10007155:
                    if input[0] < -0.31838053:
                        if input[0] < -0.7532064:
                            var75 = -0.010948524
                        else:
                            var75 = 0.11590355
                    else:
                        if input[1] < -0.08993021:
                            var75 = -0.012993041
                        else:
                            var75 = -0.11202023
                else:
                    if input[8] < -0.028521158:
                        if input[7] < 0.93511486:
                            var75 = 0.10340271
                        else:
                            var75 = -0.12642646
                    else:
                        if input[0] < -1.1259142:
                            var75 = 0.08935303
                        else:
                            var75 = 0.35920677
            else:
                if input[8] < -0.025199242:
                    if input[9] < -1.2358712:
                        var75 = 0.122865625
                    else:
                        if input[7] < 0.9238795:
                            var75 = -0.20056997
                        else:
                            var75 = -0.02041259
                else:
                    if input[0] < -0.24590954:
                        if input[0] < -0.7014414:
                            var75 = -0.0019590699
                        else:
                            var75 = -0.14232042
                    else:
                        if input[3] < 0.36641937:
                            var75 = -0.082983285
                        else:
                            var75 = 0.03273226
        else:
            if input[0] < 0.30279925:
                if input[0] < -0.84638333:
                    if input[0] < -1.0741493:
                        if input[7] < -0.1915065:
                            var75 = 0.12860855
                        else:
                            var75 = -0.19100624
                    else:
                        if input[1] < 0.2900733:
                            var75 = 0.05814255
                        else:
                            var75 = 0.31586874
                else:
                    if input[3] < 1.4464515:
                        if input[0] < -0.54614645:
                            var75 = -0.29446286
                        else:
                            var75 = -0.11206674
                    else:
                        var75 = 0.21207349
            else:
                if input[3] < 0.47638956:
                    if input[10] < -0.19680543:
                        if input[0] < 0.60303617:
                            var75 = -0.015790598
                        else:
                            var75 = 0.3604865
                    else:
                        if input[3] < -0.63909185:
                            var75 = 0.08405179
                        else:
                            var75 = -0.19563982
                else:
                    if input[0] < 0.4477412:
                        var75 = 0.12453614
                    else:
                        if input[5] < 0.64104193:
                            var75 = -0.017374791
                        else:
                            var75 = -0.2588957
    else:
        if input[9] < -0.7703406:
            if input[0] < 1.017156:
                if input[0] < 0.8722141:
                    if input[9] < -1.0806943:
                        if input[7] < 0.19574775:
                            var75 = -0.054072883
                        else:
                            var75 = 0.07412013
                    else:
                        if input[7] < -1.1183978:
                            var75 = 0.22615477
                        else:
                            var75 = 0.049221072
                else:
                    var75 = 0.3459006
            else:
                if input[1] < 0.7650777:
                    if input[3] < 0.6426471:
                        var75 = -0.3077429
                    else:
                        var75 = -0.00058986613
                else:
                    if input[1] < 1.6200856:
                        if input[6] < 0.97067964:
                            var75 = 0.18215314
                        else:
                            var75 = 0.03601574
                    else:
                        var75 = -0.10550036
        else:
            if input[9] < -0.49102226:
                if input[7] < -0.090007216:
                    if input[7] < -1.2938153:
                        if input[14] < 1.0:
                            var75 = 0.14540319
                        else:
                            var75 = -0.11366224
                    else:
                        if input[0] < -0.0077906298:
                            var75 = -0.096203156
                        else:
                            var75 = -0.38492933
                else:
                    if input[1] < 1.2400821:
                        if input[0] < -0.7532064:
                            var75 = 0.08569322
                        else:
                            var75 = -0.12674387
                    else:
                        if input[5] < 0.64104193:
                            var75 = 0.01767704
                        else:
                            var75 = 0.2619972
            else:
                if input[10] < -0.42926002:
                    if input[0] < -1.0741493:
                        if input[0] < -1.7781531:
                            var75 = -0.030716693
                        else:
                            var75 = 0.10369993
                    else:
                        if input[11] < 1.0:
                            var75 = 0.010461202
                        else:
                            var75 = -0.057442307
                else:
                    if input[0] < -1.1052083:
                        if input[7] < 0.4870541:
                            var75 = -0.13817059
                        else:
                            var75 = 0.059086844
                    else:
                        if input[8] < -0.029004993:
                            var75 = -0.019692365
                        else:
                            var75 = 0.10278277
    if input[8] < -0.0054295114:
        if input[8] < -0.006023118:
            if input[7] < -1.5516653:
                if input[7] < -1.6840237:
                    if input[11] < 1.0:
                        var76 = 0.24399576
                    else:
                        var76 = -0.07112859
                else:
                    if input[10] < 0.1874562:
                        var76 = -0.23913759
                    else:
                        if input[7] < -1.6177044:
                            var76 = -0.06339164
                        else:
                            var76 = 0.060737338
            else:
                if input[7] < -1.4953713:
                    if input[6] < 0.97067964:
                        var76 = -0.035361215
                    else:
                        var76 = 0.2561177
                else:
                    if input[7] < -1.4046581:
                        if input[2] < -0.005739468:
                            var76 = -0.06330319
                        else:
                            var76 = -0.24478924
                    else:
                        if input[7] < -1.3645813:
                            var76 = 0.2068809
                        else:
                            var76 = 0.0013829542
        else:
            if input[10] < -0.66645855:
                var76 = 0.2627155
            else:
                var76 = 0.01314147
    else:
        if input[8] < -0.0030118448:
            if input[12] < 1.0:
                if input[8] < -0.0046383874:
                    var76 = -0.036146663
                else:
                    var76 = -0.2579082
            else:
                var76 = 0.018953934
        else:
            if input[3] < 1.6430904:
                if input[9] < 1.821113:
                    if input[9] < 0.02106138:
                        if input[9] < -0.16515085:
                            var76 = -0.02033976
                        else:
                            var76 = 0.17344707
                    else:
                        if input[10] < -0.761338:
                            var76 = 0.037541933
                        else:
                            var76 = -0.12351839
                else:
                    if input[9] < 2.3952672:
                        if input[7] < -1.3192986:
                            var76 = 0.20453566
                        else:
                            var76 = 0.01838231
                    else:
                        var76 = -0.02312131
            else:
                if input[7] < -1.3495861:
                    var76 = -0.0009644164
                else:
                    var76 = 0.24373926
    if input[1] < -0.18493108:
        if input[9] < 0.9676402:
            if input[9] < 0.9055695:
                if input[3] < 1.2371876:
                    if input[3] < 1.13005:
                        if input[9] < -1.049659:
                            var77 = -0.05878376
                        else:
                            var77 = -0.00021781154
                    else:
                        if input[9] < -1.2358712:
                            var77 = 0.10098413
                        else:
                            var77 = -0.21235526
                else:
                    if input[3] < 1.4322927:
                        if input[7] < -1.2830763:
                            var77 = 0.32545084
                        else:
                            var77 = 0.050855275
                    else:
                        if input[12] < 1.0:
                            var77 = 0.010129365
                        else:
                            var77 = -0.15835127
            else:
                if input[12] < 1.0:
                    var77 = -0.052642908
                else:
                    var77 = 0.19366701
        else:
            if input[3] < -0.63909185:
                var77 = 0.026718598
            else:
                var77 = -0.1818313
    else:
        if input[13] < 1.0:
            if input[10] < 0.89905185:
                if input[10] < 0.10206473:
                    if input[7] < 1.1584231:
                        if input[7] < 1.0173054:
                            var77 = 0.0045878086
                        else:
                            var77 = -0.14918527
                    else:
                        if input[7] < 1.223257:
                            var77 = 0.1788226
                        else:
                            var77 = 0.026999332
                else:
                    if input[1] < 0.2900733:
                        if input[3] < 0.9126434:
                            var77 = 0.21081553
                        else:
                            var77 = -0.081537895
                    else:
                        if input[0] < 1.006803:
                            var77 = 0.03972313
                        else:
                            var77 = -0.14243984
            else:
                if input[0] < -0.30802754:
                    if input[9] < -1.1738005:
                        if input[11] < 1.0:
                            var77 = -0.01800151
                        else:
                            var77 = -0.25196144
                    else:
                        if input[10] < 1.1481103:
                            var77 = -0.1299822
                        else:
                            var77 = 0.079754405
                else:
                    if input[0] < 1.0792739:
                        if input[2] < -1.3866642:
                            var77 = 0.15495929
                        else:
                            var77 = -0.023423804
                    else:
                        if input[0] < 1.317393:
                            var77 = -0.23333211
                        else:
                            var77 = -0.025805825
        else:
            if input[3] < 0.32362035:
                if input[8] < -0.032779966:
                    if input[0] < 0.62374216:
                        if input[0] < 0.17856331:
                            var77 = -0.029932668
                        else:
                            var77 = -0.18279272
                    else:
                        if input[1] < 0.19507243:
                            var77 = -0.13886118
                        else:
                            var77 = 0.13875072
                else:
                    if input[1] < 0.48007506:
                        if input[0] < 0.4063292:
                            var77 = 0.29614583
                        else:
                            var77 = -0.05370183
                    else:
                        if input[2] < 1.0299541:
                            var77 = -0.092076235
                        else:
                            var77 = 0.19925123
            else:
                if input[1] < 1.1450812:
                    if input[3] < 0.94771826:
                        if input[1] < 0.67007685:
                            var77 = -0.23527823
                        else:
                            var77 = -0.032595754
                    else:
                        if input[9] < -0.6229226:
                            var77 = 0.13334854
                        else:
                            var77 = -0.08668113
                else:
                    if input[9] < 1.9762899:
                        if input[10] < -0.19680543:
                            var77 = 0.23319088
                        else:
                            var77 = -0.0012334381
                    else:
                        if input[8] < -0.025015872:
                            var77 = -0.15484239
                        else:
                            var77 = 0.032538515
    if input[6] < 0.97067964:
        if input[1] < 1.4300839:
            if input[0] < 0.37527025:
                if input[0] < 0.33385825:
                    if input[8] < -0.02895312:
                        if input[9] < -1.142765:
                            var78 = -0.16253704
                        else:
                            var78 = -0.008324604
                    else:
                        if input[9] < 1.2159232:
                            var78 = 0.0029000489
                        else:
                            var78 = 0.09264329
                else:
                    if input[7] < -0.4678239:
                        var78 = 0.06648944
                    else:
                        if input[8] < -0.028128527:
                            var78 = -0.29795113
                        else:
                            var78 = 0.013006615
            else:
                if input[0] < 0.4477412:
                    if input[9] < -0.14963317:
                        if input[3] < 0.77152056:
                            var78 = 0.28970638
                        else:
                            var78 = -0.010779882
                    else:
                        if input[9] < 0.385727:
                            var78 = -0.20450647
                        else:
                            var78 = 0.1087669
                else:
                    if input[0] < 0.5512712:
                        if input[9] < -0.27377465:
                            var78 = -0.19881822
                        else:
                            var78 = -0.019809218
                    else:
                        if input[7] < -1.5516653:
                            var78 = -0.16103972
                        else:
                            var78 = 0.02888969
        else:
            if input[3] < 0.8941428:
                if input[1] < 2.855097:
                    if input[0] < 0.29244626:
                        if input[9] < 2.2866435:
                            var78 = 0.21109264
                        else:
                            var78 = 0.037861153
                    else:
                        if input[3] < 0.5495229:
                            var78 = 0.108760506
                        else:
                            var78 = -0.062196996
                else:
                    var78 = -0.061988696
            else:
                if input[3] < 0.9687012:
                    var78 = -0.19865738
                else:
                    var78 = 0.111265704
    else:
        if input[3] < 1.4322927:
            if input[7] < 1.6966289:
                if input[7] < 1.6715614:
                    if input[1] < -1.2299408:
                        if input[0] < -0.059555613:
                            var78 = 0.006801511
                        else:
                            var78 = -0.2222489
                    else:
                        if input[13] < 1.0:
                            var78 = 0.00554174
                        else:
                            var78 = -0.032148413
                else:
                    var78 = -0.19859354
            else:
                if input[1] < -0.18493108:
                    var78 = -0.043816075
                else:
                    if input[9] < -0.3513631:
                        var78 = 0.28209195
                    else:
                        var78 = 0.005618425
        else:
            if input[1] < -0.8499372:
                if input[3] < 1.6893907:
                    var78 = -0.07307097
                else:
                    var78 = 0.19235146
            else:
                if input[8] < -0.025742803:
                    if input[0] < 0.2096223:
                        var78 = -0.06749355
                    else:
                        var78 = 0.1260747
                else:
                    if input[11] < 1.0:
                        var78 = -0.23873964
                    else:
                        if input[7] < -0.58626974:
                            var78 = 0.02944241
                        else:
                            var78 = -0.14687312
    if input[4] < 2.5279171:
        if input[9] < 2.5349264:
            if input[9] < 2.2866435:
                if input[1] < 3.1400995:
                    if input[9] < 2.2090552:
                        if input[9] < 1.6969715:
                            var79 = -0.0025725693
                        else:
                            var79 = 0.030720655
                    else:
                        if input[11] < 1.0:
                            var79 = -0.153099
                        else:
                            var79 = -0.012419565
                else:
                    var79 = -0.12730512
            else:
                if input[8] < -0.02587994:
                    if input[7] < 0.5360101:
                        var79 = -0.14653039
                    else:
                        var79 = 0.12900238
                else:
                    if input[3] < 0.671927:
                        var79 = 0.20078488
                    else:
                        var79 = 0.02573889
        else:
            if input[0] < -0.16308558:
                if input[7] < 0.30071127:
                    var79 = 0.10565581
                else:
                    if input[10] < -0.761338:
                        var79 = -0.09793975
                    else:
                        var79 = 0.0035696789
            else:
                if input[7] < -0.114853054:
                    var79 = -0.17331065
                else:
                    if input[11] < 1.0:
                        var79 = 0.07146942
                    else:
                        var79 = -0.102223754
    else:
        if input[1] < 0.2900733:
            if input[1] < 0.10007155:
                if input[9] < -0.7082699:
                    var79 = 0.10354111
                else:
                    if input[13] < 1.0:
                        var79 = 0.04336686
                    else:
                        var79 = -0.0604786
            else:
                var79 = -0.039915327
        else:
            if input[1] < 1.1450812:
                var79 = 0.12704764
            else:
                var79 = 0.025767952
    if input[1] < 2.5700943:
        if input[3] < -0.3058544:
            if input[8] < -0.032208994:
                if input[1] < 0.7650777:
                    if input[1] < 0.67007685:
                        if input[9] < -0.27377465:
                            var80 = 0.0298544
                        else:
                            var80 = -0.019865608
                    else:
                        if input[0] < -1.0430902:
                            var80 = 0.056270417
                        else:
                            var80 = -0.17358318
                else:
                    if input[0] < -1.705682:
                        var80 = -0.1755005
                    else:
                        if input[1] < 2.0000892:
                            var80 = 0.07823764
                        else:
                            var80 = -0.07133927
            else:
                if input[7] < -0.24950548:
                    if input[7] < -1.0203258:
                        var80 = 0.09628876
                    else:
                        var80 = -0.14752747
                else:
                    if input[8] < -0.031374626:
                        var80 = 0.043143395
                    else:
                        var80 = 0.3500246
        else:
            if input[3] < -0.19682488:
                if input[13] < 1.0:
                    if input[7] < 0.8511328:
                        var80 = -0.27466166
                    else:
                        var80 = -0.05218369
                else:
                    if input[9] < 0.3158974:
                        var80 = -0.06584059
                    else:
                        var80 = 0.15465759
            else:
                if input[3] < -0.13747577:
                    if input[9] < -0.52205765:
                        var80 = -0.07996121
                    else:
                        if input[7] < -0.35611662:
                            var80 = 0.27755734
                        else:
                            var80 = 0.054514352
                else:
                    if input[8] < -0.031136286:
                        if input[10] < -0.34624052:
                            var80 = -0.21587168
                        else:
                            var80 = 0.026832793
                    else:
                        if input[8] < -0.030960822:
                            var80 = 0.12320384
                        else:
                            var80 = -0.0030421584
    else:
        if input[3] < 0.94295037:
            if input[0] < -1.2397972:
                var80 = 0.03787136
            else:
                if input[3] < 0.5229495:
                    var80 = -0.1755783
                else:
                    if input[12] < 1.0:
                        var80 = -0.0932222
                    else:
                        var80 = 0.03608962
        else:
            var80 = 0.082859285
    if input[0] < -2.306156:
        if input[4] < 0.8088304:
            if input[7] < -0.3796405:
                var81 = -0.003503383
            else:
                var81 = 0.18307605
        else:
            var81 = -0.079129934
    else:
        if input[0] < -1.923095:
            if input[3] < 1.0062785:
                if input[7] < -0.40280506:
                    if input[5] < 0.64104193:
                        var81 = -0.047400683
                    else:
                        var81 = 0.17233524
                else:
                    if input[2] < 0.3394917:
                        if input[14] < 1.0:
                            var81 = -0.17676128
                        else:
                            var81 = -0.03506019
                    else:
                        if input[9] < 0.59521574:
                            var81 = 0.19651665
                        else:
                            var81 = -0.08832263
            else:
                var81 = -0.18377395
        else:
            if input[0] < -1.87133:
                if input[1] < 0.10007155:
                    var81 = -0.001938346
                else:
                    var81 = 0.15737846
            else:
                if input[1] < 3.1400995:
                    if input[4] < 2.5279171:
                        if input[1] < -1.4199425:
                            var81 = -0.04685837
                        else:
                            var81 = -0.00034791668
                    else:
                        if input[1] < -0.5649346:
                            var81 = -0.007530899
                        else:
                            var81 = 0.07162665
                else:
                    var81 = -0.08943917
    if input[6] < 0.97067964:
        if input[1] < 2.0000892:
            if input[1] < -1.3249416:
                if input[0] < -0.9499133:
                    var82 = -0.10174254
                else:
                    if input[8] < -0.0280959:
                        if input[8] < -0.029212695:
                            var82 = 0.035543673
                        else:
                            var82 = -0.085408255
                    else:
                        if input[0] < 0.8722141:
                            var82 = 0.19557154
                        else:
                            var82 = 0.024407875
            else:
                if input[1] < -0.9449381:
                    if input[8] < -0.0227347:
                        if input[7] < 0.7475207:
                            var82 = -0.24831049
                        else:
                            var82 = -0.018756593
                    else:
                        if input[1] < -1.0399389:
                            var82 = -0.09966274
                        else:
                            var82 = 0.15178618
                else:
                    if input[3] < 0.25296:
                        if input[8] < -0.029662345:
                            var82 = 0.0051303115
                        else:
                            var82 = 0.09963666
                    else:
                        if input[3] < 0.5637478:
                            var82 = -0.05193593
                        else:
                            var82 = 0.010177601
        else:
            if input[1] < 2.760096:
                if input[4] < 0.8088304:
                    var82 = 0.17527734
                else:
                    var82 = 0.027829548
            else:
                var82 = -0.01335243
    else:
        if input[8] < 0.27596393:
            if input[7] < -1.6440885:
                if input[9] < -0.8401702:
                    var82 = -0.0139805805
                else:
                    var82 = -0.20613076
            else:
                if input[9] < 2.0538783:
                    if input[9] < 1.6969715:
                        if input[9] < 1.4874827:
                            var82 = -0.003009558
                        else:
                            var82 = -0.10410067
                    else:
                        if input[3] < 0.44567034:
                            var82 = -0.0815337
                        else:
                            var82 = 0.1561813
                else:
                    if input[3] < -0.16907157:
                        if input[7] < 0.08701753:
                            var82 = -0.08149916
                        else:
                            var82 = 0.11163158
                    else:
                        if input[9] < 2.2866435:
                            var82 = -0.22815932
                        else:
                            var82 = -0.032579318
        else:
            if input[10] < -0.42926002:
                var82 = 0.020536557
            else:
                var82 = 0.1826317
    if input[8] < -0.0054295114:
        if input[8] < -0.006023118:
            if input[7] < -1.6840237:
                if input[9] < 0.059855595:
                    var83 = 0.0012896352
                else:
                    var83 = 0.17979544
            else:
                if input[7] < -1.5516653:
                    if input[9] < -1.2125946:
                        var83 = 0.049071435
                    else:
                        if input[2] < -0.005739468:
                            var83 = -0.07962904
                        else:
                            var83 = -0.23331176
                else:
                    if input[7] < -1.4953713:
                        if input[6] < 0.97067964:
                            var83 = -0.031335555
                        else:
                            var83 = 0.204733
                    else:
                        if input[7] < -1.4046581:
                            var83 = -0.17351764
                        else:
                            var83 = 0.0016857792
        else:
            if input[10] < -0.66645855:
                var83 = 0.22631268
            else:
                var83 = 0.007224156
    else:
        if input[7] < -1.2378846:
            if input[7] < -1.2938153:
                if input[0] < 1.275981:
                    if input[3] < 0.7339476:
                        if input[3] < 0.7186383:
                            var83 = -0.0034537644
                        else:
                            var83 = 0.27395302
                    else:
                        if input[7] < -1.4665563:
                            var83 = -0.0014609515
                        else:
                            var83 = -0.18927799
                else:
                    if input[3] < 0.5010245:
                        var83 = -0.06912585
                    else:
                        if input[9] < -0.63068146:
                            var83 = -0.018183334
                        else:
                            var83 = 0.2197096
            else:
                if input[7] < -1.2830763:
                    var83 = 0.32043144
                else:
                    if input[4] < 0.8088304:
                        if input[0] < 0.39597622:
                            var83 = -0.06000774
                        else:
                            var83 = 0.15406053
                    else:
                        var83 = -0.13068983
        else:
            if input[3] < 1.6430904:
                if input[10] < -0.761338:
                    if input[8] < -0.0030118448:
                        var83 = -0.07856144
                    else:
                        var83 = 0.14262506
                else:
                    if input[9] < -1.049659:
                        var83 = -0.0006955502
                    else:
                        if input[7] < -1.1486096:
                            var83 = -0.29983392
                        else:
                            var83 = -0.08568457
            else:
                var83 = 0.14528134
    if input[4] < 2.5279171:
        if input[1] < -1.6099442:
            if input[5] < 0.64104193:
                var84 = 0.022536658
            else:
                var84 = -0.13033763
        else:
            if input[7] < 1.6966289:
                if input[7] < 1.6563303:
                    if input[9] < 2.5349264:
                        if input[9] < 2.2866435:
                            var84 = -0.0001691749
                        else:
                            var84 = 0.06636039
                    else:
                        if input[0] < -0.16308558:
                            var84 = 0.0105284825
                        else:
                            var84 = -0.10510742
                else:
                    if input[10] < -0.34624052:
                        if input[1] < 0.2900733:
                            var84 = -0.23785727
                        else:
                            var84 = -0.05749878
                    else:
                        if input[3] < 0.60240114:
                            var84 = -0.13487168
                        else:
                            var84 = 0.18754087
            else:
                if input[4] < 0.8088304:
                    if input[0] < 0.94468504:
                        if input[7] < 1.7370887:
                            var84 = 0.20009406
                        else:
                            var84 = -0.049560387
                    else:
                        var84 = -0.11648944
                else:
                    var84 = -0.16258079
    else:
        if input[0] < -0.8774423:
            var84 = 0.11041276
        else:
            if input[0] < -0.58755845:
                var84 = -0.080374405
            else:
                if input[7] < -0.32233608:
                    if input[7] < -1.1768137:
                        var84 = 0.0028181481
                    else:
                        var84 = 0.12682459
                else:
                    if input[7] < 0.19574775:
                        var84 = -0.09602991
                    else:
                        if input[7] < 1.1680722:
                            var84 = 0.08385472
                        else:
                            var84 = -0.009877536
    if input[0] < -2.4407449:
        var85 = 0.07524731
    else:
        if input[1] < 3.1400995:
            if input[7] < 1.4797068:
                if input[7] < 1.3909004:
                    if input[7] < 1.376414:
                        if input[7] < 1.3543655:
                            var85 = -0.00039557813
                        else:
                            var85 = 0.07925099
                    else:
                        if input[11] < 1.0:
                            var85 = -0.20617457
                        else:
                            var85 = 0.012690802
                else:
                    if input[1] < -0.46993372:
                        if input[0] < -0.16308558:
                            var85 = 0.3239889
                        else:
                            var85 = -0.121647514
                    else:
                        if input[0] < -1.0016782:
                            var85 = -0.21446426
                        else:
                            var85 = 0.053203486
            else:
                if input[1] < -0.6599355:
                    if input[7] < 1.7107749:
                        if input[7] < 1.542998:
                            var85 = -0.022892985
                        else:
                            var85 = -0.21860698
                    else:
                        var85 = 0.032263577
                else:
                    if input[9] < -0.74706405:
                        if input[0] < 0.116445325:
                            var85 = 0.16110432
                        else:
                            var85 = -0.035761893
                    else:
                        if input[0] < 0.095739335:
                            var85 = -0.09301802
                        else:
                            var85 = 0.052994072
        else:
            var85 = -0.08134512
    if input[8] < -0.028794577:
        if input[10] < 1.8952857:
            if input[5] < 0.64104193:
                if input[2] < 1.3751853:
                    if input[9] < 0.7659103:
                        if input[9] < -1.0419002:
                            var86 = 0.17828915
                        else:
                            var86 = 0.02416956
                    else:
                        if input[3] < -0.13747577:
                            var86 = 0.23250887
                        else:
                            var86 = 0.025891976
                else:
                    if input[6] < 0.97067964:
                        if input[14] < 1.0:
                            var86 = -0.09004879
                        else:
                            var86 = 0.100398675
                    else:
                        if input[7] < 1.2062398:
                            var86 = -0.20435737
                        else:
                            var86 = 0.03311501
            else:
                if input[3] < 0.5495229:
                    if input[7] < 0.8763027:
                        if input[0] < -0.78426534:
                            var86 = -0.065260336
                        else:
                            var86 = 0.03516195
                    else:
                        if input[0] < -1.1259142:
                            var86 = 0.08527147
                        else:
                            var86 = -0.09701919
                else:
                    if input[7] < 1.0982982:
                        var86 = 0.36233664
                    else:
                        if input[11] < 1.0:
                            var86 = 0.10517852
                        else:
                            var86 = -0.12254458
        else:
            if input[5] < 0.64104193:
                if input[1] < 0.19507243:
                    var86 = -0.21584947
                else:
                    if input[0] < 0.32350525:
                        var86 = -0.08346905
                    else:
                        var86 = 0.03231191
            else:
                if input[2] < -1.3866642:
                    if input[3] < 0.21962981:
                        if input[0] < 0.37527025:
                            var86 = 0.023849327
                        else:
                            var86 = 0.22696923
                    else:
                        var86 = -0.11435037
                else:
                    if input[13] < 1.0:
                        var86 = -0.1898537
                    else:
                        var86 = 0.016424607
    else:
        if input[8] < -0.0287114:
            if input[9] < 0.6572865:
                var86 = -0.22577377
            else:
                var86 = 0.021133224
        else:
            if input[3] < 0.43356293:
                if input[7] < 0.47282687:
                    if input[6] < 0.97067964:
                        if input[9] < -0.9798294:
                            var86 = -0.1361596
                        else:
                            var86 = 0.03352525
                    else:
                        if input[9] < 0.8590164:
                            var86 = -0.020263886
                        else:
                            var86 = -0.20099019
                else:
                    var86 = -0.23094936
            else:
                if input[3] < 0.5545477:
                    if input[1] < 1.0500803:
                        if input[11] < 1.0:
                            var86 = 0.061322067
                        else:
                            var86 = -0.10096962
                    else:
                        if input[2] < -0.005739468:
                            var86 = 0.05889053
                        else:
                            var86 = 0.3532682
                else:
                    if input[2] < -1.041433:
                        if input[3] < 1.2936667:
                            var86 = 0.070400424
                        else:
                            var86 = -0.121582285
                    else:
                        if input[9] < -0.8944821:
                            var86 = -0.110098965
                        else:
                            var86 = -0.0043928544
    if input[4] < 2.5279171:
        if input[4] < 0.8088304:
            if input[0] < 1.5762178:
                if input[0] < 1.4623349:
                    if input[7] < 1.2062398:
                        if input[7] < 1.1680722:
                            var87 = -0.00042804066
                        else:
                            var87 = -0.21569635
                    else:
                        if input[7] < 1.223257:
                            var87 = 0.25464845
                        else:
                            var87 = 0.018522428
                else:
                    if input[7] < 0.38036832:
                        if input[3] < 0.5055981:
                            var87 = 0.0820899
                        else:
                            var87 = -0.12846692
                    else:
                        var87 = -0.2371944
            else:
                if input[3] < 0.37825713:
                    if input[1] < 0.10007155:
                        if input[7] < -0.9653717:
                            var87 = 0.15622611
                        else:
                            var87 = -0.19703256
                    else:
                        if input[7] < -0.90622854:
                            var87 = -0.00009974383
                        else:
                            var87 = 0.25774848
                else:
                    if input[6] < 0.97067964:
                        if input[3] < 1.0372064:
                            var87 = -0.005304616
                        else:
                            var87 = 0.21283367
                    else:
                        if input[1] < 1.0500803:
                            var87 = -0.15742882
                        else:
                            var87 = 0.066329926
        else:
            if input[0] < 1.5762178:
                if input[3] < 1.2371876:
                    if input[3] < 1.1227999:
                        if input[3] < 1.0842971:
                            var87 = -0.009240029
                        else:
                            var87 = 0.22028877
                    else:
                        var87 = -0.26558912
                else:
                    if input[3] < 1.3814396:
                        if input[9] < 0.69608074:
                            var87 = 0.24784972
                        else:
                            var87 = -0.033054844
                    else:
                        if input[12] < 1.0:
                            var87 = 0.06258529
                        else:
                            var87 = -0.20661455
            else:
                if input[0] < 1.9903376:
                    var87 = -0.20561676
                else:
                    if input[3] < -0.11640179:
                        var87 = 0.07388773
                    else:
                        var87 = -0.07244269
    else:
        if input[0] < -0.8774423:
            var87 = 0.10620317
        else:
            if input[0] < -0.58755845:
                var87 = -0.05167755
            else:
                if input[7] < -0.32233608:
                    if input[7] < -1.1768137:
                        var87 = -0.0009530788
                    else:
                        var87 = 0.10768796
                else:
                    if input[7] < 0.36911884:
                        var87 = -0.074078545
                    else:
                        if input[9] < -0.6772345:
                            var87 = -0.007708382
                        else:
                            var87 = 0.082046986
    if input[9] < 3.3728817:
        if input[1] < -0.18493108:
            if input[9] < 0.9676402:
                if input[9] < 0.9055695:
                    if input[8] < 0.5748285:
                        if input[7] < -1.6840237:
                            var88 = 0.12672746
                        else:
                            var88 = -0.007086222
                    else:
                        var88 = -0.17126039
                else:
                    if input[12] < 1.0:
                        var88 = -0.022661151
                    else:
                        var88 = 0.15827015
            else:
                if input[11] < 1.0:
                    var88 = -0.1629763
                else:
                    var88 = 0.029513191
        else:
            if input[3] < 1.195201:
                if input[3] < 1.0757194:
                    if input[3] < 1.0123969:
                        if input[12] < 1.0:
                            var88 = -0.006197746
                        else:
                            var88 = 0.026963416
                    else:
                        if input[10] < -0.595299:
                            var88 = 0.036171366
                        else:
                            var88 = -0.15370683
                else:
                    if input[1] < 0.7650777:
                        if input[0] < 0.57197714:
                            var88 = 0.17521212
                        else:
                            var88 = -0.041853365
                    else:
                        if input[0] < 0.05432735:
                            var88 = -0.13797735
                        else:
                            var88 = 0.12682177
            else:
                if input[1] < -0.08993021:
                    var88 = -0.22941865
                else:
                    if input[3] < 1.2371876:
                        if input[0] < -0.7532064:
                            var88 = 0.109522626
                        else:
                            var88 = -0.20033894
                    else:
                        if input[0] < 0.5098592:
                            var88 = -0.024564857
                        else:
                            var88 = 0.100627065
    else:
        var88 = -0.08464595
    if input[8] < -0.030154988:
        if input[3] < 0.39631158:
            if input[1] < 2.0000892:
                if input[1] < 1.8100873:
                    if input[8] < -0.030248145:
                        if input[7] < -1.4046581:
                            var89 = -0.056728415
                        else:
                            var89 = 0.009595058
                    else:
                        var89 = -0.16545969
                else:
                    if input[10] < -0.42926002:
                        var89 = 0.01812891
                    else:
                        var89 = 0.33216906
            else:
                if input[6] < 0.97067964:
                    var89 = 0.044011086
                else:
                    if input[14] < 1.0:
                        var89 = -0.034661535
                    else:
                        var89 = -0.20160604
        else:
            if input[7] < 1.542998:
                var89 = 0.25201067
            else:
                if input[12] < 1.0:
                    var89 = -0.13457586
                else:
                    var89 = 0.115871005
    else:
        if input[8] < -0.029952338:
            if input[4] < 0.8088304:
                if input[9] < 0.69608074:
                    var89 = -0.28114173
                else:
                    var89 = -0.03343267
            else:
                if input[7] < 1.2604674:
                    var89 = 0.10286404
                else:
                    var89 = -0.021390662
        else:
            if input[8] < -0.029821312:
                if input[0] < -0.3908515:
                    var89 = -0.12418567
                else:
                    if input[0] < 0.04397435:
                        var89 = 0.042356096
                    else:
                        if input[0] < 1.006803:
                            var89 = 0.30784586
                        else:
                            var89 = 0.058968917
            else:
                if input[7] < 1.6285735:
                    if input[3] < -0.19682488:
                        if input[8] < -0.019090505:
                            var89 = -0.14772472
                        else:
                            var89 = 0.07789934
                    else:
                        if input[3] < -0.13747577:
                            var89 = 0.16883393
                        else:
                            var89 = -0.0023089463
                else:
                    if input[0] < -0.7325004:
                        var89 = -0.02542658
                    else:
                        var89 = -0.19463849
    if input[0] < -0.12167359:
        if input[3] < 1.3683784:
            if input[0] < -0.16308558:
                if input[1] < -1.4199425:
                    if input[7] < 0.8219023:
                        var90 = -0.16741443
                    else:
                        var90 = -0.000928142
                else:
                    if input[1] < -1.3249416:
                        if input[0] < -0.80497134:
                            var90 = 0.013071815
                        else:
                            var90 = 0.24423696
                    else:
                        if input[9] < 1.6969715:
                            var90 = 0.000799757
                        else:
                            var90 = 0.05962422
            else:
                if input[3] < 0.5229495:
                    if input[7] < -0.704771:
                        var90 = 0.13720354
                    else:
                        var90 = -0.18567786
                else:
                    if input[1] < 0.7650777:
                        if input[4] < 0.8088304:
                            var90 = 0.14382888
                        else:
                            var90 = -0.097101815
                    else:
                        var90 = 0.31235558
        else:
            if input[11] < 1.0:
                if input[8] < -0.0039396794:
                    if input[8] < -0.026213264:
                        var90 = 0.012768376
                    else:
                        if input[5] < 0.64104193:
                            var90 = -0.0695279
                        else:
                            var90 = -0.27538726
                else:
                    var90 = 0.058180775
            else:
                if input[0] < -0.49438146:
                    if input[7] < 0.2508246:
                        if input[0] < -1.0741493:
                            var90 = 0.11522486
                        else:
                            var90 = -0.11658831
                    else:
                        if input[0] < -1.1259142:
                            var90 = 0.024945006
                        else:
                            var90 = 0.19943042
                else:
                    var90 = -0.1351427
    else:
        if input[0] < -0.10096759:
            if input[3] < 0.8668733:
                var90 = -0.26388037
            else:
                var90 = 0.053084355
        else:
            if input[1] < -1.5149434:
                if input[14] < 1.0:
                    var90 = 0.17849424
                else:
                    var90 = -0.022185236
            else:
                if input[3] < 1.354722:
                    if input[3] < 1.1873089:
                        if input[3] < 1.1172676:
                            var90 = -0.0059917914
                        else:
                            var90 = 0.07914491
                    else:
                        if input[0] < 0.56162417:
                            var90 = -0.16966042
                        else:
                            var90 = -0.0056542917
                else:
                    if input[9] < 0.4400389:
                        if input[9] < 0.036579065:
                            var90 = 0.035210393
                        else:
                            var90 = 0.20454915
                    else:
                        if input[3] < 1.7584945:
                            var90 = -0.12579137
                        else:
                            var90 = 0.06996367
    if input[1] < 1.1450812:
        if input[1] < 0.3850742:
            if input[7] < -1.0354191:
                if input[9] < -1.1272473:
                    if input[5] < 0.64104193:
                        if input[3] < 0.58319753:
                            var91 = 0.25296915
                        else:
                            var91 = 0.021105055
                    else:
                        if input[3] < 0.5895688:
                            var91 = -0.085119836
                        else:
                            var91 = 0.11313744
                else:
                    if input[9] < -0.18066853:
                        if input[8] < 0.0009902425:
                            var91 = -0.20151244
                        else:
                            var91 = -0.033968557
                    else:
                        if input[9] < 0.5098685:
                            var91 = 0.057537716
                        else:
                            var91 = -0.06741632
            else:
                if input[8] < -0.016679041:
                    if input[8] < -0.017604362:
                        if input[7] < -0.9653717:
                            var91 = 0.16458915
                        else:
                            var91 = -0.0028181393
                    else:
                        if input[10] < -0.595299:
                            var91 = -0.032465074
                        else:
                            var91 = -0.23993205
                else:
                    if input[0] < 0.4063292:
                        if input[0] < -0.3597925:
                            var91 = -0.0009153645
                        else:
                            var91 = 0.2295162
                    else:
                        if input[7] < -0.82613385:
                            var91 = -0.18099904
                        else:
                            var91 = 0.09008286
        else:
            if input[0] < 0.27174026:
                if input[3] < 1.3407071:
                    if input[0] < -0.3390865:
                        if input[0] < -0.6496764:
                            var91 = 0.046458803
                        else:
                            var91 = -0.05785959
                    else:
                        if input[3] < 0.5010245:
                            var91 = 0.16445416
                        else:
                            var91 = 0.04274017
                else:
                    if input[8] < -0.0030118448:
                        if input[10] < -0.71982825:
                            var91 = 0.0072755665
                        else:
                            var91 = -0.22059889
                    else:
                        var91 = 0.075250514
            else:
                if input[7] < 0.08701753:
                    if input[7] < -0.29495046:
                        if input[7] < -0.52951545:
                            var91 = 0.027055603
                        else:
                            var91 = -0.13565552
                    else:
                        if input[10] < -0.66645855:
                            var91 = -0.024604214
                        else:
                            var91 = 0.21246482
                else:
                    if input[10] < -0.19680543:
                        if input[2] < 1.0299541:
                            var91 = -0.21013717
                        else:
                            var91 = -0.042891044
                    else:
                        if input[0] < 0.4995062:
                            var91 = 0.1493767
                        else:
                            var91 = -0.060970444
    else:
        if input[0] < 0.58233017:
            if input[0] < -0.11132059:
                if input[0] < -0.17343858:
                    if input[9] < -1.096212:
                        if input[0] < -0.5564994:
                            var91 = 0.016890077
                        else:
                            var91 = -0.21317871
                    else:
                        if input[8] < 0.0050556543:
                            var91 = 0.015781863
                        else:
                            var91 = -0.14593007
                else:
                    var91 = 0.17162757
            else:
                if input[3] < 1.0172395:
                    if input[7] < 1.2062398:
                        if input[1] < 2.0000892:
                            var91 = -0.21037865
                        else:
                            var91 = -0.012142431
                    else:
                        var91 = 0.022488538
                else:
                    if input[12] < 1.0:
                        var91 = 0.14759694
                    else:
                        var91 = -0.04610708
        else:
            if input[0] < 0.8515081:
                if input[7] < 0.6485844:
                    if input[10] < -0.71982825:
                        var91 = 0.1818868
                    else:
                        if input[8] < -0.024886819:
                            var91 = -0.20493048
                        else:
                            var91 = 0.054614272
                else:
                    if input[7] < 1.1829834:
                        var91 = 0.3055053
                    else:
                        var91 = 0.002895757
            else:
                if input[9] < 0.30037972:
                    if input[9] < -0.6074049:
                        if input[8] < -0.027295405:
                            var91 = -0.13647878
                        else:
                            var91 = 0.06352333
                    else:
                        if input[8] < -0.021049293:
                            var91 = 0.21670385
                        else:
                            var91 = -0.081086345
                else:
                    if input[3] < 0.19976293:
                        var91 = -0.20671435
                    else:
                        if input[3] < 0.6612899:
                            var91 = 0.14442028
                        else:
                            var91 = -0.060038712
    if input[14] < 1.0:
        if input[0] < -1.4882691:
            if input[10] < -0.66645855:
                if input[7] < 0.30071127:
                    if input[9] < 0.9986756:
                        var92 = 0.18470785
                    else:
                        var92 = 0.019351272
                else:
                    var92 = -0.039752066
            else:
                if input[3] < 0.25296:
                    if input[3] < 0.057679754:
                        if input[0] < -1.7781531:
                            var92 = -0.008954382
                        else:
                            var92 = -0.19235495
                    else:
                        var92 = 0.1707874
                else:
                    if input[7] < -0.5700874:
                        if input[6] < 0.97067964:
                            var92 = -0.098866396
                        else:
                            var92 = 0.09822015
                    else:
                        if input[0] < -2.140508:
                            var92 = -0.023978353
                        else:
                            var92 = -0.25445867
        else:
            if input[0] < -1.3536801:
                if input[7] < 1.1680722:
                    if input[9] < 0.533145:
                        if input[7] < 0.618036:
                            var92 = 0.07633193
                        else:
                            var92 = 0.30322763
                    else:
                        var92 = -0.019577965
                else:
                    var92 = -0.09559835
            else:
                if input[7] < -0.86889863:
                    if input[0] < -0.049202614:
                        if input[1] < 0.67007685:
                            var92 = -0.03305105
                        else:
                            var92 = 0.122342736
                    else:
                        if input[9] < -1.1738005:
                            var92 = 0.068423085
                        else:
                            var92 = -0.09881319
                else:
                    if input[7] < -0.811972:
                        if input[2] < 1.0299541:
                            var92 = 0.22724116
                        else:
                            var92 = -0.084502704
                    else:
                        if input[10] < -0.23950118:
                            var92 = 0.013064785
                        else:
                            var92 = -0.03281209
    else:
        if input[7] < 0.54616344:
            if input[7] < -0.0044453996:
                if input[3] < 0.90806395:
                    if input[0] < 0.30279925:
                        if input[0] < 0.28209326:
                            var92 = -0.004737862
                        else:
                            var92 = -0.2567643
                    else:
                        if input[3] < 0.6770472:
                            var92 = 0.038800564
                        else:
                            var92 = 0.22814313
                else:
                    if input[9] < -0.5375753:
                        if input[0] < -0.06990861:
                            var92 = -0.01026461
                        else:
                            var92 = -0.2077865
                    else:
                        if input[2] < 1.0299541:
                            var92 = 0.028884603
                        else:
                            var92 = -0.10288707
            else:
                if input[9] < -0.5608519:
                    if input[3] < 0.75438815:
                        if input[0] < 0.39597622:
                            var92 = 0.14502998
                        else:
                            var92 = -0.045671552
                    else:
                        if input[7] < 0.2887667:
                            var92 = -0.17576176
                        else:
                            var92 = 0.086107776
                else:
                    if input[10] < -0.71982825:
                        if input[3] < 0.4199065:
                            var92 = -0.09421805
                        else:
                            var92 = 0.122474454
                    else:
                        if input[7] < 0.45228475:
                            var92 = -0.09823605
                        else:
                            var92 = -0.30870554
        else:
            if input[9] < -0.801376:
                if input[0] < -0.52544045:
                    if input[0] < -0.7325004:
                        if input[3] < 1.13005:
                            var92 = -0.079585165
                        else:
                            var92 = 0.15962982
                    else:
                        var92 = 0.24488385
                else:
                    if input[9] < -1.2746654:
                        if input[1] < -0.18493108:
                            var92 = -0.11987906
                        else:
                            var92 = 0.10317709
                    else:
                        if input[1] < 0.2900733:
                            var92 = -0.2220184
                        else:
                            var92 = 0.010583398
            else:
                if input[9] < -0.63068146:
                    if input[7] < 0.7595052:
                        var92 = -0.09538508
                    else:
                        if input[7] < 0.8908117:
                            var92 = 0.51970625
                        else:
                            var92 = 0.12059622
                else:
                    if input[7] < 0.5579357:
                        var92 = 0.3665924
                    else:
                        if input[1] < -0.9449381:
                            var92 = 0.13634337
                        else:
                            var92 = 0.0064219357
    if input[6] < 0.97067964:
        if input[1] < 1.4300839:
            if input[9] < 1.6271418:
                if input[9] < 1.4874827:
                    if input[8] < 0.20603855:
                        if input[7] < -1.6840237:
                            var93 = 0.15253901
                        else:
                            var93 = 0.0031474917
                    else:
                        if input[0] < -0.52544045:
                            var93 = 0.13641442
                        else:
                            var93 = -0.2486953
                else:
                    if input[11] < 1.0:
                        if input[4] < 0.8088304:
                            var93 = 0.26437932
                        else:
                            var93 = 0.050425556
                    else:
                        if input[0] < -0.16308558:
                            var93 = -0.12139693
                        else:
                            var93 = 0.12251838
            else:
                if input[9] < 1.6969715:
                    var93 = -0.2238401
                else:
                    if input[0] < -0.0077906298:
                        if input[7] < -0.77200156:
                            var93 = -0.080242105
                        else:
                            var93 = 0.14368463
                    else:
                        if input[1] < 0.8600786:
                            var93 = -0.17001137
                        else:
                            var93 = 0.030672701
        else:
            if input[7] < 1.2988641:
                if input[1] < 2.855097:
                    if input[4] < 0.8088304:
                        if input[1] < 1.6200856:
                            var93 = 0.0029555217
                        else:
                            var93 = 0.21241832
                    else:
                        if input[0] < -0.16308558:
                            var93 = 0.09869472
                        else:
                            var93 = -0.06294765
                else:
                    var93 = -0.025389744
            else:
                var93 = -0.052455578
    else:
        if input[13] < 1.0:
            if input[0] < -0.54614645:
                if input[0] < -0.8774423:
                    if input[7] < -0.5418341:
                        if input[7] < -1.0934299:
                            var93 = -0.027584288
                        else:
                            var93 = 0.19463702
                    else:
                        if input[7] < 0.19574775:
                            var93 = -0.12841965
                        else:
                            var93 = 0.009992874
                else:
                    if input[0] < -0.78426534:
                        var93 = -0.25280264
                    else:
                        if input[9] < -0.19618623:
                            var93 = -0.17438194
                        else:
                            var93 = -0.009612628
            else:
                if input[1] < -1.3249416:
                    var93 = -0.17301464
                else:
                    if input[1] < 1.1450812:
                        if input[1] < 0.8600786:
                            var93 = 0.016264468
                        else:
                            var93 = 0.16011561
                    else:
                        if input[0] < -0.4012045:
                            var93 = 0.11938106
                        else:
                            var93 = -0.055644516
        else:
            if input[0] < -0.0077906298:
                if input[1] < -0.5649346:
                    if input[0] < -1.3122681:
                        var93 = -0.08419213
                    else:
                        if input[8] < -0.02823931:
                            var93 = 0.26185778
                        else:
                            var93 = 0.012398471
                else:
                    if input[9] < -1.2281123:
                        if input[0] < -0.5564994:
                            var93 = 0.23456715
                        else:
                            var93 = -0.020099439
                    else:
                        if input[7] < 0.14232793:
                            var93 = -0.13047825
                        else:
                            var93 = 0.002645258
            else:
                if input[1] < 1.1450812:
                    if input[9] < 0.059855595:
                        if input[3] < 1.26428:
                            var93 = -0.1075284
                        else:
                            var93 = 0.1367726
                    else:
                        var93 = -0.21591987
                else:
                    if input[2] < -0.6962018:
                        var93 = -0.12010492
                    else:
                        if input[2] < 0.68472284:
                            var93 = 0.20879945
                        else:
                            var93 = -0.04372033
    if input[4] < 2.5279171:
        if input[7] < 1.57172:
            if input[7] < 1.4974321:
                if input[1] < 1.7150865:
                    if input[9] < 2.2866435:
                        if input[0] < -1.2708561:
                            var94 = 0.022171615
                        else:
                            var94 = -0.001919707
                    else:
                        if input[13] < 1.0:
                            var94 = 0.13498421
                        else:
                            var94 = -0.076176606
                else:
                    if input[0] < -1.2708561:
                        if input[1] < 2.190091:
                            var94 = -0.18765901
                        else:
                            var94 = -0.023243068
                    else:
                        if input[0] < -1.0741493:
                            var94 = 0.12057852
                        else:
                            var94 = -0.026355868
            else:
                if input[5] < 0.64104193:
                    if input[0] < 0.106092334:
                        var94 = -0.05785765
                    else:
                        var94 = 0.20883988
                else:
                    if input[9] < -0.8634467:
                        var94 = 0.12950224
                    else:
                        if input[12] < 1.0:
                            var94 = -0.2883302
                        else:
                            var94 = -0.06629259
        else:
            if input[1] < -0.6599355:
                if input[7] < 1.7107749:
                    var94 = -0.1619134
                else:
                    var94 = 0.027997598
            else:
                if input[0] < -1.5193281:
                    var94 = -0.08647925
                else:
                    if input[0] < -1.1259142:
                        if input[9] < 0.84349877:
                            var94 = 0.06028234
                        else:
                            var94 = 0.24025927
                    else:
                        if input[2] < 0.68472284:
                            var94 = 0.08357847
                        else:
                            var94 = -0.044861574
    else:
        if input[9] < 0.23055014:
            if input[9] < 0.067614436:
                if input[7] < 0.5033865:
                    var94 = 0.094804816
                else:
                    if input[7] < 1.1354:
                        var94 = -0.07385943
                    else:
                        var94 = 0.05302863
            else:
                var94 = -0.08118342
        else:
            if input[7] < -0.4824063:
                var94 = -0.015392718
            else:
                var94 = 0.13948123
    if input[9] < -1.142765:
        if input[3] < 0.42386827:
            if input[7] < -1.5862556:
                var95 = 0.09524069
            else:
                if input[13] < 1.0:
                    if input[0] < -0.3908515:
                        if input[0] < -1.3433272:
                            var95 = -0.01783751
                        else:
                            var95 = -0.21963136
                    else:
                        if input[0] < 0.106092334:
                            var95 = 0.08832724
                        else:
                            var95 = -0.10442915
                else:
                    if input[1] < 0.005070672:
                        if input[14] < 1.0:
                            var95 = 0.16662632
                        else:
                            var95 = -0.035719045
                    else:
                        if input[0] < -0.5564994:
                            var95 = 0.07157503
                        else:
                            var95 = -0.19831829
        else:
            if input[3] < 0.47035775:
                if input[0] < 0.1992693:
                    var95 = 0.003793045
                else:
                    var95 = 0.24675512
            else:
                if input[0] < -0.13202658:
                    if input[3] < 1.2936667:
                        if input[0] < -0.27696854:
                            var95 = 0.04661759
                        else:
                            var95 = 0.26799512
                    else:
                        var95 = -0.1646787
                else:
                    if input[0] < 0.2510343:
                        if input[3] < 0.73790437:
                            var95 = 0.03321977
                        else:
                            var95 = -0.21103813
                    else:
                        if input[0] < 0.35456425:
                            var95 = 0.13389903
                        else:
                            var95 = -0.036254928
    else:
        if input[8] < -0.027789427:
            if input[8] < -0.028055904:
                if input[8] < -0.028158316:
                    if input[8] < -0.02823931:
                        if input[9] < -0.9332763:
                            var95 = 0.06973039
                        else:
                            var95 = 0.00076849747
                    else:
                        if input[12] < 1.0:
                            var95 = 0.23089732
                        else:
                            var95 = 0.020845998
                else:
                    if input[14] < 1.0:
                        var95 = -0.22203064
                    else:
                        var95 = -0.04917888
            else:
                if input[9] < 1.1538525:
                    if input[0] < -1.1052083:
                        var95 = -0.04943549
                    else:
                        if input[1] < 0.5750759:
                            var95 = 0.21557902
                        else:
                            var95 = -0.012321119
                else:
                    var95 = -0.11877135
        else:
            if input[8] < -0.027456515:
                if input[9] < 0.28486204:
                    if input[4] < 0.8088304:
                        var95 = -0.25164646
                    else:
                        var95 = -0.089472994
                else:
                    if input[9] < 0.6029746:
                        var95 = 0.15311055
                    else:
                        if input[9] < 1.122817:
                            var95 = -0.15937181
                        else:
                            var95 = 0.06787445
            else:
                if input[8] < -0.02738316:
                    if input[5] < 0.64104193:
                        if input[1] < -0.08993021:
                            var95 = 0.3272961
                        else:
                            var95 = 0.063447
                    else:
                        var95 = -0.08883861
                else:
                    if input[8] < -0.027242165:
                        if input[1] < 0.48007506:
                            var95 = -0.19720478
                        else:
                            var95 = 0.023685183
                    else:
                        if input[10] < -0.34624052:
                            var95 = -0.013481363
                        else:
                            var95 = 0.016705781
    if input[0] < 0.37527025:
        if input[1] < -1.4199425:
            if input[7] < 0.6371509:
                if input[1] < -1.6099442:
                    var96 = -0.045452885
                else:
                    var96 = -0.19752602
            else:
                if input[10] < -0.34624052:
                    var96 = -0.097622626
                else:
                    var96 = 0.12840304
        else:
            if input[1] < -1.3249416:
                if input[8] < -0.024182342:
                    if input[3] < 0.31213254:
                        var96 = 0.12397858
                    else:
                        var96 = -0.10705765
                else:
                    var96 = 0.19609457
            else:
                if input[3] < 0.91767496:
                    if input[7] < 0.8763027:
                        if input[7] < 0.69357884:
                            var96 = -0.010592928
                        else:
                            var96 = 0.10483851
                    else:
                        if input[0] < 0.116445325:
                            var96 = -0.0212755
                        else:
                            var96 = -0.16344774
                else:
                    if input[11] < 1.0:
                        if input[9] < -0.5142988:
                            var96 = 0.06112197
                        else:
                            var96 = -0.062807456
                    else:
                        if input[10] < -0.5500156:
                            var96 = -0.01019441
                        else:
                            var96 = 0.12271005
    else:
        if input[7] < 0.34157342:
            if input[7] < 0.08701753:
                if input[0] < 0.4477412:
                    if input[9] < -0.8944821:
                        var96 = -0.0883029
                    else:
                        if input[7] < -0.75954294:
                            var96 = 0.030507136
                        else:
                            var96 = 0.25092223
                else:
                    if input[1] < 0.2900733:
                        if input[13] < 1.0:
                            var96 = -0.013893128
                        else:
                            var96 = -0.1201671
                    else:
                        if input[7] < -0.114853054:
                            var96 = 0.010485604
                        else:
                            var96 = 0.15773538
            else:
                if input[1] < -0.9449381:
                    var96 = 0.17192502
                else:
                    if input[8] < -0.025518332:
                        if input[1] < 1.2400821:
                            var96 = -0.21595757
                        else:
                            var96 = 0.032432877
                    else:
                        if input[8] < -0.024557525:
                            var96 = 0.14366828
                        else:
                            var96 = -0.089891255
        else:
            if input[7] < 0.39287364:
                if input[3] < 0.8783539:
                    if input[10] < -0.27831548:
                        var96 = 0.2657769
                    else:
                        var96 = 0.07088283
                else:
                    var96 = 0.015874289
            else:
                if input[9] < -0.5142988:
                    if input[0] < 1.017156:
                        if input[1] < 0.5750759:
                            var96 = -0.19558094
                        else:
                            var96 = 0.15250832
                    else:
                        if input[3] < -0.43135172:
                            var96 = 0.2352189
                        else:
                            var96 = -0.0727186
                else:
                    if input[9] < -0.21170391:
                        if input[10] < -0.42926002:
                            var96 = 0.3647305
                        else:
                            var96 = -0.019773666
                    else:
                        if input[10] < -0.42926002:
                            var96 = -0.024481077
                        else:
                            var96 = 0.11851113
    if input[1] < -0.18493108:
        if input[7] < -1.261072:
            if input[7] < -1.2938153:
                if input[9] < -0.32808656:
                    if input[7] < -1.4046581:
                        if input[14] < 1.0:
                            var97 = -0.096300445
                        else:
                            var97 = 0.07713405
                    else:
                        var97 = -0.23784089
                else:
                    if input[8] < 0.015543436:
                        if input[1] < -0.75493634:
                            var97 = -0.10980844
                        else:
                            var97 = 0.2722014
                    else:
                        if input[3] < 0.8180369:
                            var97 = -0.14008443
                        else:
                            var97 = 0.04152458
            else:
                if input[7] < -1.2830763:
                    var97 = 0.32804048
                else:
                    var97 = 0.03162111
        else:
            if input[7] < -1.0090576:
                if input[9] < -1.3289773:
                    var97 = 0.123925395
                else:
                    if input[1] < -0.75493634:
                        if input[14] < 1.0:
                            var97 = -0.15594716
                        else:
                            var97 = 0.07811867
                    else:
                        var97 = -0.25306892
            else:
                if input[7] < 0.39287364:
                    if input[0] < -1.2915622:
                        if input[10] < -0.42926002:
                            var97 = 0.040463436
                        else:
                            var97 = -0.22011524
                    else:
                        if input[0] < -0.3494395:
                            var97 = 0.09252407
                        else:
                            var97 = -0.005564401
                else:
                    if input[7] < 0.4870541:
                        var97 = -0.23830114
                    else:
                        if input[0] < -1.2915622:
                            var97 = 0.09109342
                        else:
                            var97 = -0.035627387
    else:
        if input[1] < 0.19507243:
            if input[3] < 0.76233363:
                if input[3] < 0.7410882:
                    if input[0] < -1.4261512:
                        if input[8] < -0.027423343:
                            var97 = -0.16180277
                        else:
                            var97 = 0.09525899
                    else:
                        if input[0] < -0.19414456:
                            var97 = 0.0895471
                        else:
                            var97 = 0.0020240913
                else:
                    var97 = 0.3665995
            else:
                if input[3] < 0.93833226:
                    if input[10] < -0.006615333:
                        if input[10] < -0.595299:
                            var97 = -0.050259817
                        else:
                            var97 = -0.2905494
                    else:
                        if input[3] < 0.8488668:
                            var97 = 0.19529839
                        else:
                            var97 = -0.103948936
                else:
                    if input[6] < 0.97067964:
                        if input[3] < 1.1601992:
                            var97 = 0.20904087
                        else:
                            var97 = -0.0032060996
                    else:
                        if input[1] < 0.005070672:
                            var97 = -0.21545611
                        else:
                            var97 = 0.01894923
        else:
            if input[1] < 0.2900733:
                if input[0] < 0.65480113:
                    if input[0] < -1.4261512:
                        if input[3] < 0.18023762:
                            var97 = 0.15160726
                        else:
                            var97 = -0.033038747
                    else:
                        if input[0] < -0.06990861:
                            var97 = -0.15511978
                        else:
                            var97 = -0.02700074
                else:
                    if input[0] < 1.09998:
                        if input[0] < 0.9136261:
                            var97 = 0.073920645
                        else:
                            var97 = 0.25682035
                    else:
                        if input[0] < 1.4830408:
                            var97 = -0.19922347
                        else:
                            var97 = 0.037619065
            else:
                if input[7] < -1.6440885:
                    if input[9] < -0.3358454:
                        if input[0] < -0.0077906298:
                            var97 = 0.29248255
                        else:
                            var97 = 0.014182536
                    else:
                        if input[12] < 1.0:
                            var97 = -0.15399416
                        else:
                            var97 = 0.12855898
                else:
                    if input[8] < 0.07376749:
                        if input[8] < 0.05595688:
                            var97 = 0.0014536384
                        else:
                            var97 = 0.1801109
                    else:
                        if input[5] < 0.64104193:
                            var97 = 0.0637202
                        else:
                            var97 = -0.18975644
    if input[0] < 0.2510343:
        if input[0] < 0.1889163:
            if input[8] < -0.02349976:
                if input[8] < -0.023776902:
                    if input[1] < -0.37493283:
                        if input[1] < -0.46993372:
                            var98 = -0.01760899
                        else:
                            var98 = -0.16588396
                    else:
                        if input[0] < -1.0223843:
                            var98 = -0.035291407
                        else:
                            var98 = 0.03196364
                else:
                    if input[10] < -0.42926002:
                        var98 = 0.4422508
                    else:
                        var98 = -0.017118424
            else:
                if input[8] < -0.023202173:
                    var98 = -0.2347384
                else:
                    if input[3] < 0.46102956:
                        if input[8] < -0.011215854:
                            var98 = -0.16531335
                        else:
                            var98 = -0.011792408
                    else:
                        if input[1] < -0.08993021:
                            var98 = -0.03336082
                        else:
                            var98 = 0.019263022
        else:
            if input[10] < -0.27831548:
                if input[1] < 0.48007506:
                    if input[10] < -0.34624052:
                        if input[9] < 0.533145:
                            var98 = -0.23328662
                        else:
                            var98 = -0.008474091
                    else:
                        var98 = 0.06731873
                else:
                    if input[7] < -0.12399654:
                        var98 = 0.03399372
                    else:
                        var98 = 0.25095263
            else:
                var98 = -0.26281795
    else:
        if input[0] < 0.27174026:
            if input[1] < -0.18493108:
                var98 = -0.0849684
            else:
                var98 = 0.26156753
        else:
            if input[3] < 0.91767496:
                if input[3] < 0.85672647:
                    if input[3] < 0.8141936:
                        if input[9] < 0.075373285:
                            var98 = 0.035576157
                        else:
                            var98 = -0.013800363
                    else:
                        if input[2] < -0.6962018:
                            var98 = 0.11511614
                        else:
                            var98 = -0.18488643
                else:
                    if input[10] < -0.5500156:
                        if input[0] < 1.017156:
                            var98 = 0.2677971
                        else:
                            var98 = 0.06568705
                    else:
                        if input[1] < 0.3850742:
                            var98 = -0.19989295
                        else:
                            var98 = 0.09919384
            else:
                if input[3] < 0.9559655:
                    var98 = -0.21321633
                else:
                    if input[4] < 0.8088304:
                        if input[9] < 0.781428:
                            var98 = 0.056645256
                        else:
                            var98 = -0.06478735
                    else:
                        if input[14] < 1.0:
                            var98 = -0.0069462075
                        else:
                            var98 = -0.21720041
    if input[11] < 1.0:
        if input[7] < -1.6840237:
            if input[0] < 0.2510343:
                if input[1] < -0.37493283:
                    var99 = -0.013264329
                else:
                    var99 = 0.2668951
            else:
                var99 = -0.052359574
        else:
            if input[0] < 0.7893901:
                if input[0] < 0.1889163:
                    if input[0] < 0.0025623667:
                        if input[9] < -0.7858583:
                            var99 = 0.042233758
                        else:
                            var99 = -0.0182774
                    else:
                        if input[6] < 0.97067964:
                            var99 = 0.12925145
                        else:
                            var99 = -0.041523963
                else:
                    if input[8] < -0.017132947:
                        if input[0] < 0.5512712:
                            var99 = -0.105978005
                        else:
                            var99 = 0.01539192
                    else:
                        if input[2] < 0.68472284:
                            var99 = 0.11446329
                        else:
                            var99 = -0.13596728
            else:
                if input[0] < 0.8515081:
                    if input[5] < 0.64104193:
                        var99 = -0.04300718
                    else:
                        if input[9] < 0.15296172:
                            var99 = 0.0499939
                        else:
                            var99 = 0.27375564
                else:
                    if input[3] < 0.4385279:
                        if input[0] < 1.6072768:
                            var99 = -0.06595445
                        else:
                            var99 = 0.08816072
                    else:
                        if input[0] < 1.265628:
                            var99 = 0.099228375
                        else:
                            var99 = -0.020393325
    else:
        if input[9] < -1.2513889:
            if input[7] < 1.3260196:
                if input[1] < 0.2900733:
                    if input[10] < 2.8915195:
                        var99 = -0.2318538
                    else:
                        if input[7] < -0.51192284:
                            var99 = 0.06166773
                        else:
                            var99 = -0.08693442
                else:
                    if input[7] < -1.0814095:
                        var99 = -0.17954364
                    else:
                        if input[7] < -0.12399654:
                            var99 = 0.19683546
                        else:
                            var99 = -0.105600975
            else:
                var99 = 0.099200726
        else:
            if input[0] < -0.99132526:
                if input[1] < -0.08993021:
                    if input[1] < -0.8499372:
                        if input[1] < -1.1349399:
                            var99 = -0.14108811
                        else:
                            var99 = 0.19266716
                    else:
                        if input[10] < -0.27831548:
                            var99 = -0.17871442
                        else:
                            var99 = 0.054143753
                else:
                    if input[1] < 0.10007155:
                        if input[7] < -0.23367912:
                            var99 = 0.3109641
                        else:
                            var99 = 0.07828047
                    else:
                        if input[3] < 0.7086714:
                            var99 = -0.014969071
                        else:
                            var99 = 0.18184848
            else:
                if input[3] < 0.37825713:
                    if input[3] < 0.36641937:
                        if input[7] < -1.5516653:
                            var99 = -0.16258049
                        else:
                            var99 = 0.0108814975
                    else:
                        var99 = 0.33991587
                else:
                    if input[0] < -0.3597925:
                        if input[3] < 1.2371876:
                            var99 = -0.19377345
                        else:
                            var99 = 0.045888525
                    else:
                        if input[0] < -0.21485056:
                            var99 = 0.14349067
                        else:
                            var99 = -0.034455888
    if input[4] < 0.8088304:
        if input[0] < 0.98609704:
            if input[0] < 0.955038:
                if input[7] < 1.57172:
                    if input[0] < -2.306156:
                        if input[6] < 0.97067964:
                            var100 = 0.1710276
                        else:
                            var100 = -0.011637115
                    else:
                        if input[7] < 1.5329322:
                            var100 = -0.002521508
                        else:
                            var100 = -0.103541546
                else:
                    if input[1] < -0.27993196:
                        if input[3] < 0.6515143:
                            var100 = 0.05250607
                        else:
                            var100 = -0.1689897
                    else:
                        if input[2] < 0.68472284:
                            var100 = 0.15921052
                        else:
                            var100 = -0.00012085538
            else:
                if input[2] < -0.6962018:
                    var100 = 0.017102009
                else:
                    if input[3] < -0.63909185:
                        var100 = -0.02594954
                    else:
                        var100 = -0.2150581
        else:
            if input[0] < 1.027509:
                if input[1] < 0.005070672:
                    var100 = 0.017162886
                else:
                    if input[5] < 0.64104193:
                        var100 = 0.047231283
                    else:
                        var100 = 0.27718243
            else:
                if input[1] < 0.7650777:
                    if input[1] < -0.08993021:
                        if input[9] < -1.24363:
                            var100 = -0.14882767
                        else:
                            var100 = 0.066369556
                    else:
                        if input[0] < 1.5451589:
                            var100 = -0.12021164
                        else:
                            var100 = 0.03179695
                else:
                    if input[7] < -1.1486096:
                        var100 = 0.20448457
                    else:
                        if input[0] < 1.09998:
                            var100 = 0.19431393
                        else:
                            var100 = 0.008111296
    else:
        if input[8] < -0.019266702:
            if input[8] < -0.030567229:
                if input[1] < 0.5750759:
                    if input[9] < -0.5841284:
                        if input[9] < -1.049659:
                            var100 = -0.07414769
                        else:
                            var100 = 0.18552378
                    else:
                        if input[9] < 0.71935725:
                            var100 = -0.10451743
                        else:
                            var100 = 0.06412821
                else:
                    if input[1] < 1.8100873:
                        if input[0] < -1.2915622:
                            var100 = 0.04082256
                        else:
                            var100 = -0.14598365
                    else:
                        if input[1] < 2.0000892:
                            var100 = 0.2400331
                        else:
                            var100 = -0.115114324
            else:
                if input[7] < -0.5418341:
                    if input[1] < 0.7650777:
                        if input[14] < 1.0:
                            var100 = 0.14313139
                        else:
                            var100 = -0.12292181
                    else:
                        var100 = 0.2752177
                else:
                    if input[0] < 0.975744:
                        if input[0] < 0.4477412:
                            var100 = -0.0045379004
                        else:
                            var100 = 0.13205105
                    else:
                        if input[7] < 0.5822555:
                            var100 = -0.23569587
                        else:
                            var100 = 0.007844153
        else:
            if input[7] < -0.6676928:
                if input[3] < 0.77152056:
                    if input[0] < 0.30279925:
                        if input[2] < 1.0299541:
                            var100 = -0.23326878
                        else:
                            var100 = 0.05690405
                    else:
                        if input[9] < -0.65395796:
                            var100 = -0.12820546
                        else:
                            var100 = 0.08328802
                else:
                    if input[10] < -0.19680543:
                        if input[3] < 1.26428:
                            var100 = -0.13474916
                        else:
                            var100 = 0.08862152
                    else:
                        if input[3] < 0.8141936:
                            var100 = 0.29302192
                        else:
                            var100 = 0.06493327
            else:
                var100 = -0.21107109
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]
