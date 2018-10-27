'''
Written by Abhinav Dhere (abhitechnical41[at]gmail.com).
NOTE: Currently some part of focussed image is being lost. Bug needs to be fixed.
'''
from PIL import Image
import numpy as np
import sys
import pdb

def sphericalTransform(im, xc, yc, rmax, rho ):
    '''
    Apply spherical transform on image im.
    xc,yc - center of lens ; rmax - radius ; rho - refractive index of lens.
    '''
    im2 = im1
    for i in range(0,im2.shape[0]):
        for j in range(1,im2.shape[1]):
            dx=i-xc
            dy=j-yc
            r=(dx**2+dy**2)**0.5
            z=(rmax**2-r**2)**0.5
            Bx=(1-(1/rho))*np.arcsin(dx/((dx**2+z**2)**0.5))
            By=(1-(1/rho))*np.arcsin(dy/((dy**2+z**2)**0.5))
            if r<rmax:
                t1=int(np.round(i-z*np.tan(Bx)))
                t2=int(np.round(j-z*np.tan(By)))
            else:
                t1=0
                t2=0
            if (t1>0 and t1<im1.shape[0]) and (t2>0 and t2<im1.shape[1]):
                im2[i,j,0] = im1[t1,t2,0]
                im2[i,j,1] = im1[t1,t2,1]
                im2[i,j,2] = im1[t1,t2,2]
    return im1

filename=sys.argv[1]
xc,yc,rmax,rho=np.ravel(map(float,sys.argv[2].split(',')))
im1 = np.array(Image.open(filename))
print(im1.shape)
im_trans = sphericalTransform(im1,xc,yc,rmax,rho)
im_out = Image.fromarray(im_trans)
im_out.show()
