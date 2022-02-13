#this file experiments with contour detection in opencv
#contours and edges are actually different concepts in image processing 
#Contour detection is mainly used to determine the shape of closed objects as the process to find the contours is to check for the continuous points having same color intensity 
#whereas edge detection is carried by detecting the change in the color intensity
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

cv.imshow('Gray', gray)
cv.imshow('Cats', img)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)