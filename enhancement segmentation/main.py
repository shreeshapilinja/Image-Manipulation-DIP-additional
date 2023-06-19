import cv2
import numpy as np

img = cv2.imread('lena.png')
img_g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # for enhancing convert color to gray scale image

# OR directly to gray scale by passing 0 : img = cv2.imread('lena.png',0)

img_equalize = cv2.equalizeHist(img_g)

result = np.hstack((img_g,img_equalize))

# cv2.imwrite('result.png',result)
# cv2.threshold(source,thresholdValue, maxVal ,thresholdingTechinques)

ret,img_thresh = cv2.threshold(img_equalize,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original Image',img)
cv2.imshow('Original Image Converted to grayscale',img_g)
cv2.imshow('Enhanced Image',img_equalize)
cv2.imshow('Original Image & Enhanced Image',result)
cv2.imshow('Segmented Image',img_thresh)
'''
cv2.imwrite('Original Image.png',img)
cv2.imwrite('Original Image Converted to grayscale.png',img_g)
cv2.imwrite('Enhanced Image.png',img_equalize)
cv2.imwrite('Original Image & Enhanced Image.png',result)
cv2.imwrite('Segmented Image.png',img_thresh)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()