import cv2 as cv

img=cv.imread("lena.jpg")

#grayscale 
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#blur image
img_blur=cv.GaussianBlur(img,(51,51),0) #blur is dependent on the (x,y), its odd and greater the value more it blur

#edges 
img_edge=cv.Canny(img,5,100)

cv.imshow("img",img)
#cv.imshow("img_blur",img_blur)
cv.imshow("edges",img_edge)
cv.waitKey(0)

cv.destroyAllWindows()