import cv2 as cv
import numpy as np

#numpy to create a blabk image and uint8 is image type
blank = np.zeros((500,700,3),dtype='uint8')
#3 indicates the brg channel for color , 500 and 700 for resolution

blank [:] = [255,0,0] # set full image to blue color

cv.imshow('Blank',blank)
#shows the blank

cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
#(0,0) is origin and (250,250) pixels , so 0,0 to 250,250 and color and thickness
cv.imshow('rectangle',blank)

cv.circle(blank,(250,250),70,(0,0,255),thickness = -1) 
# 70 is radius 

cv.imshow('circle',blank)

cv.line(blank,(0,0),(250,250),(0,0,255),thickness =5)
#(o,o) is orgin to (250,250) is pixel 

cv.imshow('line',blank)

cv.waitKey(0)