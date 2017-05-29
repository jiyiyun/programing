#!/usr/bin/env python _*_ coding: utf-8 _*_
#题目：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？

import math
for i in range(1,1000000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if (x*x==i+100) and (y*y==i+268):
        print i


#我做的
import math
for i in range(100000):
    x=math.floor(math.sqrt(i+100))
    y=math.floor(math.sqrt(i+268))
    if (x*x==i+100) and (y*y==i+268):
        print i