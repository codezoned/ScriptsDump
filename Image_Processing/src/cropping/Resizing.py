import cv2
dimensions = input("Enter width and height : ").split()
width = int(dimensions[0])
height = int(dimensions[1])

image = cv2.imread("lenna.png")
resized_image = cv2.resize(image , (width, height), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
