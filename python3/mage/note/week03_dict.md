字典dict :可变，无序，key不可重复 
===

key不可重复,value可以重复，典型应用redis

```shell
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
|  clear(...)
|      D.clear() -> None.  Remove all items from D.
|
|  copy(...)
|      D.copy() -> a shallow copy of D
|
|  fromkeys(iterable, value=None, /) from builtins.type
|      Returns a new dict with keys from iterable and values equal to value.
|
|  get(...)
|      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
|
|  items(...)
|      D.items() -> a set-like object providing a view on D's items
|
|  keys(...)
|      D.keys() -> a set-like object providing a view on D's keys
|
|  pop(...)
|      D.pop(k[,d]) -> v, remove specified key and return the corresponding val
e.
|      If key is not found, d is returned if given, otherwise KeyError is raise

|
|  popitem(...)
|      D.popitem() -> (k, v), remove and return some (key, value) pair as a
|      2-tuple; but raise KeyError if D is empty.
|
|  setdefault(...)
|      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
|
|  update(...)
|      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
|      If E is present and has a .keys() method, then does:  for k in E: D[k] =
E[k]
|      If E is present and lacks a .keys() method, then does:  for k, v in E: D
k] = v
|      In either case, this is followed by: for k in F:  D[k] = F[k]
|
|  values(...)
|      D.values() -> an object providing a view on D's values
  Data and other attributes defined here:

  __hash__ = None

由上可知,dict的方法不多

增加和修改
>>> D1={'name':'jack','age':'33'}
>>> D1
{'age': '33', 'name': 'jack'}
>>> D1.get('age')
'33'
>>> D1.get('name')
'jack'
get 是获取key对应的valuez值

增加1
>>> D1['ID']=12
>>> D1
{'age': '33', 'name': 'jack', 'ID': 12}
增加2
>>> D1.update(name='google')
>>> D1
{'age': '33', 'name': 'google', 'ID': 12}
增加3
>>> D1.update((('red',2),))
>>> D1
{'age': '33', 'name': 'google', 'red': 2, 'ID': 345}
修改1
>>> D1.update({'ID':345})
>>> D1
{'age': '33', 'name': 'google', 'ID': 345}

删除pop(key) 
popitem()
clear()清空字典
>>> D1
{'age': '33', 'name': 'google', 'red': 2, 'ID': 345}
>>> D1.pop('red')
2
>>> D1
{'age': '33', 'name': 'google', 'ID': 345}
>>> D1.popitem()
('age', '33')


>>> b=[6]
>>> d={'a':1,'b':b,'c':[1,3,5]}
>>> d
{'a': 1, 'c': [1, 3, 5], 'b': [6]}

>>> for i in d:
...     print i
... 
a
c
b
>>> for n in d:
...     print d[i]
... 
[6]
[6]
[6]
>>> d
{'a': 1, 'c': [1, 3, 5], 'b': [6]}

>>> for n in d:
...     print d[n]
... 
1
[1, 3, 5]
[6]
>>> for n in d:
...     print d.get(n)
... 
1
[1, 3, 5]
[6]


>>> for item in d.items():
...     print item
... 
('a', 1)
('c', [1, 3, 5])
('b', [6])
>>> d
{'a': 1, 'c': [1, 3, 5], 'b': [6]}

>>> for k,v in d.items():
...     print(k,v)
... 
('a', 1)
('c', [1, 3, 5])
('b', [6])
```