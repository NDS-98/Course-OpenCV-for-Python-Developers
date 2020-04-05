import numpy as np 
import cv2

color = cv2.imread('butterfly.jpg',1)

#Converting to grayscale
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray_butterfly.jpg',gray)

#Adding 4th alpha channel - transparency channel
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

#Pixel having high alpha value are non-transparent and vice versa
rgba = cv2.merge((b,g,r,g))
cv2.imwrite('rgba_butterfly.png',rgba)
#jpeg images do not support image transparence hence png
