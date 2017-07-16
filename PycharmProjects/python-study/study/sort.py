#!/usr/bin/env python _*_ coding: utf-8 _*_
#输入三个整数x,y,z，请把这三个数由小到大输出
a=int(raw_input("请输入第一个数字\n"))
b=int(raw_input("请输入第二个数字\n"))
c=int(raw_input("请输入第三个数字\n"))
L=[a,b,c]
L.sort()
for i in L:
    print i