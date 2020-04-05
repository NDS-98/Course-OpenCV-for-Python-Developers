#Binary images are pure non-aliased black and white images and act as a mask on the source image
#One of the ways of obtaining binary images is the thresholding algorithm
#Consider a threshold value and mask every pixel with value>threshold to be 1 and vice-versa

import numpy as np 
import cv2

#Loading as a black and white image (0)
bw = cv2.imread('detect_blob.png', 0)
height, width = bw.shape[0:2]
cv2.imshow('Original BW', bw)

#binary image - 1 channel
binary = np.zeros([height, width, 1], 'uint8')

thresh = 85
#uint8 -> 2^8=255 -> Range = [0,255]

for row in range(0, height):
	for col in range(0, width):
		if(bw[row][col]>thresh):
			binary[row][col] = 255

#This is a very slow method
cv2.imshow('Slow Binary', binary)

#Faster in-built fn
ret, thresh = cv2.threshold(bw, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow('CV Threshold', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()