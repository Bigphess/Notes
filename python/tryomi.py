import cv2
import numpy as np




def angles_to_px(diameter, aperture, a):
        r = (np.pi / 2 - a[1]) * diameter / aperture
        theta = a[0]
        x = r * np.sin(theta) + diameter / 2
        y = r * -np.cos(theta) + diameter / 2
        return np.array([x, y])



def vec_to_angles(vec):
        return np.array([
            np.arctan2(vec[0], vec[2]),
            np.arcsin(vec[1] / np.linalg.norm(vec))
        ])


target_aperture = 140 * np.pi / 180
prj_pos = np.array([0, -7.49213, 18.5437])
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
	

	dstQuad = np.float32([[cols * 0.05,rows * 0.33],
			[cols * 0.9, rows * 0.25],
			[cols * 0.8 ,rows * 0.9],
			[cols * 0.2, rows * 0.7]])

	persMat = cv2.getPerspectiveTransform(srcQuad,dstQuad)
	warp = cv2.warpPerspective(debug, persMat,(rows,cols))
	cv2.imshow('??',warp)
	# debug = cv2.circle(debug,
 #                           (int(frame.shape[1] / 2), int(frame.shape[0] / 2)),
 #                           int(frame.shape[0] / 2 * target_aperture / (235 * np.pi / 180)),
 #                           (0, 0, 255),
 #                           2)


	# debug = cv2.circle(debug,
 #                           tuple(angles_to_px(frame.shape[0], 235 * np.pi / 180,
 #                                                   vec_to_angles(prj_pos)).astype(np.int)),
 #                           10,
 #                           (0, 0, 255),
 #                           -1)

	# cv2.imshow('have a try',debug)
	cv2.waitKey(1)


