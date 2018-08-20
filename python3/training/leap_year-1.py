year=int(input("Year=: "))

if (year%4 ==0) and (year%100 !=0) or (year%400 ==0):
    print("%d is Leap Year\n" %year)
else:
    print("%d is a common year\n" %year)