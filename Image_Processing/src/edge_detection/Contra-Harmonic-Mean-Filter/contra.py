from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy

def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray

def setGrayColor(color):
    color = int(color)
    return [color, color, color]

size = 3
limit = int((size-1)/2)

file = input('Enter image name: ')
print('Hello', file)


#image SaltNoise, pepperNoise

imgPep = Image.open('image/'+file+'.bmp')

imgPep = np.asarray(imgPep)
Contra = deepcopy(imgPep)

#Q > 0 for Pepper Noise
#Q < 0 for Salt Noise

q = input('Enter Q : ')
q = int(q)


qup = q+1
for i in range(limit,len(imgPep)-limit):
    for j in range(limit,len(imgPep[i])-limit):
        s1 = 0
        s2 = 0
        zigma1 = 0
        zigma2 = 0

        for k in range(i-limit, i+limit+1):
            for l in range(j-limit, j+limit+1):
                exe = getGrayColor(imgPep[k][l])

                if exe is 0 and q+1.0 < 0:
                    zigma1 += 0
                else:
                    zigma1 += exe**(q+1.0)

                if exe is 0 and q < 0:
                    zigma2 += 0
                else:
                    zigma2 += exe**q

                s1 += zigma1
                s2 += zigma2
        if s2==0 :
            Contra[i][j] = setGrayColor(0)
        else :
            Contra[i][j] = setGrayColor(s1/s2)


plt.subplot(2, 2, 1)
plt.imshow(imgPep)
plt.subplot(2, 2, 2)
plt.imshow(Contra)
plt.show()