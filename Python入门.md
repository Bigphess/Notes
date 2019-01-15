## 基础入门
terminal：python3
help()打开帮助，q退出帮助
* 注释：#

### sublime自己设置python3
```
which python3
```

### 常量
* 数字：int和float。（int可以表示任何大小的整数）
* 字符串：单引号或者双引号表示，三引号指定多行字符串
	* 字符串创建了就不能改变
	* 没有单独的char类型
	* 用format来表示构建的类型
```
age = 20
name = "XU"
#括号里可以不写数字
print("{0} is {1} years old".format(name,age))
```
除此之外，可以用+链接
```
name + 'is' + str(age) + 'years old'
```
还可以定义不同的格式
```
#小数点后面的位数
print('{0:.3f}'.format(1.0/3))
#一共11位，hello居中
print('{0:_^11}'.format(hello))
```
如果指定固定的结尾，就不会用换行符号
```
print('a',end = '')
print('b',end = '')
```
\反斜杠代表转义序列，一个反斜杠转义单引号，两个转双引号。字符串前面加**r或者R**可以转换成原始字符串

### 编程实操
#### 行
* python认为每一个物理行都会对应一个逻辑行（可以用分号但是没必要）
* 如果有一行非常长，可以用\把它拆成更多个物理行

#### 缩进
* 每一次同样的缩进都代表一个语句块，不能随便缩
* 用四个空格缩进


## 运算符，表达式
* 乘方 ** 
* 整除 //
* 按位与 &，按位或 |
* 按位取反 ~
* 按位异或 ^
* 非：not，与：and，或：or

## if,for,while
* if并不用括号，elif，else。需要冒号
* while也不需要括号，可以用continue和break，后面也可以加else
* for xx in range（1，5）,range包括前面的不包括后面的
	* **for后面居然还可以加else我的天呐！！！！**
* break可以break循环语句，后面的else都不会再执行了
* continue，跳过当前循环的剩余语句，继续下一个循环

## 函数
* 函数通过：def 函数名 (参数)：来定义
* 如果在函数定义的里面定义全局变量，用global
```
x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)
```
```
$ python function_global.py
x is 50
Changed global x to 2
Value of x is 2
```
* 默认参数，在定义的时候直接给这个参数赋值，如果调用的时候不改就是默认值，改了的话就是改了的值
* 关键字参数：在调用参数的时候使用函数的关键字，而不是参数的位置来调用：func(c=50, a=100)
* 可变参数：希望参数可以任意数量变换，def total(a=5, * numbers, ** phonebook):当收到星号加参数的时候，所有参数都会变成一个tuple或者dict？
* return可以设置返回值，pass可以直接pass整个函数的定义
* docstrings：函数定义后面的一个字符串，第一行是大写字母开始，第二行空着，第三行开始写详细内容，使用 .__doc__ 来调用。**也可以用help(函数名)来调用**
```
def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
```
```
$ python function_docstring.py
5 is maximum
打印两个数值中的最大数。

    这两个数都应该是整数
```

## 模块