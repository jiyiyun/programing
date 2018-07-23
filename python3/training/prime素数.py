i = int(input("input a number\n"))
import _datetime
starttime = _datetime.datetime.now()
count=0
for m in range(1,i+1):
    for n in range(2, m):
        count +=1
        if m % n == 0:
            break
    else:
        print(m, end=',')
endtime = _datetime.datetime.now()
print("\nThis cost of time is",(endtime - starttime))
print("The total cont is",count)