#basic functions to draw
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')

import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#paint the entire blank image with a particular color
blank[200:300 ]=0,255,0
cv.imshow('Green',blank)

#Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow('rectangle',blank)
cv.waitKey(0)

#Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),30,(0,255,0),thickness=-1)
cv.imshow('circle',blank)
cv.waitKey(0)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Rehan!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)

