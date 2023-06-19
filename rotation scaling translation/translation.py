# translation

import cv2
import numpy as np
M = np.float32([[1,0,100],[0,1,50]])
try:
	img = cv2.imread('camaraman.png')
	(rows,cols)=img.shape[:2]
	img_translation = cv2.warpAffine(img,M,(cols,rows))
	cv2.imwrite('translation.png',img_translation)
	cv2.imshow('translation',img_translation)
	cv2.waitKey()
except IOError:
	print('Error while readning files !!!')