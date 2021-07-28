import os

files = os.listdir('videoclip')
frames = os.listdir('thumbnail')

files = sorted(files)
frames = sorted(frames)


print(files)
print(frames)


for video , frame in zip(files,frames):
    print(video , frame)
    syntax = f'''ffmpeg -i videoclip/{video} -i thumbnail/{frame} -filter_complex "[0:v][1:v] overlay=0:0:enable='between(t,0,20)'" -vb 20M -s "1920x1080" vms/{video}'''
    os.system(syntax)