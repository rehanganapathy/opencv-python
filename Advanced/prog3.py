#smoothening and blurring techniques
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#averaging
average=cv.blur(img,(3,3))
cv.imshow('Averaging',average)

#gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('gauss',gauss)

#median blur, used for noise reduction too
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral, retains edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)