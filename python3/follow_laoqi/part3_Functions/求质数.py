#质数：只能被1和本身整除的元素

def find_prime(m):
	for n in range(2,m):
		for i in range(2,n):
			if n % i == 0:
				break
		else:
			print(n ,end=',')


m=int(input("请输入一个大于1的整数\n"))
if m < 2:
	print("数字小于1，重新输入")
else :
	print("数字 %d 范围以内所有质数为\n" %m)
	print(find_prime(m))
	input('\n')