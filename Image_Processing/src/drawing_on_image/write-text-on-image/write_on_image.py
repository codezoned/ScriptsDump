from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
 
in_file, out_file, text = sys.argv[1:]
 
img = Image.open(in_file)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)
draw.text((0, 0), text, (255, 255, 255), font=font)
img.save(out_file)