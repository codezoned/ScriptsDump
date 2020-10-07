from cv2 import cv2
import numpy as np
import sys

image_name = input("Enter the name of the input image: ")

# reading the image
img = cv2.imread(image_name)

while img is None:
    image_name = input("Enter the name of the input image or Enter 'exit' to end program : ")
    # if end the program 
    if image_name == "exit":
        sys.exit()

    # reading the image
    img = cv2.imread(image_name)    

# resize the image to fit it to show in the screen
img = cv2.resize(img, (0, 0), None, .75, .75)

# converting the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# inverting the image
img_invert = cv2.bitwise_not(img_gray)
# bluring or smoothing the inverted image with the kernel size (25,25)
img_blur = cv2.blur(img_invert, (25, 25))

# Applying another type of blur for cheaking
img_blur_2 = cv2.GaussianBlur(img_invert, (23, 23),0)

# The Dodge blend function divides the bottom layer by the inverted top layer. 
# This lightens the bottom layer depending on the value of the top layer. 
# We have the blurred image, which highlights the boldest edges.
def dodgeV2(image, mask):
    # inverting color with 255 - ...
    return cv2.divide(image, 255 - mask, scale=256)


final_img = dodgeV2(img_gray, img_blur)

final_img_2 = dodgeV2(img_gray, img_blur_2)
# final_img_2 = cv2.blur(final_img_2, (3, 3),0)
final_img_2 = cv2.bilateralFilter(final_img_2,9,50,50)

# convert to bgr for showing the input and output in the same window
# this will convert the output from 2 channel to 3 channel
final_img = cv2.cvtColor(final_img, cv2.COLOR_GRAY2BGR)
# concatenate both the input and output 
numpy_vertical_concat = np.concatenate((img, final_img), axis=1)

# cv2.imshow('image', final_img)
# cv2.imshow('image_2', final_img_2)

# displaying the sketch image
cv2.imshow('image', numpy_vertical_concat)
print("Press 'Esc' button to exit or Press 's' to save the image and exit.")

k = cv2.waitKey(0)
# if escape is pressed
if k == 27:
    cv2.destroyAllWindows()
# save the output image
elif k == ord('s'):
    cv2.imwrite('output.png', final_img)
    cv2.imwrite('combined.png',numpy_vertical_concat)
    cv2.destroyAllWindows()
