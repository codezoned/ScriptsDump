# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:42:58 2016

@author: utkarsh
"""

import numpy as np
#import cv2
#import numpy as np;
import matplotlib.pylab as plt;
import scipy.ndimage
import sys
import cv2

from image_enhance import image_enhance


if(len(sys.argv)<2):
    print('loading sample image');
    img_name = '01.jpg'
    img = scipy.ndimage.imread('images/' + img_name);
    
elif(len(sys.argv) >= 2):
    img_name = sys.argv[1];
    img = scipy.ndimage.imread(sys.argv[1]);
    
if(len(img.shape)>2):
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114]);
    
    
print(img.shape)

rows,cols = np.shape(img);
aspect_ratio = np.double(rows)/np.double(cols);

new_rows = 350;             # randomly selected number
new_cols = new_rows/aspect_ratio;

#img = cv2.resize(img,(new_rows,new_cols));
img = scipy.misc.imresize(img,(np.int(new_rows),np.int(new_cols)));

enhanced_img = image_enhance(img);
enhanced_img = 255*np.uint8(enhanced_img)
kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(enhanced_img, cv2.MORPH_OPEN, kernel)
erosion = cv2.erode(enhanced_img,kernel,iterations = 1)

cv2.imshow('output',enhanced_img)
cv2.waitKey(0)

   

if(1):
    print('saving the image')
    scipy.misc.imsave('../enhanced/' + img_name, enhanced_img)
else:
    plt.imshow(enhanced_img,cmap = 'Greys_r');
