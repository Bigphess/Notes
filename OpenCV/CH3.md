# CH3 data types
  
three types：
* basic data type
* helper objects -> more abstract
* large array types
*Standard Template Library(STL)*
  

## basic type overview
### **cv::Vec<>** fixed vector class
cv::Vec2i, cv::Vec3i, and cv::Vec4d (for a two-element integer vector, a three-element integer vector, or a four-element double-precision floating-point vector, respectively).
### **cv::Matx<>** fixed mactrice class -> for the handling of certain specific small matrix operations（小的矩阵）
the dimen‐ sionality of the fixed matrix classes must be known at compile time
### point class -> related to fixed vectors
access by named varibles rather than index
cv::Point2i, cv::Point2f, and cv::Point2d, or cv::Point3i, cv::Point3f, and cv::Point3d.
### cv::Scalar -> 4d point
keyword cv::Scalar specifically is aliased to a four-component vector with double-precision components
### cv::Size & cv::Rect
cv::Size is mainly distinguished by having data members width and height rather than x and y, while cv::Rect has all four.

