#color channels
#working with color spaces
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r=cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
#shows color instead of a grayscale image
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

#shows pixel intensity of each colour channel
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged=cv.merge([b,g,r])
cv.imshow('Merged image',merged)
cv.waitKey(0)
