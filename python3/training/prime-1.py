'''
一个数能被从2到自己的平方根整除这数就是合数
'''
import math
n=int(input("N=:"))

for i in range(2,n+1):
    for x in range(2,math.ceil(math.sqrt(i))):
        if i%x == 0:
            break
    else:
        print(i,end=',')