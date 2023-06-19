# rotation

import cv2
import numpy as np
try:
	img = cv2.imread('camaraman.png')
	(rows,cols)=img.shape[:2]
	M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
	rotation = cv2.warpAffine(img,M,(cols,rows))
	cv2.imwrite('rotation.png',rotation)
	cv2.imshow('rotation',rotation)
	cv2.waitKey()
except IOError:
	print('Error while readning files !!!')