# Scalling

import cv2
import numpy as np
try:
	img = cv2.imread('camaraman.png')
	(height,width)=img.shape[:2]
	img_scaled = cv2.resize(img,None,fx=1.2,fy=1.2,interpolation = cv2.INTER_LINEAR)
	cv2.imshow('Scaling - linear interpolation',img_scaled)
	cv2.imwrite('Scaling - linear interpolation.png',img_scaled)
	img_scaled = cv2.resize(img,None,fx=1.2,fy=1.2,interpolation = cv2.INTER_CUBIC)
	cv2.imshow('Scaling - Cubic interpolation',img_scaled)
	cv2.imwrite('Scaling - Cubic interpolation.png',img_scaled)
	img_scaled = cv2.resize(img,(600,600),interpolation = cv2.INTER_AREA)
	cv2.imshow('Scaling - Skewed Size',img_scaled)
	cv2.imwrite('Scaling - Skewed Size.png',img_scaled)
	cv2.waitKey()
except IOError:
	print('Error while readning files !!!')