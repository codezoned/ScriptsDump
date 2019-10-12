# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:50:30 2016

@author: utkarsh
"""
from ridge_segment import ridge_segment
from ridge_orient import ridge_orient
from ridge_freq import ridge_freq
from ridge_filter import ridge_filter
import cv2
import numpy as np
import scipy.ndimage

def image_enhance(img):
    blksze = 40;
    thresh=0.1
    normim,mask = ridge_segment(img,blksze,thresh);             # normalise the image and find a ROI
    temp=normim -normim.min()
    temp =temp/temp.max()
    cv2.imshow("normim",normim)
    cv2.waitKey(0)

    gradientsigma = 1;
    blocksigma = 9;
    orientsmoothsigma = 7;
    orientim = ridge_orient(normim, gradientsigma, blocksigma, orientsmoothsigma);              # find orientation of every pixel
    cv2.imshow("orientim",orientim)
    cv2.waitKey(0)

    blksze = 50;
    windsze = 5;
    minWaveLength = 5;
    maxWaveLength = 15;
    freq,medfreq = ridge_freq(normim, mask, orientim, blksze, windsze, minWaveLength,maxWaveLength);    #find the overall frequency of ridges
    
    
    freq = medfreq*mask;
    kx = 0.65;ky = 0.65;
    newim = ridge_filter(normim, orientim, freq, kx, ky);       # create gabor filter and do the actual filtering
    # temp=newim-newim.min();
    # temp = temp/temp.max()
    # cv2.imshow('output',newim)
    # cv2.waitKey(0)
   
   
    #gray = cv2.cvtColor(newim, cv2.COLOR_BGR2GRAY)    
    #thresholding
    th, bin_im = cv2.threshold(np.uint8(newim),0,255,cv2.THRESH_BINARY);
    # cv2.imshow('out',bin_im)
    # cv2.waitKey(0)
    # th3 = cv2.adaptiveThreshold((bin_im).astype('uint8'),255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
            
    # cv2.imshow('out',th3)
    # kernel = np.ones((5,5),np.uint8)
    # closing = cv2.morphologyEx(bin_im, cv2.MORPH_OPEN, kernel)
    # cv2.imshow('outclosed',closing)
    # cv2.waitKey(0)

    cv2.waitKey(0)
    return(newim<th )