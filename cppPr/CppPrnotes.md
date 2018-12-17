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
