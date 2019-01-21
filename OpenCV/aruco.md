# Detection of ArUco Markers
* pose estimation：
	* finding correspondences between points in the real environment and their 2d image projection
	* 因为不好实现所以经常使用marker来实现寻找
	* 一种方法：binary square fiducial markers
```
#include <opencv2/aruco.hpp>
```

## Markers and Dictionaries
* 外部是黑色的（最外面一圈是黑色的），里面是白色的，设置的时候的尺寸是白色的尺寸
* 大小取决于这个marker的id
* 因为检测到的时候这个码的方向可能改变， each corner is identified unequivocally
* 需要一个marker的dictornary的size和每个marker的size
* marker的id就是他在所有marker的dictornary里面的index（并不是读出来的数据233）

## Marker Creation
* 用drawMarker这个函数来生成print出来的marker
* DICT_6X6_250 -> 生成一个有250个6乘6的marker的dict(用cv2.aruco.getPredefinedDictionary这个生成默认的dict)
* 画的时候的参数：dict，id，输出尺寸，输出图片，优化参数

## Marker Detection
* 对于一组arUco，有两个返回值
	* code的四个角的位置（原始的顺序）
	* marker的id
* 主要步骤：
	* 检测marker的候选
		* 找到方形的部分，可能是marker
		* 确认内部的部分到底是不是marker
			* 进行投影变换，换成正面的
			* 滤波，区分出来黑色和白色的部分
			* 判断是不是属于dict
* dectectMarkers（）
	* 检测marker的图片
	* marker所在的dict
	* markerCorners：储存检测到的marker的角的位置（从左上角开始顺时针
	* markerIds：检测到的marker的id，大小和corner一样
	* 可以优化的参数
	* 被拒绝的marker（四个角的坐标）
* drawDectectedMarkers -> 可以直接画出来检测到的marker

## Pose Estimation
获得相机的pose for markers
* 需要知道相机的calibration matrix。（可以用opencv自带的函数calibrationCamera()
	* 会得到一个3乘3的矩阵
	* distortion coefficients: a vector of 5 elements
* cv2.aruco.estimatePoseSingleMarkers
	* 得到的结果应该是一个rotation vector和一个translation vector（纸的平面上有两个坐标x和y，垂直纸的坐标z）（平移向量和旋转向量）
	* 需要corner
	* 这个marker的大小和米的比例
	* 相机的参数

## Selecting a dictionary
* 在marker的dict里面，除了角和id，还有一个参数是inter-marker distance（minimum distance among its markers and it determines the error detection and correction capabilities of the dictionary）
	* 用来提高dict的鲁棒性，这个dict越小越好
	* 最简单的初始化方法： cv::aruco::getPredefinedDictionary
* 也可以通过手动来初始化但是我还没有看！

## Detector Parameters
懒得看了用的时候再说吧