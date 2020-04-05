#Can help break the objects if there is an overlap in our segmentation process
import numpy as np 
import cv2

img = cv2.imread('tomato2.jpg', 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Thresholding hue channel
res, thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Thresh', thresh)

#Canny edge Detection
edges = cv2.Canny(img, 100, 70)
cv2.imshow('Canny', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()