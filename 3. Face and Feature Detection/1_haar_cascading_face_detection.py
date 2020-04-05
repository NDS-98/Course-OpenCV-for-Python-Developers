#Haar Cascade Method
#1. A form of feature-based machine learning
#2. Uses pretrained images of lebeled positives and negatives
#3. Runs through thousands of classifiers in a cascaded manner
#4. Use case: detect faces in the image and draw bounding boxes

#There may be false positives and false negatives

import numpy as np 
import cv2

img = cv2.imread('faces.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

path = 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(path)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))
print('No. of faces found: {}'.format(len(faces)))

for(x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), 2)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()