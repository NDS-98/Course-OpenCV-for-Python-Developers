#For all objects in the fuzzy image, segment them out, draw them on a blank image, and print the perimeter and area
#Only draw large objects (area of greater than 1000 px2)
#Each object should be drawn with its own color (it does not need to match the source image color)
#TIP: Consider smoothing the image before segmenting

import numpy as np 
import cv2
import random    #For drawing random colors

img = cv2.imread('fuzzy.png', 1)
cv2.imshow('Original', img)

#Converting to grayscale so that we can do thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Little trick: Adaptive thresholding will work better if we use blur considering our fuzzy image
blur = cv2.GaussianBlur(gray, (3,3), 0)

#Adaptive thresholding
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow('Binary', thresh)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('No. of contours found: {}'.format(len(contours)))

#We need to draw only large objects/contours, hence filtering is needed
filtered = []
for c in contours:
	if(cv2.contourArea(c)<1000):
		continue
	filtered.append(c)

print('No. of large contours: {}'.format(len(filtered)))

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
for c in filtered:
	col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    #random color
	cv2.drawContours(objects, [c], -1, col, -1)
	#First -1 indicates to draw all the contours in the contour list passed
	#Second -1 indicates to fill in the contour completely
	area = cv2.contourArea(c)
	perimeter = cv2.arcLength(c, True)

	print('Area = {}, Perimeter = {}'.format(area, perimeter))

cv2.imshow('Contours', objects)

# cv2.imwrite('challenge2_original.jpg', img)
# cv2.imwrite('challenge2_binary.jpg', thresh)
# cv2.imwrite('challenge2_contours.jpg', objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
