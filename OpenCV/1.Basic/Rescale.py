import cv2 as cv


def rescaleframe(frame,scale):# can be use for photos,video,live video
    
    width = int( frame.shape[1] * scale)     #values must be in integer
    
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) #resizing

    
img = cv.imread('photos/cat.jpg') #rescaling a img

rescale_img=rescaleframe(img,scale=.1) #setting its scale and calling a function

cv.imshow('cat',rescale_img) #reading the frame

cap = cv.VideoCapture("Video/Catwalk.mp4") #read video

while True: #use while true to run the video
    isTrue,frame = cap.read()  #set cap.read()
    
    rescale = rescaleframe(frame,scale = .2)#setting scale to 0.2 and calling function
    cv.imshow('Video',rescale) #to run the video    
    
    if cv.waitKey(20) & 0xFF==ord('d'): # delay 20 ms and d to break
        break
    
cap.release() #stop the video
cv.destroyAllWindows() #close the windows