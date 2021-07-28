import os
#load a video and out a video 
# ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -shortest output.mp4

os.system('ffmpeg -i output.mp4 -i audio/this.wav -map 0:v -map 1:a -s "1920x1080" -vb 20M main.mp4')