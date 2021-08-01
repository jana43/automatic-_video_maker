from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops , ImageOps
import textwrap
import os
import httplib2
from urllib.parse import urlencode, quote # For URL creation
from gtts import gTTS, lang 

background = Image.open('thumbnailtemplates/bitmap.png')
episod = 'e04s01 ~ '
remark = '10 inspirational quotes you should not miss'
im = Image.open('thumbnail/20210731_105603.png')
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(
    'Bangers-Regular.ttf', 110)

MAX_W , MAX_H = 1872 , 1032
w,h = draw.textsize(remark , font=font)

font_colors = [(5, 221, 255),(226, 186, 44),(5, 221, 255)]
draw.text((50, 50), episod, font=font  , fill =font_colors[1] ,  stroke_width=16 , stroke_fill="black")

draw.text((50, 170), remark, font=font  , fill =font_colors[0] ,  stroke_width=16 , stroke_fill="black")
background.paste(im , (0,0),mask=im)
background.save(f'thumbnail.png')