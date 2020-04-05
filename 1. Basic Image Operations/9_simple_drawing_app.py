#Able to paint multiple circles onto a white canvas
#Able to select between atleast 2 different colors

#Press q to quit
#Press b to change color to blue and g to change color to green

import numpy as np 
import cv2

#Global variables
canvas = np.ones([500,500,3],'uint8')*255 #white canvas
radius = 3
color = (0,255,0) #initial green color for drawing circle
pressed = False

#Click callback
def click(event, x, y, flags, param):
	global pressed

	if(event==cv2.EVENT_LBUTTONDOWN):
		pressed = True
		cv2.circle(canvas, (x,y), radius, color, -1)
	elif(event==cv2.EVENT_MOUSEMOVE and pressed==True):
		cv2.circle(canvas, (x,y), radius, color, -1)
	elif(event==cv2.EVENT_LBUTTONUP):
		pressed = False

#Window initialization and callback assignment
cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', click)

#Forever draw loop
while(True):
	cv2.imshow('Canvas', canvas)

	#Key capture every 1ms
	ch = cv2.waitKey(1)
	if(ch & 0xFF==ord('q')):
		break
	elif(ch & 0xFF==ord('b')):
		color = (255,0,0)
	elif(ch & 0xFF==ord('g')):
		color = (0,255,0)

cv2.destroyAllWindows()

