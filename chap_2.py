import cv2 as cv
import numpy as np 

img=cv.imread("lena.jpg")

#grayscale 
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#blur image
img_blur=cv.GaussianBlur(img,(51,51),0) #blur is dependent on the (x,y), its odd and greater the value more it blur

#edges 
img_edge=cv.Canny(img,110,210) #larger value finds initial edges and smaller on links them
#to have a better result keep values in range of 100 and 200  

kernel = np.ones((5,5),np.uint8)
#dilation : an edge if is somewhat disconected , we use dilation to enhance it better and than use canny
img_dilation=cv.dilate(img_edge,kernel,iterations=1) #we need the canny image , 
#a matrix to slide over the image, no of iterations ,to get desired thikness 

img_erroded= cv.erode(img_dilation,kernel,iterations=1) #opposite of dilations 

# cv.imshow("img",img)
# #cv.imshow("img_blur",img_blu
cv.imshow("edges",img_edge)
cv.imshow("dilated",img_dilation)
cv.imshow("erroder",img_erroded)
cv.waitKey(0)

cv.destroyAllWindows()