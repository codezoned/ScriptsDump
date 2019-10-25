from tkinter import *
import os
import random

#Creating GUI
#welcome note

    
root=Tk()
root.title("EncRYPTO")
Label(root,font=('arial',20,'bold'),text="WELCOME TO EncRYPTO").grid(columnspan=2)
Label(root,font=('arial',10),text="Choose an image file to encrypt data into").grid(columnspan=2)


#opens dialog to choose image file for encryption


from tkinter.filedialog import askopenfilename
filename = askopenfilename()


#Accessing image and image matrix

from PIL import Image
im=Image.open(filename).convert('L')
data=im.load()
w,h=im.size
img=Image.open(filename).convert('L')
final=img.load()
l=[]
central=[]
c=0

#Creating pixel intensity matrix where each row contains 5 columns which have all possible pixel values of an image(5 values in 1 row).

for i in range(0,255,5):
    t=[x for x in range(i,i+5)]
    l.append(t)
    central.append(i+2)

#Pixel Mapping Reference to encrypt Image
    
pm=(100,101,110,111)

#Creating Location Map

loc_map=""    
for i in range(im.size[0]):
    for j in range(im.size[1]):
        k=0
        for v in l:
            if(v[2]==data[i,j]):
                loc_map=loc_map+"1"
                k=1
                break
        if(k==0):
            loc_map=loc_map+"0"
            
#Generating Random data to hide into image
            
from random import randint
d=""
for i in range(5120):
    d=d+str(randint(0,1))
    
#Embedding data into image using a reversible data hiding technique
    
di=0
flag=0
c=0
for i in range(w):
    for j in range(h):
       if(final[i,j] in central):
           while(c<len(d)):
               if(d[c]=='1'):
                   y=d[c:c+3]
                   ind=central.index(final[i,j])
                   tup=l[ind]
                   if(int(y)==pm[0]):
                       final[i,j]=tup[0]
                   elif(int(y)==pm[1]):
                       final[i,j]=tup[1]
                   elif(int(y)==pm[2]):
                       final[i,j]=tup[3]
                   elif(int(y)==pm[3]):
                       final[i,j]=tup[4]
                   break
               else:
                   pass
               c=c+1
               
#Calculating PSNR value of the encrypted image
               
import math     

s=0
for i in range(w):
    for j in range(h):
       s=s+(data[i,j]-final[i,j])**2
s=s/(w*h)
PSNR=10*math.log10((255*255)/s)

#Saving the encrypted image

img.save("Encrypted.png")

#Creating GUI to display results

Label(root,font=('arial',20,'bold'),text="IMAGE ENCRYPTED").grid(columnspan=2)
Label(root,text="MSE value is :"+str(s)).grid(columnspan=2)
Label(root,text="PSNR value is :"+str(PSNR)).grid(columnspan=2)


def display_Encrypted():
    os.system("Encrypted.png")
def display():
    os.system(filename)
def exit():
    root.destroy()
Button(root, text='Display Original Image', command=display).grid(row=5,column=0)
Button(root, text='Display Encrypted Image', command=display_Encrypted).grid(row=5,column=1,sticky=W)
Button(root, text='Exit',command=exit,width=10).grid(row=7,columnspan=2)

#STATUS OF OUR PROJECT

"""The project stands completed.
We have made use of the Python Imaging Library to access and process the image
and hide data into it. We have also used the tkinter library to make a graphical
user interface or GUI to make the program user friendly. The code makes use of pixel
intensity segmentation.In this technique, we have divided all possible pixels of image
into groups of five out of which the central pixel value is the concealable pixel. Then
the loop goes through the matrix object and finds all the concealable pixels and hides
data accordingly."""
        
                
        
    
    
    
    
