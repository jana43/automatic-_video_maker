from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops , ImageOps
import textwrap
import os
import httplib2
from urllib.parse import urlencode, quote # For URL creation

# To play wave files
import pygame
import math # For ceiling

text_file = open('this.txt','r')
texts = text_file.readlines()
print(texts)
count = 0
string = ''''''
string_list = []
for text in texts:
    astr = text
    para = textwrap.wrap(astr, width=20)
    print(para)
    for item in para:
        string = string + item + '\n'
    string_list.append(string)
    string = ''''''
print(string_list)



text_filea = open('thisa.txt','r')
textsa = text_filea.readlines()
print(textsa)
string_lista = textsa
print(string_lista)

    







#for right top corner
def right(string_list ,i,title):
    count = 0
    font_colors = [(226, 186, 44),(5, 221, 255),(5, 221, 255)]
    stroke_colors = [(0, 0, 0),(0, 48, 56),(0, 48, 56)]
    glow_colors = [(113, 249, 230, 6),(113, 249, 230, 6),(113, 249, 230, 6)]
    current_h, pad = 50, 10
    color_counter = 0

    text = string_list[i]



    
    MAX_W , MAX_H = 1872 , 1032
    im = Image.new('RGBA', (MAX_W, MAX_H), (255, 255, 255, 5))
    # im = Image.open('bitmap.png')
    im = im.filter(ImageFilter.GaussianBlur(radius = 5))
    im = ImageOps.expand(im , border=24 , fill=font_colors[color_counter])
    print(len(para),MAX_H,MAX_W)
    # im = Image.open('bitmap.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
    'Staatliches-Regular.ttf', 80)
    w,h = draw.textsize(text , font=font)
    draw.text(((MAX_W - w) -100, 30), text, font=font,fill =font_colors[color_counter] ,  stroke_width=16 , stroke_fill=stroke_colors[color_counter])
    # im.paste(img2 ,(300,300),mask=img2 )
    im.save(f'thumbnail/{title}.png')  
    count = count+1


def left(string_list ,i, title):
    print("file processing")
    count = 0
    font_colors = [(226, 186, 44),(5, 221, 255),(5, 221, 255)]
    stroke_colors = [(0, 0, 0),(0, 48, 56),(0, 48, 56)]
    glow_colors = [(113, 249, 230, 6),(113, 249, 230, 6),(113, 249, 230, 6)]
    current_h, pad = 50, 10
    color_counter = 0
    text = string_list[i]
    MAX_W , MAX_H = 1872 , 1032
    im = Image.new('RGBA', (MAX_W, MAX_H), (255, 255, 255, 5))
    # im = Image.open('bitmap.png')
    im = im.filter(ImageFilter.GaussianBlur(radius = 5))
    im = ImageOps.expand(im , border=24 , fill=font_colors[color_counter])
    print(len(para),MAX_H,MAX_W)
    # im = Image.open('bitmap.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
    'Staatliches-Regular.ttf', 80)
    w,h = draw.textsize(text , font=font)
    draw.text((100, 30), text, font=font,fill =font_colors[color_counter],   stroke_width=16 , stroke_fill=stroke_colors[color_counter])
    # im.paste(img2 ,(300,300),mask=img2 )
    im.save(f'thumbnail/{title}.png')  
    count = count+1


def middle(texts ,i ,title):
    count = 0
    string = ''''''
    string_list = []
    for text in texts:
        astr = text
        para = textwrap.wrap(astr, width=40)
        print(para)
        for item in para:
            string = string + item + '\n'
        string_list.append(string)
        string = ''''''
    print(string_list)

    print("file processing")
    count = 0
    font_colors = [(226, 186, 44),(5, 221, 255),(5, 221, 255)]
    stroke_colors = [(0, 0, 0),(0, 48, 56),(0, 48, 56)]
    glow_colors = [(113, 249, 230, 6),(113, 249, 230, 6),(113, 249, 230, 6)]
    current_h, pad = 50, 10
    color_counter = 0



    text = string_list[i]
    MAX_W , MAX_H = 1872 , 1032
    im = Image.new('RGBA', (MAX_W, MAX_H), (255, 255, 255, 5))
    # im = Image.open('bitmap.png')
    im = im.filter(ImageFilter.GaussianBlur(radius = 5))
    im = ImageOps.expand(im , border=24 , fill=font_colors[color_counter])
    print(len(para),MAX_H,MAX_W)
    # im = Image.open('bitmap.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
    'Staatliches-Regular.ttf', 80)
    w,h = draw.textsize(text , font=font)
    draw.text((300,600), text, font=font,fill =font_colors[color_counter] ,  stroke_width=16 , stroke_fill=stroke_colors[color_counter])
    # im.paste(img2 ,(300,300),mask=img2 )
    im.save(f'thumbnail/{title}.png')  
    count = count+1



def audioGenerator(string_lista,i, title):
# Mary server informations
    mary_host = "localhost"
    mary_port = "59125"
    text = string_lista[i]
    query_hash = {"INPUT_TEXT":text,
                  "INPUT_TYPE":"TEXT", # Input text
                  "LOCALE":"en_US",
                  "VOICE":"dfki-spike-hsmm", # Voice informations  (need to be compatible)
                  "OUTPUT_TYPE":"AUDIO",
                  "AUDIO":"WAVE",
                  "EFFECTS":{
                      "effect_chorus_selected":"delay1:466;amp1:0.5"
                  } # Audio informations (need both)
                  }
    query = urlencode(query_hash)
    print("query = \"http://%s:%s/process?%s\"" % (mary_host, mary_port, query))
    
    # Run the query to mary http server
    h_mary = httplib2.Http()
    resp, content = h_mary.request("http://%s:%s/process?" % (mary_host, mary_port), "POST", query)
    
    #  Decode the wav file or raise an exception if no wav files
    if (resp["content-type"] == "audio/x-wav"):
    
        # Write the wav file
        f = open(f"audioclip/{title}.wav", "wb")
        f.write(content)
        f.close()
    
        # Play the wav file
        pygame.mixer.init(frequency=16000) # Initialise the mixer
        s = pygame.mixer.Sound(f"audioclip/{title}.wav")
        s.play()
        pygame.time.wait(int(math.ceil(s.get_length() * 1000)))
        
    
    else:
        raise Exception(content)

i =0 
postion = os.listdir('videoclip')
for pos in postion:
    print(pos)
    title = pos.replace('.mp4','')
    if 'right.mp4' in pos:
        left(string_list , i,title)
        audioGenerator(string_lista , i , title)
        i = i+1
    elif 'left.mp4' in pos:
        right(string_list, i,title)
        audioGenerator(string_lista , i , title)
        i = i+1
    elif 'middle.mp4' in pos:
        middle(texts, i,title)
        audioGenerator(string_lista , i , title)
        i = i+1





      



