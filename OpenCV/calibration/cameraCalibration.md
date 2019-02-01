# Camera Calibration
[Calibration on Python OpenCV 4.0.1](https://docs.opencv.org/4.0.1/dc/dbb/tutorial_py_calibration.html)
## goal
* camera distortion的类型
* 如何找到intrinsic and extrinsic properties
* 基于上面的参数，如何undistort images

## basic
* pinhole的相机的distortion
	* radial distortion 辐射状
		* 直线会变成曲线
		* 离画面中心越远，辐射的扭曲越强烈
		* 公式和离画面中心的距离r有关
	* tangential distortion 正切状
		* 因为镜头不是完全平行与平面，所以有的部分可能看起来更近
	* 上面两个是distortion需要的参数（五个参数）
* 除此之外，还需要相机本身的参数
	* Intrinsic parameters（每个相机都不一样）
		* focal length ( fx,fy) 
		* optical centers ( cx,cy)
		* 这两个参数可以形成camera metrix，3乘3的
	* Extrinsic parameters （取决于旋转和平移向量）
* 校准方法
	* 需要一个比较标准的图片（比如棋盘）
	* 找到一些已经知道相关关系的点（比如四个角）
	* 知道现实中的坐标和图片中的坐标
	* 为了更好的结果，应该测试至少10个不同的patterns

## code
相机静止，棋盘被放在不同的位置和方向 -> 为了简单，可以让棋盘在Z（Z = 0）方向上不变，就移动相机（？）。3D点是object point，2D点是image points
* setup
	* cv.findChessboardCorners()来找到棋盘的corner
		* 逐帧检查是不是有棋盘
		* 得到棋盘之后，储存corner在list里面
	* 找到之后，可以用
		* increase their accuracy using cv.cornerSubPix().
		* draw the pattern using cv.drawChessboardCorners().
* calibration：cv.calibrateCamera() 
	* 返回camera matrix, distortion coefficients, rotation and translation vectors
	* 参数是现实中的点和图片中的点之类的
* undistortion（把图片还原成原来的样子）
	* refine camera matrix： cv.getOptimalNewCameraMatrix
	* 方法一： cv.undistort()（用上边得到的矩阵当参数）
	* 方法二： cv.remap


# Omnidirectional Cameara Calibration
[omi camera calibration](  )
## calibration
* 注意使用的时候要使用特定的calibration（omnidir）
* [使用时遇到错误信息](https://stackoverflow.com/questions/34355059/opencv-python-how-to-format-numpy-arrays-when-using-calibration-functions)
* 初始化objp的时候大小应该是（1，格子大小，3）
* 具体代码在 CaliCodeOmni.py

## 还原相机图片
* undistortImage
	* 原图
	* 想得到的perspective校准的结果
	* 相机参数K，D，xi
		* The xi is a single value variable of Mei's model
	* KNew and new_size are the camera matrix and image size for rectified image.
		* Knew应该谨慎选择，并且根据相机
		* 官方有推荐的Knew
		* new_size需要强调这个参数，需要是tuple类型的（我也不知道为啥）
	* 校正的类型

# 结果存在json里面。
```
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
```


# 实践
## 使用系统自带图片的相机的标定实践
* 使用下载好的标定板（棋盘），拍摄图片，不少于3张，10到20张左右（/samples/data/left01-12.jpg)
    * 因为是系统给好的图片，所以标定出来是sample里面相机的数据
