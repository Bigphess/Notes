import numpy as np
import cv2 as cv
# 返回所有图片路径的奇怪包包
import glob
import json
import time



# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# 一共的点数是6乘7个，每个点需要三个方向的坐标（即XYZ三个方向的位置的点，
# 这里为了容易判断所以都默认Z方向的点是0）
objp = np.zeros((8*9,3), np.float32)
# 选中这个东西里面的所有行的前两项
# mgrid输出出来的是：1.一个7行每行分别全是0，1...6的数列 2.一个7行每行是0,1,2,3,4,5的数列
# T把这个矩阵转至了，然后reshape成了一个两列的数组，就可以替代原来数组里面的前两列
objp[:,:2] = np.mgrid[0:9,0:8].T.reshape(-1,2)


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


# 读取上级目录的所有jpg文件，也可以用这个命令指定函数
images = glob.glob('*.jpg')

# objpoints.append(objp)

for fname in images:
    img = cv.imread(fname)

    # cv.imshow("fname",img)
    # cv.waitKey(0)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (9,8), None)
    # If found, add object points, image points (after refining them)
    
    if ret == True:

    	# 每一个点都必须对应一个objp的数组，所以要放在循环里面
        objpoints.append(objp)
        # print(objpoints,"\n---------------------------")

        # 重新定义点的位置，第三个参数是searchWindow的点的一半
        # 只是为了提高点的准确性！！！
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (9,8), corners, ret)
        cv.imshow('img', img)
        cv.waitKey(0)
cv.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(mtx,"\n",dist)


# 这部分是开始检测结果了
# img = cv.imread('left12.jpg')
# h,  w = img.shape[:2]
# newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# # undistort
# dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# # crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imshow("yahaha",dst)
# cv.waitKey(0)




# # 尝试储存到xml里面
# doc = Document()
# calibrateCamera = doc.createElement("calibrateCamera")
# doc.appendChild(calibrateCamera)
# calibrateTime = doc.createElement("calibrateTime")
# calibrateCamera.appendChild(calibrateTime)

# # time
# time = time.asctime( time.localtime(time.time()) )
# currenttime = doc.createTextNode(time)
# calibrateTime.appendChild(currenttime)

# # camera matrix
# cameraMatric = doc.createElement("cameraMatric")
# calibrateCamera.appendChild(cameraMatric)
# rows = doc.createElement("rows")
# cameraMatric.appendChild(rows)
# rows.appendChild(doc.createTextNode("3"))

# cols = doc.createElement("cols")
# cameraMatric.appendChild(cols)
# cols.appendChild(doc.createTextNode("3"))

# data = doc.createElement("data")
# cameraMatric.appendChild(data)
# data.appendChild(doc.createTextNode(','.join(mtx)))
##########################################


#################存到json里面
cameraMat = mtx.tolist()
disCo = dist.tolist()

time = time.asctime( time.localtime(time.time()))
cameraMatric = {"rows":3,"cols":3,"data":cameraMat}
distortion = {"rows":1,"cols":4,"data":disCo} 
havetry = {"xi":324}
wholeData = {"calibration time":time,"cameraMatric":cameraMatric,"distortion co":distortion,"try":havetry}
# wholeData = [time,cameraMatric]
print(wholeData)
with open("logicool_calibration.json","w",encoding = "utf-8") as f:
	f.write(json.dumps(wholeData,indent = 2))
# print(wholeData)

with open("logicool_calibration.json","r") as f:
	df = json.load(f)

print(df["calibration time"])
print(type(df["cameraMatric"]["data"]))

