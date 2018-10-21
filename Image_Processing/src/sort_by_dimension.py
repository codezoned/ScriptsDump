from os import mkdir, listdir, path
from PIL import Image as image
from shutil import move as mover
from math import ceil
from time import sleep

current_directory = listdir('.')
files = 0
folders = 0

def nameshorten(image):
    name_length = len(image)
    namediv_even = name_length / 2
    namediv_odd = int(ceil(name_length / 2))

    def range_maker(designated_var):
      return f'{image[:designated_var - designated_var / 2]} ... {image[- int(ceil(designated_var/ 2)):]}'

    if name_length % 2 == 0 and name_length > 50: #even
      range_maker(namediv_even)
    elif name_length % 2 != 0 and name_length > 50: #odd
      range_maker(namediv_odd)
    else:
        return image

def imagesize(x):
    return f"{str(image.open(x).width)}x{str(image.open(x).height)}"

for i in current_directory:
    try:
        fileformat = image.open(i).format
        imgsize = imagesize(i)
        if not path.exists(imgsize):
            mkdir(imgsize)
            folders =+ 1
        else:
            print(f"Image: {nameshorten(i)} -> Folder: '{imgsize}'")
    except IOError:
        continue

for i in current_directory:
    try:
        imgsize = imagesize(i)
        fileformat = image.open(i).format
        if fileformat in ('JPEG', 'BMP', 'GIF', 'PNG'):
            mover(i, imgsize)
            print(f"Image: {nameshorten(i)} -> Folder: '{imgsize}'")
            files =+ 1
    except IOError:
        continue

print ("------------------")
print ("  \n Sorting complete!\n")
print (f"- Files sorted: {len(current_directory)}")
print (f"- Images moved: {files}")
print (f"- Folders created: {folders}")
