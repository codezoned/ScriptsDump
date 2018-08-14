#IN PROGRESS - Not complete but works
#Written by Senthil @Rats12
#This bot plays this game for you - http://orteil.dashnet.org/cookieclicker/
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import win32api, win32con
import os
import time


###CORDINATES FOR BUTTONS
x_cookie=210
y_cookie=342

x_button1=1163
y_button1=291
button1_unavail=8436 ###pixel sum of greyed out button

x_button2=1195
y_button2=365
button2_unavail=12912 ##pixel sum of greyed out button


##to cheeck if button1 is available
def get_button1(): 
    box = (1049+7,266+7,1049+53,266+56)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    #im.save(os.getcwd() + 'cursor__' + str(int(time.time())) + '.png', 'PNG')    
    return a

##to check if button2 is available
def get_button2():
    box = (1049+2,266+65,1049+57,266+127)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    #im.save(os.getcwd() + 'cursor__' + str(int(time.time())) + '.png', 'PNG')    
    return a


##takes a screenshot of the buttons
def screenGrab():
    box =(1049,266,1340,516)
    im=ImageGrab.grab(box)
    im.save(os.getcwd() +'\\ __buttons __' +'.png','PNG')
    return im
    


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("LEFT CLICK")

def mousePos(x,y):
    win32api.SetCursorPos((x,y))


def check1():
    if(get_button1() != button1_unavail):
        mousePos(x_button1,y_button1)
        time.sleep(.1)
        leftClick()



def check2():
    if(get_button2() != button2_unavail):
        mousePos(x_button2,y_button2)
        time.sleep(.1)
        leftClick()


#get cordinates of current mouse pos
def get_cords():
    x,y = win32api.GetCursorPos()
    
    print (x,y)



def main():
    while True:
        try:
         
            mousePos(x_cookie,y_cookie)
            leftClick()
            time.sleep(.1)
            check2()
            time.sleep(.1)
            check1()
            time.sleep(.1)

        except (KeyboardInterrupt):
            print('closing')
            exit()
  
        
        
        


