'''
>>> help(random.randint)
Help on method randint in module random:
randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
输入10个介于10到20之间的随机数，求相同和不相同的数字，各自共有几个
'''
import random
lst1=[]
lst2=[]
for i in range(10):
    lst1.append(random.randint(10,20))
print("list1 =",lst1)
for n in range(10):
    lst2.append(random.randint(10,20))
print("list2 =" ,lst2)

S1=set(lst1)
S2=set(lst2)
S3=S1.union(S2)
print("The number of uniq is",len(S3))
print("uni=",S3)

S4=S1.intersection(S2)
print("The number of interction",len(S4))
print("intersection is",S4)
