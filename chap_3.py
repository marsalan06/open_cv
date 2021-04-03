import cv2 as cv 

img=cv.imread("download.jpg")
print(img.shape) #height(y),width(x),bgr(3)
img_resize=cv.resize(img,(300,100)) #(width x,height y)

#h x,w y in terms of range to keep, list slicing 
imgcrop=img_resize[0:250,0:100]

cv.imshow('img',img)
cv.imshow('img_re',img_resize)
cv.imshow("cropped",imgcrop)
cv.waitKey(0)

cv.destroyAllWindows()