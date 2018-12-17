第一部分 Basics

* C++在编译的时候就会检查类型
* allow programmers to define types that include operations as well as data

# 第二章 varibles and basic type
## 2.1 bulid-in
基础类型包括算数类型（arithmtic type）和void类型，void用于没有返回值的函数
### 算数类型
include：intergal（bool& char）/ float
  

不同的长度的叫法不同：
* char -> wchar_t, char16_t, char32_t(后面两个for unicode，自然语言里面)
* int -> short, long, long long
* float -> double, long double
  

扩展：在储存信息方面，储存在每个byte里面，是最小的计量单位（8bits）。在内存中，每个byte拥有一个address，需要知道地址和类型才知道到底存储的是什么东西。
  

signed & unsigned（除了bool）：
* signed：包括0的正数和负数
* unsigned：大于等于零
* 没有写unsigned的话就是signed的
	* 对于char来说，signed，unsigined和char三种，
