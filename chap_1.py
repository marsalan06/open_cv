import cv2 as cv
#print(cv.__version__)

img=cv.imread("lena.jpg")

# cv.imshow("img",img)
# cv.waitKey(0) #0 is infinte while 1000 is 1s

#cap=cv.VideoCapture("testVideo.mp4") #video
cap=cv.VideoCapture(0) #webcam 
cap.set(3,640) #set height '3'
cap.set(4,480)#set width '4'
cap.set(10,100) #set brightness '10'
while True:
    success,img=cap.read() #read in img and success is a boolean that video exist
    img=cv.flip(img,1) #in cases of mirror   
    cv.imshow("video",img) #showed the video 
    if cv.waitKey(1) & 0xFF==ord('q'): #wait (1)
        break 

cap.release()
cv.destroyAllWindows()