import numpy as np
import cv2 as cv

img=np.zeros((512,512,3),np.uint8)

cv.putText(img,"PAK VS SA",(160,50),cv.FONT_HERSHEY_COMPLEX,1,(0,250,0),1)
cv.rectangle(img,(120,150),(380,200),(25,120,200),cv.FILLED)
cv.rectangle(img,(340,150),(380,200),(255,255,255),2)
cv.rectangle(img,(120,150),(160,200),(255,255,255),2)

cv.rectangle(img,(120,250),(170,300),(0,250,0),cv.FILLED)
cv.circle(img,(145,272),15,(255,255,255),cv.FILLED)
cv.circle(img,(148,272),15,(0,255,0),cv.FILLED)
cv.circle(img,(150,272),5,(255,255,255),cv.FILLED)

cv.rectangle(img,(330,250),(380,300),(0,250,0),cv.FILLED)
cv.circle(img,(355,275),10,(0,0,0),cv.FILLED)
cv.circle(img,(355,278),10,(0,255,255),cv.FILLED)
cv.circle(img,(355,281),10,(0,255,50),cv.FILLED)
cv.circle(img,(355,284),10,(255,255,255),cv.FILLED)
cv.circle(img,(355,287),10,(0,0,255),cv.FILLED)
cv.circle(img,(355,290),10,(255,0,0),cv.FILLED)
cv.circle(img,(355,292),8,(0,255,0),cv.FILLED)

cv.imshow('img',img)
cv.waitKey(0)

cv.destroyAllWindows()