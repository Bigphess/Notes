import numpy as np
import cv2 
# 返回所有图片路径的奇怪包包
import glob
import json
import time
import os



# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.00001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# 这里为了容易判断所以都默认Z方向的点是0）
chessBoardSize = [9,8]
# objp需要全都变成一个1
objp = np.zeros((1,chessBoardSize[0]*chessBoardSize[1],3), np.float32)
# 选中这个东西里面的所有行的前两项
# mgrid输出出来的是：1.一个7行每行分别全是0，1...6的数列 2.一个7行每行是0,1,2,3,4,5的数列
# T把这个矩阵转至了，然后reshape成了一个两列的数组，就可以替代原来数组里面的前两列
objp[0,:,:2] = np.mgrid[0:chessBoardSize[0],0:chessBoardSize[1]].T.reshape(-1,2)


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


# 读取上级目录的所有jpg文件，也可以用这个命令指定函数
images = glob.glob('*.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (chessBoardSize[0],chessBoardSize[1]), None)
    # If found, add object points, image points (after refining them)
    
    if ret == True:

    	# 每一个点都必须对应一个objp的数组，所以要放在循环里面
        objpoints.append(objp)
        # 重新定义点的位置，第三个参数是searchWindow的点的一半
        # 只是为了提高点的准确性！！！
        corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (chessBoardSize[0],chessBoardSize[1]), corners2, ret)
        cv2.imshow('img', img)
        # cv2.waitKey(100)
cv2.destroyAllWindows()


######################## 这部分更容易理解各个参数的类型
# N_OK = len(objpoints)
# K = np.zeros((3, 3))
# D = np.zeros((4, 1))
# xi = 0
# rvecs = [np.zeros((1, 1, 3), dtype=np.float64) for i in range(N_OK)]
# tvecs = [np.zeros((1, 1, 3), dtype=np.float64) for i in range(N_OK)]

# ########################标定
retval,K,xi,D,rvecs,tvecs,inx = cv2.omnidir.calibrate(objpoints,imgpoints,gray.shape[::-1],None,None,None,cv2.omnidir.CALIB_USE_GUESS,criteria)




####################### 这部分是开始检测结果（扭回来

# # undistort
new_Size = np.array([1200,1200])
Knew = np.array([[new_Size[1] / 4, 0, new_Size[1]/2],
	[0, new_Size[0] / 4, new_Size[0]/2],
	[0,  0, 1]])

images = glob.glob("*.jpg")
for img in images:
	dis = cv2.imread(img)
	undisImg = cv2.omnidir.undistortImage(
		dis, K, D, xi, 
		cv2.omnidir.RECTIFY_PERSPECTIVE,
		Knew,
		new_size = (1500,1500))
	cv2.imshow("undistort",undisImg)
	cv2.waitKey(0)





#################存到json里面
cameraMat = K.tolist()
disCo = D.tolist()
xi = xi.tolist()

time = time.asctime( time.localtime(time.time()))
K = {"rows":3,"cols":3,"data":cameraMat}
D = {"rows":1,"cols":4,"data":disCo} 
xi = {"xi":xi}
wholeData = {"calibration time":time,"cameraMatric":K,"distortion co":D,"try":xi}
with open("logicool_calibration.json","w",encoding = "utf-8") as f:
	f.write(json.dumps(wholeData,indent = 2))

####读取信息
with open("logicool_calibration.json","r") as f:
	df = json.load(f)

# print(df["calibration time"])
# print(type(df["cameraMatric"]["data"]))

