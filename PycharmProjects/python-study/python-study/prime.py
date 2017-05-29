#!/usr/bin/python _*_ coding: utf-8  _*_
#求一定范围内的素数,素数就是只能被1和它本身整除的数

a=int(raw_input("请输入一个搜索素数的大于0整数范围\n"))

for i in range(2,a):
    for m in range(2,i):
        if (i/m)== int(i/m):
            break
    else:
        print i,
#为什么没有返回值，看下面输出
#>>>i=100
#>>>m=32
#>>>i/m
#>>>3
#在python2中默认整数相除得出的就是整除，在python3中可以用这个，两数相除不含小数，则这个分母不是素数


#参考1
def find_prime(m):
	for n in range(2,m):
		for i in range(2,n):
			if n % i == 0:
				break
		else:
			print n ,

if a < 2:
	print("数字小于1，重新输入")
else :
	print "数字 %d 范围以内所有质数为\n" %a
	print find_prime(a)