## C++ pointer
每一个变量都可以用&来计算地址
如&var可能是：0xbfebd5c0 这种东西
***核心：地址和地址玩耍，值和值玩耍，指针不带星的时候显示的是地址，带星的时候显示的才是实际指向的内容***

指针式一个变量，它的值是另一个变量的地址

	int    *ip;    /* 一个整型的指针 */
	double *dp;    /* 一个 double 型的指针 */
	float  *fp;    /* 一个浮点型的指针 */
	char   *ch;    /* 一个字符型的指针 */
无论是什么数据类型的指针，它的值都是一个代表地址的十六进制数，不同只是指向的数据类型不同
  

### 空指针 null pointer
被赋值为NULL的指针，在标准库里为**0**
如果指针包含0，则不指向任何东西，可以防止使用一个未初始化的指针
  
### 指针的运算
递增：用指针代替数组，变量指针可以递增，数组是一个常量指针
同理，指针也可以递减

	#include <iostream>
	 
	using namespace std;
	const int MAX = 3;
	 
	int main ()
	{
	   int  var[MAX] = {10, 100, 200};
	   int  *ptr;
	 
	   // 指针中的数组地址
	   ptr = var;
	   for (int i = 0; i < MAX; i++)
	   {
	      cout << "Address of var[" << i << "] = ";
	      cout << ptr << endl;
	 
	      cout << "Value of var[" << i << "] = ";
	      cout << *ptr << endl;
	 
	      // 移动到下一个位置
	      ptr++;
	   }
	   return 0;
	}  

	Address of var[0] = 0xbfa088b0
	Value of var[0] = 10
	Address of var[1] = 0xbfa088b4
	Value of var[1] = 100
	Address of var[2] = 0xbfa088b8
	Value of var[2] = 200
  

指针可以用运算关系进行比较，但是***比较的时候要和&之后的数据进行比较，地址和地址比较？***
### 指针和数组
一个数组名对应一个指针常量（指向数组开头的指针？）
一个指向数组开头的指针，可以通过指针的运算或者数组的索引来访问数组
修改数组是违法的，但是可以把指针运算符 * 用到数组上面去，只要不改变数组的值

	//将var[2]的值赋为500
	*（var+2） = 500

### 指针数组
	int *ptr[MAX]
	//ptr声明为一个数组，数组由MAX个整数指针组成，每个element都是一个指向int的指针

### pointer -> pointer
多级寻址（指针链）

	//用int **var定义
	#include <iostream>
	using namespace std;
	 
	int main ()
	{
	    int  var;
	    int  *ptr;
	    int  **pptr;
	 
	    var = 3000;
	 
	    // 获取 var 的地址
	    ptr = &var;
	 
	    // 使用运算符 & 获取 ptr 的地址
	    pptr = &ptr;
	 
	    // 使用 pptr 获取值
	    cout << "var 值为 :" << var << endl;
	    cout << "*ptr 值为:" << *ptr << endl;
	    cout << "**pptr 值为:" << **pptr << endl;
	 
	    return 0;
	}

### 指针和函数
* 可以传递指针给函数并在函数里面改变这个值，能接受指针的函数也能接受数组作为参数
* 如果需要返回一个指针，需要声明一个返回指针的函数。C++不支持在函数外返回局部变量的地址，除非定义成
一个static变量
int * Function(){}
static int r[10]；

## C++ reference
是一个已经存在的变量的另一个名字
和指针相比：
* 不存在空refrence
* 一旦被指向一个对象，就不能指向另一个对象了
* 必须在创建时就被初始化，指针随时都可以初始化

		int i = 17;
		int&  r = i;
		double& s = d;

这里面的&是引用，r是一个初始化为i的引用

