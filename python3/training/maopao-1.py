'''
要求使用封装和解构来交互数据
'''
lst=[1,9,8,5,6,7,4,3,43,88,2]

for i in range(len(lst)):
    flag = False
    for j in range(1,len(lst)-i):
        if lst[j-1] > lst[j]:
            lst[j-1],lst[j] = lst[j],lst[j-1]
            flag =True
    if not flag:
        break
print(lst)

