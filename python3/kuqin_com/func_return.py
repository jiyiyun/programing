#!/usr/bin/python
#Filename: func_return.py

def maximum(x,y):
	if x > y:
		return x
	else:
		return y

print("The max of 10 and 20 is " , maximum(10,20))

#没有返回值的return语句等价于return None。None是Python中表示没有任何东西的特殊类型。例如，如果一个变量的值为None，可以表示它没有值。

#除非你提供你自己的return语句，每个函数都在结尾暗含有return None语句。通过运行print someFunction()，你可以明白这一点，函数someFunction没有使用return语句
# def someFunction():
#    pass 
#pass语句在Python中表示一个空的语句块。