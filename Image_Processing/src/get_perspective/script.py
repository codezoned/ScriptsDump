import cv2
import numpy as np
import argparse

# global vars
arr = []
count = 0

# setup argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help = "path to image")
args = vars(parser.parse_args())

# transform image to perspective form using warpPerspective
def transform(img, arr):
       (tl, tr, br, bl) = arr

       # find the maximum width of selected object
       widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
       widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
       w = max(int(widthA), int(widthB))

       # find the maximum height of selected object
       heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
       heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
       h = max(int(heightA), int(heightB))

       print("New Image Dimensions: \nWidth = {}\nHeight = {}".format(w,h))
       # Create source and destination points
       inp_pts = np.float32(arr)
       op_pts = np.float32([[0,0],[w-1,0],[w-1,h-1],[0,h-1]])

       # Create Perspective Transform and perform warp Perspective
       M = cv2.getPerspectiveTransform(inp_pts,op_pts)
       out = cv2.warpPerspective(img, M, (w, h))

       return out

# read image
img = cv2.imread(args["path"])

# resize image
width = 500
height = int((img.shape[0] * 500)/(img.shape[1]))
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('image', img)

# helper function to append coordinates
def points(x,y):
    if len(arr) <= 4:
        arr.append((x,y))
    return len(arr)

# helper function to draw connector lines
def draw(count, img):
    if(count == 2):
        cv2.line(img, arr[0], arr[1], (255,255,255), 2)
    if(count == 3):
           cv2.line(img, arr[1], arr[2], (255,255,255), 2)
    if(count == 4):
           cv2.line(img, arr[2], arr[3], (255,255,255), 2)
           cv2.line(img, arr[3], arr[0], (255,255,255), 2)

# mouseclick events
def onClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        count = points(x,y)
        if count <= 4:
            cv2.circle(img, (x,y), 2, (255,255,0), 10)
            draw(count, img)
        cv2.imshow('image', img)

cv2.setMouseCallback('image', onClick)
cv2.waitKey(0)

# transform image with mentioned coordinates
out = transform(img, arr)

cv2.imshow('final', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
