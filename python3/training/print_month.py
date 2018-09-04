month=int(input("month: "))
year=int(input("year: "))
day=int(input("day: "))
sum_days=0
month_days=0
days=[]

for i in range(month):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        month_days = 31
        days.append(month_days)
    elif i in [4, 6, 9, 11]:
        month_days = 30
        days.append(month_days)
    elif i == 2:
        month_days = 28
        days.append(month_days)
    elif i == 2 and year % 4 == 0:
        month_days = 29
        days.append(month_days)
    else:
        print(" ")
        exit

for n in days:
    sum_days =sum_days + n

print("今天是 %d 年第 %d 天" %(year,(sum_days +day)))