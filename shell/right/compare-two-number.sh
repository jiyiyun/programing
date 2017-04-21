#!/bin/bash
#compare a and b

value1=10
value2=13

if [ $value1 -ge $value2 ]
then
   echo "$value1 is great or equal than $value2"
fi

if [ $value1 -eq $value2 ]
then
    echo "$value1 is equal $value2"
fi

if [ $value1 -gt $value2 ]
then
    echo "$value1 is great than $value2"
fi

if [ $value1 -lt $value2 ]
then
    echo "$value1 is litter than $value2"
fi
