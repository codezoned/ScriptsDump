# coding: utf8
# Author: Oriol Vall

from PIL import Image

#FLIP AN IMAGE

def mirror(image_path, direction):
    image_obj = Image.open(image_path)
    if direction == 'h': # Horizontal
        rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == 'v':
        rotated_image = image_obj.transpose(Image.FLIP_TOP_BOTTOM)
    rotated_image.show()
 
if __name__ == '__main__':
    image = 'test.jpg'
    mirror(image, 'h')
    mirror(image, 'v')