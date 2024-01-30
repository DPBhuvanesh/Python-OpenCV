import cv2 as cv

img = cv.imread('photos/park.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#convertion of image to gray filter

cv.imshow('gray',gray)

cv.waitKey(0)