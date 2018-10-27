import math

from copy import deepcopy
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def negative(r,g,b):
    r = int(255-r)
    g = int(255-g)
    b = int(255-b)
    return [r, g, b]


def setRGB(r,g,b):
    r = int(r)
    g = int(g)
    b = int(b)
    return [r, g, b]

img = Image.open('img/PeppersRGB.jpg')
img = np.asarray(img)

colorImg = deepcopy(img)

for i in range(len(img)):
        for j in range(len(img[i])):
            pixelR = int (img[i][j][0])
            pixelG = int (img[i][j][1])
            pixelB = int (img[i][j][2])

            colorImg[i][j] = negative(pixelR,pixelG,pixelB)






plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3)
plt.imshow(colorImg)
plt.subplot(2,2,4)
plt.hist(colorImg.ravel(),256,[0,256])


plt.show()
