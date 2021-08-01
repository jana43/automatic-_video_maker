import os 



files = os.listdir('vms')
files = sorted(files)

print(files)



syntax = f'''ffmpeg -i tintro.mp4 -i vms/{files[0]} -i vms/{files[1]} -i vms/{files[2]} -i vms/{files[3]} -i vms/{files[4]} -i vms/{files[5]} -i vms/{files[6]} -i vms/{files[7]} -i vms/{files[8]} -i vms/{files[9]} -i vms/{files[10]} -i vms/{files[11]} -i vms/{files[12]} -i vms/{files[13]} -i vms/{files[14]}  -i toutro.mp4 \
    -filter_complex "[0:v][1:v]xfade=transition=wipeup:duration=1.000:offset=5[V01];\
        [V01][2:v]xfade=transition=wipedown:duration=1.000:offset=17[V02];\
            [V02][3:v]xfade=transition=wipeleft:duration=1.000:offset=29[V03];\
                [V03][4:v]xfade=transition=wiperight:duration=1.000:offset=41[V04];\
                    [V04][5:v]xfade=transition=wipeup:duration=1.000:offset=53[V05];\
                        [V05][6:v]xfade=transition=wipedown:duration=1.000:offset=65[V06];\
                            [V06][7:v]xfade=transition=wipeleft:duration=1.000:offset=77[V07];\
                                [V07][8:v]xfade=transition=wiperight:duration=1.000:offset=89[V08];\
                                    [V08][9:v]xfade=transition=wipeup:duration=1.000:offset=101[V09];\
                                        [V09][10:v]xfade=transition=wipedown:duration=1.000:offset=113[V10];\
                                            [V10][11:v]xfade=transition=wipeleft:duration=1.000:offset=125"\
            -s "1920x1080" -vb 20M output.mp4'''



syntax = f'''ffmpeg -i tintro.mp4 -i vms/{files[0]} -i vms/{files[1]} -i vms/{files[2]} -i vms/{files[3]} -i vms/{files[4]} -i vms/{files[5]} -i vms/{files[6]} -i vms/{files[7]} -i vms/{files[8]} -i vms/{files[9]} -i vms/{files[10]} -i vms/{files[11]} -i vms/{files[12]} -i vms/{files[13]} -i vms/{files[14]}  -i toutro.mp4 \
    -filter_complex "[0:v][1:v]xfade=transition=wipeup:duration=1.000:offset=5[V01];\
        [V01][2:v]xfade=transition=wipedown:duration=1.000:offset=17[V02];\
            [V02][3:v]xfade=transition=wipeleft:duration=1.000:offset=29[V03];\
                [V03][4:v]xfade=transition=wiperight:duration=1.000:offset=41[V04];\
                    [V04][5:v]xfade=transition=wipeup:duration=1.000:offset=53[V05];\
                        [V05][6:v]xfade=transition=wipedown:duration=1.000:offset=65[V06];\
                            [V06][7:v]xfade=transition=wipeleft:duration=1.000:offset=77[V07];\
                                [V07][8:v]xfade=transition=wiperight:duration=1.000:offset=89[V08];\
                                    [V08][9:v]xfade=transition=wipeup:duration=1.000:offset=101[V09];\
                                        [V09][10:v]xfade=transition=wipedown:duration=1.000:offset=113[V10];\
                                                [V10][11:v]xfade=transition=wipeleft:duration=1.000:offset=125[V11];\
                                                    [V11][12:v]xfade=transition=wipeleft:duration=1.000:offset=137[V12];\
                                                        [V12][13:v]xfade=transition=wipeleft:duration=1.000:offset=149[V13];\
                                                            [V13][14:v]xfade=transition=wipeleft:duration=1.000:offset=161[V14];\
                                                                [V14][15:v]xfade=transition=wipeleft:duration=1.000:offset=173[V15];\
                                                                    [V15][16:v]xfade=transition=wipeleft:duration=1.000:offset=185"\
            -s "1920x1080" -vb 20M output.mp4'''


# os.system('ffmpeg -i 1a.mp4 -i 2a.mp4 -i 3a.mp4 -filter_complex "[0:v][1:v]xfade=transition=wipedown:duration=1.000:offset=9.16[V01];[V01][2:v]xfade=transition=wipeleft:duration=1.000:offset=19" -s "1920x1080" -vb 20M output.mp4')

os.system(syntax)



                                            