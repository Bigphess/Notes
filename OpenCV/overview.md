# learning OpenCV overview

	go trough chapter 1-5
	Chapters 18 and 19 (which cover camera calibration and stereo imaging) and Chapters 20, 21, and 22 (which cover machine learning)

ML值得一本新的书去学
  




# CH1.overview
有一个专门的ML模块


## what's CV:
In a machine vision system, however, a computer receives a grid of numbers from the camera or from disk, and that’s it. 
	-> the 2D appearance of objects can change rad‐ ically with viewpoint

many noise & distortions

Thus, there is often quite a bit of unintentional implicit information within photos taken by people

The next problem facing computer vision is noise. -> 边缘检测在统计情况下变得简单



## reference
  
	core -> all the basic part
	imgproc -> fliters/ convolutional operator
	highgui -> user interface
	vidoe
	calib3d -> detecting, describing, matching key-point features
	objdetect -> detect face/ pedestrains
	ml -> ML
	flann -> Fast Library for Approximate Nearest Neighbors
	....


  



# CH2.intro to OpenCV
主要讲的是如何读取和现实储存图片和视频

## display a image:
read from a wide array of image/video/cameras
  
opencv functions live within ***cv*** (namespace) -> can use **using namespace cv**
  
	#include <opencv2/opencv.hpp> //Include file for every supported OpenCV function
	int main( int argc, char** argv ) {
	  cv::Mat img = cv::imread(argv[1],-1);
	  if( img.empty() ) return -1;
	  cv::namedWindow( "Example1", cv::WINDOW_AUTOSIZE );
	  cv::imshow( "Example1", img );
	  cv::waitKey( 0 );
	  cv::destroyWindow( "Example1" );
	  return 0;
	}
  
* use <opencv2/opencv.hpp> -> general include
* use "opencv2/highgui/highgui.hpp" -> only the neceaaary file to improve the time
  
*cv::imread()* is a high-level routine that determines the file format to be loaded based on the filename -> return a cv::Mat
  

***img.empty()*** -> true/false

***cv::namedWindow( "Example1", cv::WINDOW_AUTOSIZE );*** 
* 0 -> true size
* WINDOW_AUTOSIZE -> to fit the window
  
***imshow("name",img)*** -> crreate a window(if not created) & show the img
  
***cv::waitKey( 0 );*** -> stop and wait for key if 0, and wait for ms if have args(如果在这么长的时间内没有人按，就继续执行程序)
  
***cv::destroyWindow( "Example1" );*** -> save memory usage
  
## vedio
	#include "opencv2/highgui/highgui.hpp"
	#include "opencv2/imgproc/imgproc.hpp"
	int main( int argc, char** argv ) {
	  cv::namedWindow( "Example3", cv::WINDOW_AUTOSIZE );
	  cv::VideoCapture cap;
	  //这个变量是专门用在捕捉视频上面的
	  cap.open( string(argv[1]) );
	  cv::Mat frame;
	  for(;;) {
	    cap >> frame;
	    if( frame.empty() ) break;
	    cv::imshow( "Example3", frame );
	    if( cv::waitKey(33) >= 0 ) break;
	}
	return 0; }

***VideoCapture*** -> object for video cap
  
***cap.open(string(argv[1]));*** -> open the video in path
  

## 给视频加一个进度条
***createTrackbar*** -> 可以直接给视频加进度条，牛逼 

## 一些其他的转化
* ***GaussianBlur()*** 高斯滤波，给画面加滤镜
* downsample一张图片 -> image pyramid -> change the scale -> ***pyrDown()***
  

## write video to a AVI file
* cv::VideoWriter
* Once this call has been made, we may stream each frame to the cv::VideoWriter object, and finally call its cv::VideoWriter.release() method when we are done
* The first is just the filename for the new file. The second is the video codec with which the video stream will be compressed. The next two arguments are the replay frame rate and the size of the images we will be using
	

cv::VideoWriter writer;
writer.open( argv[2], CV_FOURCC('M','J','P','G'), fps, size );
//第二个参数是压缩的文件的格式
  

	#include <opencv2/opencv.hpp>
	#include <iostream>
	int main( int argc, char* argv[] ) {
	  cv::namedWindow( "Example2_11", cv::WINDOW_AUTOSIZE );
	  cv::namedWindow( "Log_Polar",   cv::WINDOW_AUTOSIZE );
	  // ( Note: could capture from a camera by giving a camera id as an int.)
	  //
	  cv::VideoCapture capture( argv[1] );
	  double fps = capture.get( cv::CAP_PROP_FPS );
	  cv::Size size(
	    (int)capture.get( cv::CAP_PROP_FRAME_WIDTH ),
	    (int)capture.get( cv::CAP_PROP_FRAME_HEIGHT )
	);
	cv::VideoWriter writer;
	writer.open( argv[2], CV_FOURCC('M','J','P','G'), fps, size );
	cv::Mat logpolar_frame, bgr_frame;
	for(;;) {
	  capture >> bgr_frame;
	  if( bgr_frame.empty() ) break; // end if done
	  cv::imshow( "Example2_11", bgr_frame );
	}
	cv::logPolar(
	  bgr_frame,
	  logpolar_frame,
	  cv::Point2f(
	    bgr_frame.cols/2,
	    bgr_frame.rows/2
	  ),
	40,
	  cv::WARP_FILL_OUTLIERS
	);
	// Input color frame
	// Output log-polar frame
	// Centerpoint for log-polar transformation //x
	//y
	// Magnitude (scale parameter)
	// Fill outliers with 'zero'
	cv::imshow( "Log_Polar", logpolar_frame );
	writer << logpolar_frame;
	    char c = cv::waitKey(10);
	    if( c == 27 ) break;
	  capture.release();
	}
	// allow the user to break out

