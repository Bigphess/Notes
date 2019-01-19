import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	# image = cv2.imread('/Users/bigphess/Downloads/IMG_6453.JPG')
	

	debug = frame
	if cv2.waitKey(100) & 0xFF == ord('q'):
		cv2.imwrite('/Users/bigphess/Desktop/xu.jpg',debug)
		print("successful write")
		break

	h,w,ch = debug.shape

	# print(type(debug.shape[0]))
	# break
	debug = cv2.logPolar(frame,(debug.shape[0]/2,debug.shape[1]/2),100,cv2.WARP_FILL_OUTLIERS)


	
	cv2.imshow('??',debug)
	
	cv2.waitKey(1)


