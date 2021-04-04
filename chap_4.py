import numpy as np
import cv2 as cv

img=np.zeros((512,512,3),np.uint8) #black canvas ,shape is 512,512 for rgb we place 512,512,3

#img[:]=255,0,0 #list values in terms of slicing , : is for complete 

#while a particular segement is like below, 255,0,0 is blue 
#img[100:200,200:300]=255,0,0

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3) #bgr color format 
#if image shape isnt know use img.shape[1], img.shape[0] for complete

cv.rectangle(img,(40,79),(200,300),(255,0,0),3) #for rectangle, 
                                            #in place of thickness to fill complete, cv.FILLED 

cv.circle(img,(400,50),45,(43,154,100),4) # starting coordinate and radius 

cv.putText(img,"OPEN CV",(250,350),cv.FONT_HERSHEY_COMPLEX,1,(123,21,200),1) 
        # img, text, coordinate , font type, scale , color, thickness



cv.imshow('img',img)
cv.waitKey(0)

cv.destroyAllWindows()