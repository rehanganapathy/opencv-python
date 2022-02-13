import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages ')

import cv2 as cv
img=cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    #only works on live video
   capture.set(3,width)
   capture.set(4,height)

capture=cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows



