集合set特性:可变，不重复，无序
===
```shell
>>> s7={[1],(1,),1}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

报错原因：set的元素必须是可以hash的，list 和set不可以hash

```shell
help(set)
 add(...)
     Add an element to a set.

     This has no effect if the element is already present.

 clear(...)
     Remove all elements from this set.

 copy(...)
     Return a shallow copy of a set.
pop(...)
|   Remove and return an arbitrary set element.
|   Raises KeyError if the set is empty.|
remove(...)
|      Remove an element from a set; it must be a member.
|      If the element is not a member, raise a KeyError.	

  union(...)
      Return the union of sets as a new set.

      (i.e. all elements that are in either set.)

  update(...)
      Update a set with the union of itself and others.
  Data and other attributes defined here:

  __hash__ = None
```

发现不支持索引，可以迭代

```shell
>>> s1={1,2,3}
>>> s1
{1, 2, 3}
>>> s1.add('a')
>>> s1
{1, 2, 3, 'a'}
>>> s2={3,4,5}
>>> s1.update(s2)
>>> s1
{1, 2, 3, 4, 5, 'a'}

remove()属性在remove不存在元素时会报错，discard不存在元素时不会抛出异常
>>> s1.remove('a')
>>> s1
{1, 2, 3, 4, 5}
>>> s1.remove('b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'b'
>>> s1.discard(5)
>>> s1
{1, 2, 3, 4}
>>> s1.discard(6)
>>> s1
{1, 2, 3, 4}

pop()敲出任意元素，而且不可以指定，为什么是任意呢？(个人觉得因为用hash算法决定剔除那个元素)
>>> s1.pop()
1
>>> s1
{2, 3, 4}
>>> s1.pop(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop() takes no arguments (1 given)
```

set 要么删除元素remove,pop，要么添加元素add,update 没有修改元素(个人觉得因为重创建开始已经建立起一对一的hash映射)
非线性，无法索引
遍历：可以遍历所有元素
成员运算符，可以使用in 和not in 判断是否在set中
效率高,(redis就是最好的应用)
set和线性结构
线性结构的查询时间复杂度为O(n),set ，dict等结构，内部使用hash作为key，时间复杂度可以做到O(1)查询时间和数据规模无关

可hash的类型 数值型，布尔型，字符串型，tuple,None,这些都是不可变类型都可以hashable
集合的运算
并集union(*others)  等同于 | 
合集update(*others) 等同于 |=
交集intersection(*others)  等同于 &
交集并就地修改intersection_update(*others) 等同于 &=

```shell
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a&b
{4, 5}
>>> a
{1, 2, 3, 4, 5}
>>> b
{8, 4, 5, 6, 7}
>>> a&=b
>>> a
{4, 5}
>>> b
{8, 4, 5, 6, 7}
```

```txt
差集 difference(*others) 等同于 -
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a-b
{1, 2, 3}
>>> a
{1, 2, 3, 4, 5}
差集并修改difference_update(*others)  等同于 -=

对称差集：所有不属于A和B交集的元素组成的集合 (交集取反)
symmetric_difference(other)  等同于^
symmetric_difference_update  等同于^=

issubset(other) <=   判断前个集合是否是另一个集合的子集
set1 < set2  #判断set1 是否是set2的真子集
issuperset(other) >=  #是否是other的超集
set1 > set2
isdisjoint(other) #判断是否有交集,没有返回True
集合的应用
1、共同好友(交集)  2、都不是好友(isdisjoint)  3、权限判断(要求具有ABC权限才能)4、总任务表找出未完成任务
```


