第一部分 Basics

* C++在编译的时候就会检查类型
* allow programmers to define types that include operations as well as data

# 第二章 varibles and basic type
## 2.1 bulid-in
基础类型包括算数类型（arithmtic type）和void类型，void用于没有返回值的函数
### 2.1.1 算数类型
**include：intergal（bool& char）/ float**
  
***
不同的长度的叫法不同：
* char -> wchar_t, char16_t, char32_t(后面两个for unicode，自然语言里面)
* int -> short, long, long long
* float -> double, long double

扩展：在储存信息方面，储存在每个byte里面，是最小的计量单位（8bits）。在内存中，每个byte拥有一个address，需要知道地址和类型才知道到底存储的是什么东西。
  
***
signed & unsigned（除了bool）：
* signed：包括0的正数和负数
* unsigned：大于等于零
* 没有写unsigned的话就是signed的
	* 对于char来说，signed，unsigined和char三种
		* char到底算不算unsigned显示取决于编译器
		* unsigned从0-255
		* signed一般是-128 ～ 127
***
关于到底怎么用：
* 当确定不可能是负值的时候用unisgned
* short太短了，long太长了，平常用int，int不够用long long
* 如果用char，为了考虑到不同编译的结果不同，确定好用signed还是unsigned
* 用double，float的精度不够，long double小号内存

### 2.1.2 类型转换（conversions）
在把一个东西加到另一个的过程中，支持**自动的**类型转换
* 当bool被赋值为非0时，为true，0时为false
* 给int赋值double，自动变成整数；给doubl赋值int，变成整数后面.0
* 当unsigned超出界限时，the result is the remainder of the value modulo the number of values the target type can hold.
* 当signed超出界限的时候，结果是undefined。不知道会发生什么事。
***
***在写代码的时候尽量避免没有定义的，或者在implement中才定义的行为，因为这样容易导致在这个电脑上行得通但是换个地方没准就行不通了***
***
一些引起的问题：
* int和unsigned相加，会引起wrap around
* 两个unsigned相减如果小于零会出问题
* 在for循环的条件里，unsiged作为变量的话永远不会小于零
* **求求你了反正不要混着用**

### 2.1.3 literals
每个literal都有一个type，这是由form和value决定的。
* 整数类型的
	* 0开头的整数是八进制，0x是16进制
	* 负号不是literal的一部分，比如 -42，42是literal，负号是operator
* float类型的
	* 十进制带小数点的数字
	* 用exponent，E或者e，e后面的东西就是十的多少次方
* character
	* string的类型是一个char的array，complier会在每个string 后面加上‘\0'（null character）
* escape -> 一些带有奇怪意义的\n，\t,\'等等
	* 如果在\后面跟着多于三个数字，只会读取前三个
	* \x会读取跟在她后面的所有hex digits
* 单独改变一个literal，在数字后面加后缀suffix
	* U：unsigned type
	* L：long
	* ULL：unsigned long long
	* 但是如果你要给1024后面加个f就不行，因为1024是整形（这时候又开始怀念python）
* bool

## 2.2 变量 Variables
***变量提供的是：命名好的存储空间，程序可以对他执行，每个变量都有type（其实也就是class或者object吗）***
### 2.2.1 变量的定义
* assignment(赋值)和initialize(初始化)在c++里面是不一样的，初始化是在创建的时候赋予的值，赋值是之后改变这个变量的值
* list的初始化：尖括号。
	* 在使用bulit-in的时候，可能无法list初始化这个变量，因为会丢失一些信息。比如把一个double扔到int里面
* 是否可以不初始化就使用取决于class的定义。**比如要是int没有初始化的时候是0，string没有初始化的时候是空字符串**

### 2.2.2 变量declaration（声明？）和定义
* 在分开编写代码的时候，需要知道调用的函数从哪里来。***注意：不初始化变量容易出问题，建议初始化每个bulit-in***
* declaration：让程序知道函数的名字
	* 在前面加上extern，就可以declare但是不define
	* 但是如果已经初始化了函数，就不能加extern了，会引起错误
	* **在其他函数的地方调用的时候（use a varible in multiple files），不需要再define了，但是需要声明**
* defination：创建相应的实体
	* 除了干declaration的事情，他还分配内存，或者提供初始值
	* 变量被define一次，但是可以被declaration无数次。

### 2.2.3 identifiers（定义的名字）
* 要求
	* 数字，字母，下划线underscore
	* 对大小写有区分
	* 不能使用C++的关键词
	* 不能含有两个相连的下划线

### 2.2.4 名字的scope
* 使用的意义：同一个名字可能会在程序的其他地方被使用，所以要用scope确定这个名字在哪个范围里面有意义（**不是namespace啊啊啊啊啊竟然是大括号我震惊**）
* nested scope
	* 在外层被定义的名字可以在内层被重新定义
	* 温情建议：***局部变量和全局变量不要使用一个名字***

## 2.3 compound types（有范围的类型？）
就是定义在其他类型之上的类型。**在c++里面有两个，pointer和reference**
### 2.3.1 reference（lvalue reference）
在创建的时候，copy的不是对象的值，而是把refer和值绑在了一起，在创建之后不能再和别的东西绑在一起。reference必须初始化。
* 不是对象，是一个已经存在的对象的另一个名字
	* 给refer赋值的时候，实际上是赋值给refer所绑定的对象
	* 当给一个refer赋值另一个refer的时候，其实是绑到了同一个对象（但是不应该这么定义）
* 定义
	* 在refer的名字之前加上&，但是在后续使用的时候可以不带了
	* refer只能初始化成一个对象，不能是一个具体的值
	* 类型要正确

### 2.3.2 pointer
和refer不同，指针是一个object，他们可以被assign或者copy，在定义的时候不必须初始化，一个指针可以指向不同的东西。在定义的时候用 * 来表示
* 取址
	* pointer可以得到另一个对象的address。&也可以作为取址符号得到一个对象的地址（**和refer不一样！！**）
	* 类型必须匹配
* pointer的值（可以是以下四个之一）
	* 指向一个对象
	* 指向一个在对象中末尾的位置（没有使用的实际意义）
	* null指针，表示还没有和其他的绑定
	* 无效的？？**如果是无效的话是不能访问的**
* 访问对象
	* 当一个pointer指向对象的时候，使用dereference（ * ）来得到她的值。（pointer p是一个地址， * p是他这个地址上的值
* 空指针NULL
	* 使用nullptr定义
	* assign一个int变量给pointer是非法的，即使这个数是0（赋值的时候给的是变量的地址，带&的）
	* 真诚建议：**初始化所有的pointer**，没有初始化的很难分辨出来到底这个地址是有效还是无效
* assignment
	* 写成 pi = &val的时候，改变的是pi的值，他指向了val
	* 写成 * pi = 0 的时候，改变的是val的值，val变成了0
* void* Pointers
	* void* 是一个很牛逼的指针，可以hold所有对象的地址
	* 作用：可以传到函数或者作为函数的返回值，可以和其他指针比较，可以赋值给另一个void* 指针，但是不能操控对象的地址

### 2.3.3 理解
* 定义多个变量
	* 虽然在定义指针的时候可以加空格，但是 int* p1，p2之中，p1是指针，p2是int
* pointer到pointer
	* 写成一串星号可以表示从pointer到pointer
* refer到pointer
	* &r可以定义成一个pointer（指针写在=右边）

## 2.4 修饰词 const
* 作用：希望定义一个variable，value不可以被改变，这时候就用上了const。在创建的时候必须初始化
* 在实际操作的时候，到底是不是const对数值没有影响，可以用非const来初始化const或者用const来初始化其他的
* 在创建之后，编译的时候所有的变量名都会换成变量的值
* const对每个file来说是local的
* 如果希望定义一个在所有file里面都可以用的，然后在其他使用的时候声明，这时候用**extern const（在定义和后续声明的时候都需要使用）**

### 2.4.1 refer to const
* 可以refer到一个const，但是之后就不能通过refer来改变变量的值，也不能把一个const的变量赋值给一个非const的refer
* const refer的意思是这个refer不能被用来改变变量，但是被绑的变量本身可以改变。比如const int &r2 = i，这时候改变i是合法的

### 2.4.2 pointer and const
* pointer to const不能被用于改变指向的东西
	* 但是pointer是const的和变量自己改不改没关系。变量是const的话指针必须是const的
* const pointer
	* 指针本身就是一个对象，所以指针自己也可以是const的
	* 必须被初始化，一旦初始化了，他的内容（所指向的地址）就不能改变了。
	* 定义的时候用 int * const cpr = &num （const的位置改变了）
	* **但是可以用const pointer来改变所指向东西的值！！！只是这两个东西绑定了不能改了而已**
* 可以分开考虑pointer和对象
	* top-level：pointer自己是一个const
	* low-level：指向一个const
**常量指针就是一个常量，不能把常量给普通但是可以把普通给常量**