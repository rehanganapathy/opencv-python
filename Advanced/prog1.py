#working with color spaces
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')
import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale',gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

plt.imshow(img)
plt.show()
# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)
cv.waitKey(0)