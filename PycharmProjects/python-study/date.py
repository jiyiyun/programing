#!/usr/bin/env python  _*_ coding: utf-8  _*_
#输入某年某月某日，判断这一天是这一年的第几天？
Input_Year=int(raw_input("请输入年\n"))

Year_List1=[31,28,31,30,31,30,31,31,30,31,30,31]
Year_List2=[31,29,31,30,31,30,31,31,30,31,30,31]
if Input_Year%4 == 0:
    year=Year_List2
else:
    year=Year_List1

Input_Month=int(raw_input("请输入月\n"))
while Input_Month>12 or Input_Month<1:
    Input_Month=int(raw_input("请输入正确的月份"))
Input_Date=int(raw_input("请输入日\n"))
while Input_Date >year[Input_Month-1] or Input_Date <0:
    Input_Date=int(raw_input("请输入正确的日期"))

Month_Date=0
All_Date=0
for i in range(0,Input_Month-1):
    Month_Date=Month_Date+year[i]

All_Date=Month_Date+Input_Date
print "这天是%d年的第%d天" %(Input_Year,All_Date)

#原资料参考
year=int(raw_input('year:\n'))
month=int(raw_input('month:\n'))
day=int(raw_input('day:\n'))
months=(0,31,59,90,120,151,181,212,243,273,304,334)
if 0<=month<=12:
    sum=months[month-1]
else:
    print 'data error'
sum +=day
leap=0
if (year%400==0)or((year%4==0)and(year%100!=0)):
    leap=1
if(leap==1)and(month>2):
    sum+=1
print 'it is the %dth day.' % sum