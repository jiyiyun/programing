解压赋值给多个变量
---

``` shell
>>> p = (4,5)
>>> x,y = p
>>> x
4
>>> y
5

>>> data = ['python',50,91.1,(2016,12,6)]
>>> name,shares,price,date = data
>>> name
'python'
>>> date
(2016, 12, 6)
```

压缩可迭代对象给多个变量
---
``` shell
def drop_first_last(grades):
    first,*meddle,last = grades
    return avg(middle)
```
``` shell
>>> record =('Dave','dave@example.com','773-555-1212','847-555-1212')
>>> name,email,*phone_numbers = record
>>> name
'Dave'
>>> email
'dave@example.com'
>>> phone_numbers
['773-555-1212', '847-555-1212']
```
```shell
>>> line = 'nobody:*:-2:2:Unprivileged User:/var/empty:usr/bin/false'
>>> uname,*fields,homedir,sh=line.split(':')
>>> uname
'nobody'
>>> homedir
'/var/empty'
>>> sh
'usr/bin/false'
>>> fields
['*', '-2', '2', 'Unprivileged User']
```
查找最大、最小的N个元素
---
```shell
>>> import heapq
>>> nums = [1,3,2,23,4,-4,77,-32]
>>> print(heapq.nlargest(3,nums))
[77, 23, 4]
>>> print(heapq.nsmallest(3,nums))
[-32, -4, 1]
```
