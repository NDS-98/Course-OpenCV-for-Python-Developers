import numpy as np 
import cv2

img = cv2.imread('face_grid.png', 1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow('Original', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow('Split HSV', hsv_split)

#Filter on the saturation channel
ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
#Everything less than 40 will become 0 (black) and greater will become 255 (white)
cv2.imshow('Sat Filter', min_sat)

#Filter on the hue channel
ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
#Indicates inverse of the normal order of threshold
#Makes 0-15 white and everything else black
cv2.imshow('Hue Filter', max_hue)

#Combining the filters
final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow('Final', final)

cv2.waitKey(0)
cv2.destroyAllWindows()
