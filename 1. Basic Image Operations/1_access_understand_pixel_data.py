import numpy
import cv2

img = cv2.imread('opencv-logo.png',1)
#1 indicates color, 0 indicats black and white

print(img)
print('No of rows = '+str(len(img)))
print('No of columns = '+str(len(img[0])))
print('No of channels in img = '+str(len(img[0][0])))
print('Shape = '+str(img.shape))
print('Total no. of pixels = '+str(img.size))