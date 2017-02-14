lambda 、map 、reduce 、filter 、yield
---

``` shell

>>> numbers=[1,2,3,4,5,6]
>>> new_numbers=[i + 3 for i in numbers]
>>> print(new_numbers)
[4, 5, 6, 7, 8, 9]

>>> lam = lambda x:x+3
>>> for i in numbers:
...     n2.append(lam(i))
... 

>>> print(n2)
[4, 5, 6, 7, 8, 9]

>>> g = lambda x,y:x+y
>>> g(3,4)
7

>>> (lambda x:x**2)(4)
16

```

- 在lambda后面直接跟变量
- 变量后面是冒号
- 冒号后面是表达式，表达式的结果就是本函数的返回值

lambda arg1, arg2, arg3, ...argN :expression using arguments

虽然lambda函数可以接收任意多个参数，返回单个表达式的值，但是lambda函数不包含命令，包含的表达式不能超过一个

``` shell
>>> lamb =[lambda x:x,lambda x:x**2,lambda x:x**3,lambda x:x**4]
>>> for i in lamb:
...     print(i(3))
... 
3
9
27
81
```
map 
---

``` shell
>>> def add(x):
...     x +=3
...     return x
... 
>>> map(add,numbers)
[4, 5, 6, 7, 8, 9]
```

reduce(function,iteraable[,initializer])  reduce()是横着逐个元素进行运算，map()是上下运算
---

``` shell
求a[i] * b[i] 的值
>>> a = [3,4,5,6,7]
>>> b = [9,8,7,6,5]
>>> zip(a,b)
<zip object at 0x1021e3bc8>
>>> sum(x*y for x,y in zip(a,b))
165
>>> from functools import reduce

直接用reduce()函数
>>> reduce(lambda x,y:x+y,map(lambda x,y:x*y,a,b))
165
>>> 
```

filter 过滤器 filter(function,iterable)
---

``` shell
>> numbers=range(-5,5)
>>> numbers
range(-5, 5)
>>> filter(lambda x: x>0 ,numbers)
<filter object at 0x1021e90b8>
>>> print(filter(lambda x: x>0 ,numbers))
<filter object at 0x1021e9128>
>>> list(filter(lambda x: x>0 ,numbers))
[1, 2, 3, 4]
```
