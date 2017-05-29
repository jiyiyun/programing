#!/usr/bin/env python _*_ coding: utf-8 _*_

#number
import math
import random

print 'len(str(2**10)) is ',len(str(2**10))
print 'math.pi is',math.pi
print 'math.sqrt(100) is',math.sqrt(100)
print 'math.pow(2,3) is',math.pow(2,3)

print 'random.random() is',random.random()
print 'random.choice([2,0,6,4,100,50]) is ',random.choice([2,0,6,4,100,50])

#string
S='python'
print 'S is %s S[1] is %s' %(S,S[1])
print 'S is %s S[-1] is %s' %(S,S[-1])
print 'S is %s S[-1] is %s S[len(S)-1] is %s'%(S,S[-1],S[len(S)-1])
print 'S is %s S[1:3] is %s,S[1::] is %s'%(S,S[1:3],S[1::])
print 'S is %s S[0:3] is %s'%(S,S[0:3])
print 'S is %s S+xyz is %s'%(S,S+'xyz')

#change string
print 'S.find('y')',S.find('y')
print 'S.replace('y','H')',S.replace('y','H')

line='aaaa,bbbb,cccc,dddd'
print line
print 'line.split(',')',line.split(',')
