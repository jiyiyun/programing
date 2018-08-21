函数主要扮演两个角色
---
- 代码重用 ，最小化代码冗余
- 流程分解
- def是可执行的代码，
- def 创建了一个对象并将其赋值给某一变量名
- lambda创建一个对象但将其作为结果返回
- return 将一个结果对象发送给调用者
- yield 向调用者发回一个结果对象，但是记住它离开的地方
- global 声明了一个模块级的变量并被赋值
- nonlocal 声明了将要赋值的一个封闭的函数变量
- 函数是通过赋值(对象引用)传递的
- 参数、返回值以及变量并不是声明

``` shell
def < name > (arg1,arg2,.... argN):
    ...
    return <value>
```
return 可以在函数主体的任何地方出现，表示函数调用结束，并将结果返回至函数调用处

def语句
---
- def 语句是实时执行的
- def 可以嵌套在不同的函数中

``` shell
if case:
    def func():
        ...
else:
    def func():
        ...
func()
```
函数描述了两个方面，定义def 和 调用
``` shell
def times(x,y):   #定义一个函数
    return x*y
```
调用
- times(2,4)     #输出8
- times(NI,4)    #输出'NINININI'
