import numpy as np
import cv2

#Loading image
img = cv2.imread('opencv-logo.png')

#Displaying image
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)

cv2.waitKey(0)

#Writing image to a file in another format
cv2.imwrite('logo_output.jpg',img)