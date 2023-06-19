import cv2
import numpy as np
img = cv2.imread('lena.png')

kernel = np.ones((5,5),np.uint8)
threshold_lower = 100
threshold_upper = 200
edges = cv2.Canny(img,threshold_lower,threshold_upper)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Image',img)
cv2.imshow('Erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)
cv2.imwrite('Image.png',img)
cv2.imwrite('Erosion.png',img_erosion)
cv2.imwrite('Dilation.png',img_dilation)

erosion_edges = cv2.erode(edges, kernel, iterations=1)
dilation_edge = cv2.dilate(edges, kernel, iterations=1)

cv2.imshow('Edge image using Erosion',erosion_edges)
cv2.imshow('Edge image using Dilation',dilation_edge)
#cv2.imwrite('Edge image using Erosion.png',erosion_edges)
cv2.imwrite('Edge image using Dilation.png',dilation_edge)

result = cv2.subtract(img,img_erosion)
cv2.imshow('result after subtraction',result)
cv2.imwrite('result after subtraction.png',result)

cv2.waitKey(0)
cv2.destroyAllWindows()

