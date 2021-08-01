from pydub import AudioSegment
import os
layer = AudioSegment.from_file("layer.wav", format="wav")


audios = os.listdir('audioclip')
audios = sorted(audios)
print(audios)

final = []
i = 0
for item in audios:
    sound = AudioSegment.from_file(f'audioclip/{item}', format="mp3")
    overlay = layer.overlay(sound , position = i)
    final.append(overlay)
    i = i+1
  
print(final)


combine = ''
k = 0
for item in final:
    if k == 0:
        combine = item
        k += 1
    else:
        combine = combine + item

file_handle = combine.export("output.wav", format="wav")

    
