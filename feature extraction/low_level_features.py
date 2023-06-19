import cv2
import numpy as np

img = cv2.imread('lena.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray scale image',gray)

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)

sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=5)
sobel_edges = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
laplacian = cv2.Laplacian(blur, cv2.CV_64F) 
canny_edges = cv2.Canny(blur, 100, 200) 

cv2.imshow('Filtered output',blur)
cv2.imshow('Sobel Edges',sobel_edges)
cv2.imshow('laplacian',laplacian)
cv2.imshow('Canny Edge detection',canny_edges)

blur_median = cv2.medianBlur(gray,5)
cv2.imshow('Blur Median',blur_median)

bilateral = cv2.bilateralFilter(gray,15,75,75)
cv2.imshow('Bilateral Filter',bilateral)

kernel = cv2.getGaborKernel((31,31),5,0,10,0.5,0,ktype=cv2.CV_32F)
gabor = cv2.filter2D(gray,cv2.CV_8UC3,kernel)
cv2.imshow('Gabor Filter',gabor)

cv2.waitKey(0)
cv2.destroyAllWindows()