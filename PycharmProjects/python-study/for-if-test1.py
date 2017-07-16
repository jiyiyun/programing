#!/usr/bin/env python

a = int(raw_input("please the number of people\n"))

b=range(a+1)

while len(b) > 6:
    b = b[::6]
    if len(b)<6:
        print b
        break