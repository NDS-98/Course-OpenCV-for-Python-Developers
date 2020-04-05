#Adaptive thresholding looks into the local neighbourhood of the image to determine whether a relative threshold is met
#Doesn't use a global threshold
#Hence can counteract issues like uneven lighting

import numpy as np 
import cv2

#We consider only black and white images for segmentation
img = cv2.imread('sudoku.png', 0)
cv2.imshow('Original', img)

ret, thresh_basic = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Basic Binary', thresh_basic)

thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adaptive Threshold', thresh_adapt)
#We can still try to improve it by using dilation and erosion

cv2.waitKey(0)
cv2.destroyAllWindows()