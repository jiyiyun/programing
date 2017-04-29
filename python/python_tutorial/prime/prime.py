#!/usr/bin/env python

a=int(raw_input("please input a number more than 2 "))

def prime(a):
    """ This is prime number"""
    for n in range(2,a):
        for x in range(2,n):
            if n%x ==0:
                #print n,'euqls',x,'x',n/x
                break
            else:
                #loop fell through without finding a factor
                print n,
                break

print prime(a)        
