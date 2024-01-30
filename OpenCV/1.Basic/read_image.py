import cv2 as cv

img = cv.imread('Photos/cat1.jpg') # reading image

cv.imshow('Cat',img)  # window name and img variable

cv.waitKey(0)