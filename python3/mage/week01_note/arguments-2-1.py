#编写一个函数，能够接收知识2个参数，返回最大值和最小值
#import random
def double_values(x,y,*nums):
#    print(nums)
    return max(x,y,*nums), min(x,y,*nums)

#print(*double_values(*[random.randint(10,20) for _ in range(10)]))
#print(double_values(2))
print(double_values(3,4))
print(double_values(2,3,4,5))
print(double_values(33,11,44,66,22,121,9))