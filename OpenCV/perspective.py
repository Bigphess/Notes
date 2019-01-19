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


	rows, cols,  channels = debug.shape
	# print(cols,rows)

	srcQuad = np.float32([[0,0],[cols -1,0],[cols - 1, rows - 1],[0, rows -1]])
	
# 变换之后的四角
	dstQuad = np.float32([[cols * 0.05,rows * 0.33],
			[cols * 0.9, rows * 0.25],
			[cols * 0.8 ,rows * 0.9],
			[cols * 0.2, rows * 0.7]])

# 得到参数
	persMat = cv2.getPerspectiveTransform(srcQuad,dstQuad)
	# 按照这个参数变换图片
	warp = cv2.warpPerspective(debug, persMat,(rows,cols))
	cv2.imshow('??',warp)
	
	cv2.waitKey(1)


