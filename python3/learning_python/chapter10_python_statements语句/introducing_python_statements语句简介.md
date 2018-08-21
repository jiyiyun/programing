Python Statements
===

```txt
1.  Programs are composed of modules.
    程序由模块构成
2.  Modules contain statements.
    模块包含语句
3.  Statements contain expressions.
    语句包含表达式
4.  Expressions create and process objects.
    表达式建立并处理对象
python语法实质上是由语句和表达式组成的，表达式处理对象并嵌套在语句中。
programs written in the Python language are composed of statements
and expressions. Expressions process objects and are embedded in statements
```

```python
Statement                   Role                Example
Assigment                   Create references   a,b = 'good','bad'
Calls and other expressions Running functions   log.write("spam, ham")
print calls                 Printing objects    print('The Killer', joke)
if/elif/else                Selecting actions选择动作   if "python" in text:
                                                            print(text)
for/else                    Iteration序列迭代   for x in mylist:
                                                    print(x)
while/else                  General loops       while X > Y:
                                                    print('hello')
pass                        Empty placeholder空占位   while True:
                                                          pass
break                       Loop exit循环退出   while True:
                                                    if exittest(): break
continue                    Loop continue       while True:
                                                    if skiptest(): continue
def                         Functions and methods def f(a, b, c=1, *d):
                                                      print(a+b+c+d[0])
return                      Functions results函数结果    def f(a, b, c=1, *d):
                                                             return a+b+c+d[0]
yield                       Generator functions生成器函数  def gen(n):
                                                               for i in n: yield i*2
global                      Namespaces           x = 'old'
                                                 def function():
                                                     global x, y; x = 'new'
nonlocal                    Namespaces (3.X)     def outer():
                                                     x = 'old'
                                                 def function():
                                                     nonlocal x; x = 'new'
import                     Module access模块访问         import sys
from                       Attribute access属性访问      from sys import stdin
class                      Building objects创建对象      class Subclass(Superclass):
                                                             staticData = []
                                                             def method(self): pass
try/except/finally         Catching exceptions捕捉异常   try:
                                                             action()
                                                         except:
                                                             print('action error')
raise                     Triggering exceptions触发异常  raise EndSearch(location)
assert                    Debugging checks调试检查       assert X > Y, 'X too small'
with/as                   Context managers环境管理器      with open('data') as myfile:
                                                           process(myfile)
del                       Deleting references删除引用     del data[k]
                                                          del data[i:j]
                                                          del obj.attr
                                                          del variable
```
从技术上讲print在python3中不是保留字，也不是一条语句，而是一个内置的函数调用，由于几乎作为一条表达式语句运行，通常看作是一条语句类型
print is technically neither a reserved word nor a statement in 3.X, but a built-in
function call; because it will nearly always be run as an expression statement,
though (and often on a line by itself), it’s generally thought of as a statement type.

yield实际上是一个表达式，而不是一个语句，与print不同的三yeild是保留字
yield is also an expression instead of a statement as of 2.5; like print, it’s typically
used as an expression statement and so is included in this table, but scripts occasionally
assign or otherwise use its result, as we’ll see in Chapter 20. As an expression,
yield is also a reserved word, unlike print.

python增加的
python中新的语法成分是冒号:行首以冒号结尾
Header line:
    Nested statement block

python删除了什么？
括号是可选的 
    if (x<y)  可以省略括号写成 if x<y
终止行就是终止语句
    在python中一行结束会自动终止出现在该行的语句
缩进的结束就是代码块的结束
    不用刻意在程序代码中输入任何语法上用来标明嵌套代码块的开头和结尾的东西
    if x>y:
        x=1
        y=2

     语法规则给定一个单独的嵌套块中所有语句都必须缩进相同的距离
语句特殊情况
一行多个语句的时候，用分号分开
a = 1; b = 2; print(a + b)

```python
while True:
    reply = input('Enter text')
    if reply == 'stop': break
    print(reply.upper())

```
