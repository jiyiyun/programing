#!/usr/bin/env python _*_ coding: utf-8_*_

y = int(input("please input a int number\n"))
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, "has factor",x)
        break
    x -= 1
else:
    print(y, "is prime" )