#thresholding in opencv
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow(('GRAY'),gray)

#Simple Thresholding
threshold, thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

threshold, thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse',thresh_inv)

#Adaptive Thresholding: opencv itself finds optimal threshold values
adaptive_tresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive',adaptive_tresh)

cv.waitKey(0)