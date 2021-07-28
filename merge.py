import os 



files = os.listdir('vms')
files = sorted(files)

print(files)



syntax = f'''ffmpeg -i vms/{files[0]} -i vms/{files[1]} -i vms/{files[2]} -i vms/{files[3]} -i vms/{files[4]} \
    -filter_complex "[0:v][1:v]xfade=transition=wipedown:duration=1.000:offset=12[V01];\
        [V01][2:v]xfade=transition=wipeleft:duration=1.000:offset=24[V02];\
            [V02][3:v]xfade=transition=wipeleft:duration=1.000:offset=36[V03];\
                [V03][4:v]xfade=transition=wipeleft:duration=1.000:offset=48"\
            -s "1920x1080" -vb 20M output.mp4'''


# os.system('ffmpeg -i 1a.mp4 -i 2a.mp4 -i 3a.mp4 -filter_complex "[0:v][1:v]xfade=transition=wipedown:duration=1.000:offset=9.16[V01];[V01][2:v]xfade=transition=wipeleft:duration=1.000:offset=19" -s "1920x1080" -vb 20M output.mp4')

os.system(syntax)