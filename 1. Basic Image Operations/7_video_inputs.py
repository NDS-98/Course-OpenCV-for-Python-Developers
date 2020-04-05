import numpy as np 
import cv2

#waitKey(0) displays the window infinitely until any keypress
#waitKey(1) will display a frame for 1ms, after which it will be automatically closed

#Captures video using the camera
cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
	cv2.imshow('Frame', frame)

	ch = cv2.waitKey(1)
	#Key for breaking out of loop
	if ch & 0xFF==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()