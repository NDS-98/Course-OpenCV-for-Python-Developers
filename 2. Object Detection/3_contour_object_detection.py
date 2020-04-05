#After segmenting out the key areas of an image, next step is to typically identify individual objects
#For this contour implementation is used
#Takes a binary image and creates a fitting closed perimeter around all individual objects seen
#Each perimeter is called a contour
#An iterative enery reduction algorithm - the contours always converge

import numpy as np 
import cv2

img = cv2.imread('detect_blob.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Binary', thresh)

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)  #pink

cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow('Contours', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()