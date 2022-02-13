#masking: allows focus on certain aspects of an image 
from pickletools import uint8
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img)
#blank needs to have same dimension as that of img else masking wont work
blank=np.zeros(img.shape[:2],dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2+45 ,img.shape[0]//2), 100, 255, -1)


rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
weird_shape = cv.bitwise_and(circle,rectangle)
masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)
cv.imshow('Weird Shape', weird_shape)

cv.waitKey(0)