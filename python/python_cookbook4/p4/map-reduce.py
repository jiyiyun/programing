``` shell
>>> lower =(lambda x,y:x if x <y else y)
>>> lower('aa','bb')
'aa'
>>> lower(11,22)
11

>>> list(map(pow,[1,2,3],[4,5,6]))
[1.0, 32.0, 729.0]

>>> list(filter((lambda x:x>0),range(-5,5)))
[1, 2, 3, 4]

reduce 函数在python2中是内置函数，在python3中已经放到functools模块中
>>> reduce((lambda x,y:x+y),[1,2,3,4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reduce' is not defined
>>> from functools import reduce
>>> reduce((lambda x,y:x+y),[1,2,3,4])
10
```