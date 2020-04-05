#Create a script which draws circles around all eyes in an image
#Utilize the Haar Cascade method, leveraging the pretrained haarcascade_eye.xml file provided
#Try to reduce the number of false positives and false negatives as much as possible
#False positive - Drawing a circle where there isn't an eye
#False negative - Not drawing a circle where there is an eye

import numpy as np 
import cv2

img = cv2.imread('faces.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

path = 'HaarCascadeClassifiers/haarcascade_eye.xml'

eye_cascade = cv2.CascadeClassifier(path)

eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=20, minSize=(10,10))
print('No. of eyes found: {}'.format(len(eyes)))

for(x, y, w, h) in eyes:
	#Centre of eye for drawing circle
	xc = (x + x+w)/2
	yc = (y + y+h)/2
	radius = w/2
	cv2.circle(img, (int(xc), int(yc)), int(radius), (255, 0, 0), 2)

# img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
cv2.imshow('Eyes', img)

# cv2.imwrite('challenge3_faces.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#False positives and negatives can be seen in the result.
#The result is only as good as the training data