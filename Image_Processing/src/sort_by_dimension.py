from os import mkdir, listdir, path
from PIL import Image as image
from shutil import move as mover
from math import ceil
from time import sleep

current_directory = listdir('.')
files = []
folders = []

def nameshorten(image):
    name_length = len(image)
    namediv_even = name_length / 2
    namediv_odd = int(ceil(name_length / 2))

    if name_length % 2 == 0 and name_length > 50: #even
        return "{} ... {} ".format(image[:namediv_even - namediv_even / 2],
                                   image[- int(ceil(namediv_even / 2)):])

    elif name_length % 2 != 0 and name_length > 50: #odd
        return "{} ... {} ".format(image[:namediv_odd - namediv_odd / 2],
                                   image[- int(ceil(namediv_odd / 2)):])
    else:
        return image

def imagesize(x):
    width = str(image.open(x).width)
    height = str(image.open(x).height)
    return "{}x{}".format(width, height)

for i in current_directory:
    try:
        fileformat = image.open(i).format
        imgsize = imagesize(i)
        if not path.exists(imgsize):
            mkdir(imgsize)
            folders.append('.')
        else:
            print "Image: {} -> Folder: '{}'".format(nameshorten(i), imgsize)
    except IOError:
        continue

for i in current_directory:
    try:
        imgsize = imagesize(i)
        fileformat = image.open(i).format
        if fileformat == 'JPEG' or fileformat == 'BMP' or fileformat == 'GIF' or fileformat == 'PNG':
            mover(i, imgsize)
            files.append('*')
    except IOError:
        continue

print "------------------"
print "  \n Sorting complete!\n"
print "- Files sorted: {}".format(len(current_directory))
print "- Images moved: {}".format(len(files))
print "- Folders created: {}".format(len(folders))
