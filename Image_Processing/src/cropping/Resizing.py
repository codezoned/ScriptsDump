"""
This is small script used for resizing any image. Resizing is useful whenever we have an image dataset having
images of different resolutions. Any model would accept a fixed sized image and so we need to resize the image.

OpenCV provides a direct implementation of resizing the image.
There are 3 arguments in resize()
1. The image to be resized
2. The desired width and height in a tuple.
3. The kind of interpolation. (Choose from AREA, CUBIC, LINEAR, and NEAREST)
"""
import cv2
dimensions = input("Enter width and height : ").split()
width = int(dimensions[0])
height = int(dimensions[1])

image = cv2.imread("lenna.png")
resized_image = cv2.resize(image , (width, height), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
