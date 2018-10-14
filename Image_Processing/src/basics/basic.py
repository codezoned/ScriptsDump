# coding: utf8
# Python implementation of basic image processing
# Author: Caio Cesar Viana da Silva
# Install scikit-image: pip install scikit-image

# import skimage.io as io
# from matplotlib import pyplot as plt
# import numpy as np
# from skimage.transform import AffineTransform, warp
# import skimage.transform  as ski

#OPENING AN IMAGE

def open_img(img_path):
	import skimage.io as io

	img = io.imread(img_path)
	io.imshow(img)
	io.show()
	return img


#VISUALIZE HISTOGRAM

def histogram_img(img_path):
	import skimage.io as io
	from matplotlib import pyplot as plt

	img = io.imread(img_path)
	plt.hist(img.ravel(),256,[0,256])
	plt.show()

#RGB HISTOGRAM

def histogram_rgb_img(img_path):
	import skimage.io as io
	from matplotlib import pyplot as plt

	img = io.imread(img_path) 
	color = [ 'r','g','b']
	for i, c in enumerate(color) :
	    plt.hist(img[:,:,i].flatten(),256, color=c)
	plt.show()


#RGB TO GRAYSCALE

def rgb_2_gray(img_path):
	import numpy as np
	import matplotlib.pyplot as plt

	img = open_img(img_path)
	gray = np.dot(img[...,:3], [0.299, 0.587, 0.114])
	plt.imshow(gray, cmap = plt.get_cmap('gray'))
	plt.show()

#SCALING IMAGE

def scaling_img(img_path):
	import skimage.io as io
	import matplotlib.pyplot as plt

	fig = plt.figure(figsize=(1,8))
	img = io.imread(img_path)
	plt.imshow(img)
	plt.show()


#TRANSLATING IMAGE 

def translating_img(img_path, vector):
	import matplotlib.pyplot as plt
	from skimage.transform import AffineTransform, warp

	img = open_img(img_path)
	transform = AffineTransform(translation=vector)
	shifted = warp(img, transform, mode='constant', preserve_range=True)
	plt.imshow(shifted)
	plt.show()

#ROTATING IMAGE

def rotating_img(img_path, degree):
	import skimage.io as io
	import skimage.transform  as ski

	img = open_img(img_path) 
	imgR = ski.rotate(img,degree)
	io.imshow(imgR)
	io.show()


def main():
	
	open_img('test.jpg')
	histogram_img('test.jpg')
	histogram_rgb_img('test.jpg')
	rgb_2_gray('test.jpg')
	scaling_img('test.jpg')
	translating_img('test.jpg',[-100, -100])
	rotating_img('test.jpg',45)

		


if __name__ == "__main__":
    main()