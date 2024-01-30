import cv2 as cv

cap = cv.VideoCapture("Video/Catwalk.mp4") #read video

while True: #use while true to run the video
    isTrue,frame = cap.read()  #set cap.read()
    
    cv.imshow('Video',frame) #to run the video
    
    if cv.waitKey(20) & 0xFF==ord('d'): # delay 20 ms and d to break
        break
    
cap.release() #stop the video
cv.destroyAllWindows() #close the windows