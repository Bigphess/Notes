# CH3 data types
  
three types：
* basic data type
* helper objects -> more abstract
* large array types
*Standard Template Library(STL)*
  

## basic type overview
### **cv::Vec<>** fixed vector class
* cv::Vec2i, cv::Vec3i, and cv::Vec4d (for a two-element integer vector, a three-element integer vector, or a four-element double-precision floating-point vector, respectively).
* 

### **cv::Matx<>** fixed mactrice class -> for the handling of certain specific small matrix operations（小的矩阵）
* the dimen‐ sionality of the fixed matrix classes must be known at compile time，这样的话allcoate和clean up都很快
* vec源自matx，然后像scalar这样的再来自vec
* 有好多矩阵相关的操作，还有reshapee这种奇怪的东西

### point class -> related to fixed vectors
* access by named varibles rather than index
* cv::Point2i, cv::Point2f, and cv::Point2d, or cv::Point3i, cv::Point3f, and cv::Point3d.

### cv::Scalar -> 4d point
keyword cv::Scalar specifically is aliased to a four-component vector with double-precision components

### cv::Size & cv::Rect
* cv::Size is mainly distinguished by having data members width and height rather than x and y (其实看起来和point差不多)，可以compute area
* ***RotatedRect class*** -> point2f called center & size2f called size & float angle

### complex number
like in STL but access different(但是我并不知道STL里面什么样子)


### Details -> from P45
  


## helper objects
for control various algorithms
### The cv::TermCriteria class
* 在算法里面需要一个quit的condition：“if you are this close, you can quit” (called EPS—short for epsilon, everyone’s favorite tiny number)
* TermCriteria( int type, int maxCount, double epsilon )

### The cv::Range class
The cv::Range class is used to specify a continuous sequence of integers.
### cv::Ptr & garbage collection
* call like cv::Ptr<Matx33f> p = makePtr<cv::Matx33f>()
* supports operator * & operator -> ()
* 两个指针同时指向一个东西，最后一个消失的时候自动垃圾回收

### cv::DataType<>
This allows the cv::DataType<> object to contain both runtime information about the type, as well as typedef statements in its own definition that allow it to refer to the same type at compile time.
大概就是存储图像信息的一个template
### cv::InputArray & cv::OutputArray
* opencv take arrays as args and return arrays
* Input is const(read only)
* cv::noArray() returns a InputArray,这个结果可以被pass给任何需要的input证明它还没有被用过

## other unity functions（P60）
  
# CH4 Image&Larg Array Types
The cv::Mat class is used to represent **dense arrays** of **any number of dimensions**.
The alternative would be a sparse array. In the case of a sparse array, only nonzero entries are typically stored. -> mat 会存储所有的数据，0也存
*dim* -> dimension of the array
*col, row*
*data* -> pointer, where the data is stored
## create a Mat
can use .create() to create a Mat

	cv::Mat m;
    // Create data area for 3 rows and 10 columns of 3-channel 32-bit floats
    m.create( 3, 10, CV_32FC3 );
    // Set the values in the 1st channel to 1.0, the 2nd to 0.0, and the 3rd to 1.0
    m.setTo( cv::Scalar( 1.0f, 0.0f, 1.0f ) );
    is equivalent to:
    cv::Mat m( 3, 10, CV_32FC3, cv::Scalar( 1.0f, 0.0f, 1.0f ) );

* 初始化的时候：需要设置Mat的demension，可以初始化data，用*Scalar*或者providing a pointer to an appropriate data block that can be used by the array
* copy一个Mat，cv::Mat( const Mat& mat ); 还有更多的方法可以就copy一部分（这里面的&其实是reference）
* copy一个cvMat或者IplImage，和上面一样的方法，但是要选择是否copy data

## accessing array elements
### basic one: *.at<>*,输入需要的位置

	//对于单通道的32FC1
	m.at<float>(3,3)
	//对于多通道的32FC2
	 m.at<cv::Vec2f>(3,3)[0],
     m.at<cv::Vec2f>(3,3)[1]
**最好的方法是通过Vec<>**
### 使用ptr访问 2d数组
take an integer arg -> the row
return a pointer to primitive type -> if CV_32FC3, return float*
###  isContinuous() 
一行数组可能被存在不同的位置，这个函数会告诉你到底位置相不相同，如果相同的话直接cruise这个数组就可以了
### iterator
cv::MatIterator<> and cv::MatConstIterator
begin() and end()
可以用这个iterator迭代整个mat，注意这个iterator的object类型需要在最开始就声明 -> cv::MatConstIterator<cv::Vec3f> it = m.begin();
*如果需要对整个array做操作的时候*

## NAryMatIterator
* allows us to handle iteration over many arrays at once
* the N-ary itera‐ tor operates by returning chunks of those arrays, called planes（slice of the input which the data is contiguous in memory）

## Block
* 用于想access这个数组的一个subset吗，比如一行或者一列
* m.row() or m.col() -> data in m not copied to a new array
* rowRange() and colRange().
* m.diag() references the diagonal elements of a matrix. m.diag() expects an integer argument that indicates which diagonal is to be extracted
* cv::Rect to specify the region you want

## saturation casting
To deal with overflowing or underflowing
cv::saturate_cast<>() -> allows you to specify the type to which you would like to cast the argument

	uchar& Vxy = m0.at<uchar>( y, x );
    Vxy = cv::saturate_cast<uchar>((Vxy-128)*2 + 128);}
    //result is twice as far from 128 as the original

## SparseMat
Most of the space will be empty in many practical applications
Compare with Mat:It is defined similarly, supports most of the same operations, and can contain the same data types
### access SparseMat
Have 4 ways to access:
1.ptr()
  
	//第一个参数是element的index，第二个是是否创建（如果在里面没有）,第三个用来计算hash或者用来直接表示这个的hash
	uchar* cv::SparseMat::ptr( int i0, bool createMissing, size_t* hashval=0 );
* if creatingMissing is false:When cv::SparseMat::ptr() is called, it will return a pointer to the element if that element is already defined in the array, but NULL if that element is not defined
* if it's true: that element will be created and a valid non-NULL pointer will be returned to that new element.

2.ref<>() 
return a reference to particular element of the array
3.value<>()
it returns the value and not a reference to the value
4.find<>()
returns a pointer to the requested object
5.iterators
cv::Spar seMatIterator_<> and cv::SparseMatConstIterator_<>
  
## for large array types
**Mat<> & Mat_<>**
In the case of cv::Mat_<>, the instantiated template is actually derived from the cv::Mat class, and in effect specializes that class
**大概就是在用的时候不用再用声明<Vec2f>这种东西了？**

## cvMat，IplImage和mat
* mat具有更强的矩阵计算能力，密集（dense）的数组，数学性能比较高，偏重于计算
* cvMat比Mat更偏重于图像部分
* IplImage，继承cvMat，多了更多的参数（depth，channel）
  




  


# CH5 array operations
## rules
* output is saturation-casteed
* output: will be created if it is not match.一般需要输入和输出的size相同，但是有的函数里面也可以不相同
* scalars: the result of pro‐ viding a scalar argument is the same as if a second array had been provided with the same scalar value in every element
* masks: the output will be compu‐ ted only for those elements where the mask value corresponding to that element in the output array is nonzero.
* dtype: 有的时候不需要input全部一样或者，输入和输出并不一样。When present, dtype can be set to any of the basic types (e.g., CV_32F) and the result array will be of that type。如果就需要相同的格式的话就是默认的-1

## 一些functions
### cv::bitwise_and()
可以计算两个array中间每个element的and
ps. cv::bitwise_xor() -> 计算的是抑或
functions

