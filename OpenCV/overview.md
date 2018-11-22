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

