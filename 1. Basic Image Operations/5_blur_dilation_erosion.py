#Goal is to make image easier to work with
import numpy as np 
import cv2

#Gaussian blur smoothes an image by averaging pixel values of its neighbours
image = cv2.imread('butterfly.jpg')
cv2.imshow('Original',image)

blur = cv2.GaussianBlur(image,(5,55),0)
cv2.imshow('Blur',blur)

#kernel is needed for dilation and erosion
kernel = np.ones((5,5),'uint8')

#Increases the white portion to increase image clarity
dilate = cv2.dilate(image,kernel,iterations=1)
cv2.imshow('Dilate',dilate)

#Increases the black portion to increase image clarity
erode = cv2.erode(image,kernel,iterations=1)
cv2.imshow('Erode',erode)

cv2.waitKey(0)
cv2.destroyAllWindows()