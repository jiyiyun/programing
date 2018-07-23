a=1
b=1
n=int(input("N=:"))
if n<=2:
    sum=1
    print(sum)
else:
    for i in range(n-2):
       a,b=a+b,a
    print(a)