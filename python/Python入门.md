# 读一本书
## 基础入门
terminal：python3
help()打开帮助，q退出帮助
* 注释：#

### 一些奇怪的小笔记
* sublime自己设置python3
```
which python3
```
* sublime用REPL插件实现input，记得修改python版本

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

### 默认参数
* 在定义的时候直接给这个参数赋值
* 如果调用的时候不改就是默认值，改了的话就是改了的值

### 关键字参数
* 在调用参数的时候使用函数的关键字，而不是参数的位置来调用
* func(c=50, a=100)

### 可变参数
* 希望参数可以任意数量变换
* def total(a=5, * numbers, ** phonebook):
* 当收到星号加参数的时候，所有参数都会变成一个tuple或者dict？

### return
* 可以设置返回值
* pass可以直接pass整个函数的定义

### docstrings
* 函数定义后面的一个字符串
* 第一行是大写字母开始，第二行空着，第三行开始写详细内容
* 使用 .__doc__ 来调用。**也可以用help(函数名)来调用**
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
* 一个模块可以被import
* .pyc文件导入的速度更快，但是如果.py没有权限的话，pyc也不能访问

### from..import
* 如果只需要一个模块里面的一部分函数
* 但是这样容易冲突，不建议使用
* 如果用from mymodule import * ，会导入除了__开头的其他公共名称

### __name__
* 每个模块都有自己的名字，这个名字用来确定这是独立运行的模块还是被import的模块作用很大
* 模块第一次导入的时候，包含的代码将被执行
```
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
```

### dir函数
* 返回对象所定义的名称列表，如果没有参数，返回的是当前的 

### 包package
* 用来组织起来模块
* 是包含模块和__init__.py的文件夹，init表示他是特别的


## 数据结构
### 列表
* 有序的集合，可变
* append往列表里面增加对象
* 方括号表示

### tuple
* 多个对象保存在一起，类似列表但是不是
* 不可变，类似字符串
* 圆括号表示
* 在访问里面是括号套括号的，('monkey', 'camel', ('python', 'elephant', 'penguin'))，这时候可以用索引[2]来访问后面的括号，[2][XX]来访问括号里面的内容

### dictornary
* 把key和value对应
* 只能使用不可变的作为key，但是value都可以
* d = {key : value1 , key2 : value2}
* 已经成对的key和value不会进行排序
* call里面的key就会显示他的value，操作都是通过key来进行的
* 用.item来访问

### sequence
* 主要是判断这里面有没有东西和索引操作
* 索引可以使用负数，从后面开始，-1是最后一个，以此类推
* 选择一段的时候用冒号进行分割，也可以用负数
* 可以用两个冒号表示步长

### set
* 没有顺序，更重视出现的次数

### 字符串还有好多自己操作的方法

## 面向对象

### self
* **类方法**和普通的函数的区别，多了一个参数在最开头
* 但是不用在调用这个函数的时候给这个参数赋值
* 相当于c++里面的this

### 类
* 通过class创建一个类
* 之后是缩进的语块
* 创建的时候是后面加一个括号

### 方法
创建一个带self参数的方法，虽然say_hi不需要参数，但是还是需要一个self参数
```
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
```
```
$ python oop_method.py
Hello, how are you?
```

### init 方法（类里面的一个方法）
* 会在类的对象被实例化的时候立刻运行
* 可以对我的类进行初始化
```
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
```


### 变量
* 类变量：可以被这个类的所有实例访问，所以访问这个变量的时候用ClassName.ClassVariable。也可以用self.\__class__.population来访问
* 对象变量：独立的实例拥有的 objectName.ObjectVariable
* 当一个对象变量与一个类变量名称相同时，类变量将会被隐藏。
* 如果一个方法属于类，可以用@classmethod来标记为类方法（这个@也可以定义静态方法staticmethod）
* 所有类成员都是公开的，如果在前面加两个下划线会编程private的
* 实例方法的参数是self。类方法的参数是cls（不是self）。静态方法是和类有关，但是不需要引用类或者实例，比如调整环境变量

### 继承
* 在定义类的时候在后面加个括号里面是继承的别的类
* 基类的初始化不会自动调用，用的话需要自己调用
* 多重继承的时候调用的是子类型的方法

```
# coding=UTF-8

class SchoolMember:
    '''代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()
```

## 输入和输出
### 用户输入输出：input
### 文件
* 可以用open，read，readline，write等方法调用

### Pickle
* 标准模块
* 将任何纯python对象储存到一个文件中

### unicode
* unicode的字符串转换成可以被发送和接受的模式
* #encoding=utf-8 放在程序顶端

## 异常
* 可以通过try...except来处理异常（except里面是异常的名称）
```
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))
    ```

### 抛出异常
* 必须是在exception里面的异常
* 使用raise来引发一个异常里面东西，其他工作还能正常运行

### try..finally
* 确保被正常关闭，无论是否会发生异常东西都会关闭

### with
* 和finally一样都是释放异常的方法

## 标准库
* sys模块，命令行参数
* 日志

## 其他
* 一个函数返回两个不同的值：用一个tuple

# 读完书以后还是不懂
## 关于类的self
* 代表类的实例，这里的类对应的是对象，和局部变量，全局变量之类的对立
* 其实根本不用写成self，但是约定俗成写成了
* 在继承中，首先找子类里面有没有这个方法，要是没有的话就再沿着父类往上找

## 为啥有那么多下划线
* 前单下划线 \_var: 这个变量和方法仅供内部使用。对python本身没有影响，作为对程序员的提示
* 末尾单下划线var_: 避免名字和关键字产生冲突
* 双前下划线__var： 导致Python解释器重写属性名称，以避免子类中的命名冲突（表示类的私有成员）
* 前后双下划线__var__： 一般都是系统定义的名字，一般自己定义的时候不使用
* 单下划线：用作一个名字，表示无关紧要的临时变量，比如for里面的i

## py函数定义里面居然
* 定义里居然有箭头！！！用来定义返回值的类型（天呐我竟然能在py看到类型我真是感动）
* 定义里居然有冒号！！！用来提示参数的数据类型
* 居然可以有好几个返回值！！！tuple返回值，天惹

## with...as 关键字
* 是一个跟for那种的差不多的控制语句，简化try
* try的本身应该是try一个语句，如果可以的话就执行下一句，不可以的话执行except的情况，最后执行finally里面的关闭文件
* 在执行with的时候，会把__enter__的值返回给as后面的参数，然后执行后面的语句，最后不管怎么样都执行__exit__保证退出去
```
with open("x.txt") as f:

    data = f.read()

    do something with data
    ```

# 进阶？
## 多线程
* 同时处理不同的程序
* 两个标准库，thread和threading
* 线程优先队列Queue

# 永远看不懂问题之冒号
* 默认全部选择（逗号前面的那个东西）
* 指定范围
* 第一个逗号前面的表示的是行的范围，第二个后面表示的是列的范围
[:,【选择从第几个开始，没有填的话默认第一个】:【选择从第几个结束，没有的话默认最后一个】:【步长】-1]
第一个冒号是选取第一个维度
```
x=np.array([[1,2,3],[5,6,7],[7,8,9]])
print(x)
print('------------')
print(x[:,::-1])
print('------------')
print(x[:,::1])
print('------------')
print(x[:,::2])
print('------------')
print(x[:,::3])
print('------------')
print(x[:,::666666])

[[1 2 3]
 [5 6 7]
 [7 8 9]]
------------
[[3 2 1]
 [7 6 5]
 [9 8 7]]
------------
[[1 2 3]
 [5 6 7]
 [7 8 9]]
------------
[[1 3]
 [5 7]
 [7 9]]
------------
[[1]
 [5]
 [7]]
------------
[[1]
 [5]
 [7]]
--------------------- 
作者：ML_BOY 
来源：CSDN 
原文：https://blog.csdn.net/qq1483661204/article/details/78149262 
版权声明：本文为博主原创文章，转载请附上博文链接！
```

## 来呀来玩np啊
### numpy.zeros(shape, dtype=float, order='C')¶
* 形状是行乘列，类型，默认的C就是行主导的