import cv2
import numpy as np


video_path = '/Users/bigphess/Desktop/omnidirection/res/rabbit_250fps.mp4'
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(video_path)

while True:
	ret, frame = cap2.read()
	# image = cv2.imread('/Users/bigphess/Downloads/IMG_6453.JPG')
	

	debug = frame
	if cv2.waitKey(100) & 0xFF == ord('q'):
		cv2.imwrite('/Users/bigphess/Desktop/xu.jpg',debug)
		print("successful write")
		break

	# h,w,ch = debug.shape

	print('the size of the frame is {} and {}'.format(debug.shape[1],debug.shape[0]))
	cv2.imshow('??', frame)
	cv2.waitKey(0)
	break

	
	# debug = cv2.logPolar(frame,(debug.shape[0]/2,debug.shape[1]/2),100,cv2.WARP_FILL_OUTLIERS)


	
	
	
	# cv2.waitKey(1)


