#Qualities of Image features:
#1. Features are qualities of an object
#2. Salient attributes or components of an object within an image scene
#3. Ideally invariant to transformations
#4. May be identified by classifiers

#Detection != Recognition
#Detection is the step prior to recognition

#2 algorithms: Template Matching and Haar Cascading

#Template matching
#Searches for similar pattern between two images by sliding a source template image for matching
#A perfect match means white (a very bright spot) and no match means black color
#Limitation: Not scale invariant, not rotation invariant, requires having a well-formed template and making input assumptions

import numpy as np 
import cv2

template = cv2.imread('template1.jpg', 0)
frame = cv2.imread('tomato2.jpg', 0)

cv2.imshow('Frame', frame)
cv2.imshow('Template', template)

result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

#Maximum brightness
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)
cv2.circle(result, max_loc, 15, 255, 2)

cv2.imshow('Matching', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Not quite a perfect match