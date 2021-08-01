
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops , ImageOps
import textwrap
import os
import httplib2
from urllib.parse import urlencode, quote # For URL creation
from gtts import gTTS, lang 



text_file = open('this.txt','r')
texts = text_file.readlines()


text_filea = open('thisa.txt','r')
textsa = text_filea.readlines()
print(textsa)
string_lista = textsa
print(string_lista)

def textg(text_l,title):
    MAX_W , MAX_H = 1872 , 1032
    im = Image.new('RGBA', (MAX_W, MAX_H), (255, 255, 255, 5))
    font_colors = [(235, 137, 52),(255, 255, 255),(44, 176, 48)]
    # font_colors = [(226, 186, 44),(5, 221, 255),(5, 221, 255)]
    # im = Image.open('bitmap.png')
    im = ImageOps.expand(im , border=24 , fill=font_colors[0])
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
    'Bangers-Regular.ttf', 110)
    w,h = draw.textsize(text_l , font=font)
    lines = textwrap.wrap(text_l, width=40)
    print(lines)
    y_text = h
    center = h/2
    color_counter = 0
    
    for line in lines:
        width, height = font.getsize(line)
        print(color_counter)
        print(font_colors)
        draw.text(((MAX_W - width) / 2, (MAX_H/2)+ (y_text)-center-100), line, font=font  , fill =font_colors[color_counter] ,  stroke_width=16 , stroke_fill="black")
        y_text += height+20
        if color_counter >= 2:
            color_counter = 0
        else:
            color_counter = color_counter+1
    
    
    im.save(f'thumbnail/{title}.png')





def audioGenerator(string_lista,i, title):
    speech = gTTS(text = string_lista[i], lang = "en-uk", slow = False,tld='ca')  
    speech.save(f'audioclip/{title}.mp3')

i =0 
postion = os.listdir('videoclip')
for pos , item in zip(postion,texts):
    print(pos)
    title = pos.replace('.mp4','')
    print(item)
    textg(item,  title)
    # audioGenerator(string_lista , i , title)
    i += 1
  