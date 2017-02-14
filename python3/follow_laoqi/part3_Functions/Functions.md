foo(*args)
---

``` shell
>>> def foo(*args):
...     print(args)
... 
>>> foo('tom','jack','john')
('tom', 'jack', 'john')
>>> foo('bob','richad','sony','bush','alax')
('bob', 'richad', 'sony', 'bush', 'alax')
```
foo(**args)
---

``` shell
>>> def foo(**args):                        #**args只接收arg=value的类型
...     print(args)
... 
>>> foo(1,2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() takes 0 positional arguments but 3 were given
>>> foo(a=1,b=2,c=3)
{'b': 2, 'a': 1, 'c': 3}
```

综合foo(*args)和foo(**args)
---

``` shell
>>> def foo(x,y=2,*targs,**dargs):
...     print('x=',x)
...     print('y=',y)
...     print('targs_tuple==',targs)
...     print('dargs_dict==',dargs)
... 
>>> foo(1,2,3,4,'1x','2y','3t1','3t2',d1='4d1',d2='4d2')
x= 1
y= 2
targs_tuple== (3, 4, '1x', '2y', '3t1', '3t2')
dargs_dict== {'d1': '4d1', 'd2': '4d2'}
```