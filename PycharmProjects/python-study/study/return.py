#!/usr/bin/env python _*_ coding: utf-8 _*_

a=int(raw_input("请输入数字a\n"))
b=int(raw_input("请输入数字b\n"))

def Max_Num(x,y):
    if x >y:
        return x
    else:
        return y
print "两个数字中较大的数字是the maxminn of two number is" , Max_Num(a,b)