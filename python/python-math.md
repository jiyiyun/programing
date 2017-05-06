数学运算
===

绝对值
---

```txt
>>> abs(99)
99
>>> abs(99.99)
99.99
>>> abs(-99.99)
99.99
>>> math.fabs(3.12)
3.12
>>> math.fabs(-3.12)
3.12
>>> fabs(-0.1882)
Traceback (most recent call last):
>>> fabs(-88)
Traceback (most recent call last):
```
对比发现abs是输出绝对值的，fabs是输出浮点数绝对值的


取整
---

```txt
>>> math.ceil(1.456)
2.0

>>> math.floor(9.99)
9.0
>>> math.floor(-1.234)
-2.0
```

ceil是英文天花板的意思，floor是地板的意思
对应的给一个带小数的数字，ceil区最大整，floor取小整

示例：

```txt
>>> math.ceil(1.2345)
2.0
>>> math.floor(1.2345)
1.0
>>> math.ceil(-1.2345)
-1.0
>>> math.floor(-1.2345)
-2.0
```

```
>>> max(-132,-1.23,355,78,-10)
355
>>> min(-0.1,999,3)
-0.1
>>> cmp(4,9)
-1
>>> cmp(0,0)
0
>>> cmp(3,3)
0
>>> cmp(-10,10)
-1
>>> math.exp(7)
1096.6331584284585
```

求以自然数e为底的数字N的底数
---

```txt
>>> math.log(9)
2.1972245773362196
以10为底的自然数N的底数
>>> math.log10(9)
0.9542425094393249
>>> math.log10(100)
2.0
```

输出最大值
---

>>> max(-1.23,4.67,299)
299
输出最小值
>>> min(-0.11,-30,60)
-30


求X的N次方
---

>>> pow(3,6)
729

求平方根
---
>>> math.sqrt(5)
2.23606797749979

原文

http://www.cnblogs.com/linjiqin/p/3608541.html