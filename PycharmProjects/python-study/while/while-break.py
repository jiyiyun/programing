#!/usr/bin/env python _*_ coding utf-8 _*_

while True:
    name=input("Enter name")
    if name == "stop": break
    age =input("Enter age")
    print("hello",name, "=>",int(age) ** 2)