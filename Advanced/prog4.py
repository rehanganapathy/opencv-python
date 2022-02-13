#bitwise operations
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(390,390),255,-1)
circle=cv.circle(blank.copy(), (200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR  non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR  non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT:inverts the binary colour
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)