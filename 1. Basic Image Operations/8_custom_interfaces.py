#Creating a circle in video and capturing mouse clicks
import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

color = (0,255,0) #green
line_width = 3
#line_width -1 means completely fill in the circle
radius = 50
point = (0,0) #initial centre of circle


def click(event, x, y, flags, param):
	global point
	if(event==cv2.EVENT_LBUTTONDOWN):
		print('Pressed', x, y)
		point = (x,y)


cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',click)

while(True):
	ret, frame = cap.read()

	# frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
	cv2.circle(frame, point, radius, color, line_width)
	cv2.imshow('Frame', frame)

	ch = cv2.waitKey(1)
	if(ch & 0xFF==ord('q')):
		break

cap.release()
cv2.destroyAllWindows()
