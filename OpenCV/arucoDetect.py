import cv2

aruco = cv2.aruco
dictionary = cv2.aruco.getPredefinedDictionary(aruco.DICT_4X4_50)


# write the markers
# for i in range(50):
# 	marker = aruco.drawMarker(dictionary, i, 100)
# 	cv2.imwrite('aruco/{:02d}.png'.format(i),marker)
# 	print("success")

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	if ret:
		corners, ids , rej= aruco.detectMarkers(frame,dictionary)
		frame = aruco.drawDetectedMarkers(frame,corners,ids)
		

		if cv2.waitKey(100)  == ord('q'):
			cv2.imwrite('aruco/drawarucoqq.jpg',frame)
			print("successful write")
			break

		cv2.imshow("try",frame)
		cv2.waitKey(1)
