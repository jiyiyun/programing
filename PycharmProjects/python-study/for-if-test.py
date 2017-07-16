#!/usr/bin/env python

a = int(raw_input("please the number of people\n"))

b=range(a+1)

while len(b) > 3:
    b = b[::3]
    if len(b)<3:
        print b
        break