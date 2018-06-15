#!/bin/bash

echo "Please input a num"
read num

sum=0
i=1

signal=0

while [ $signal != 1 ]
do
    if [ $i -eq $num ]
    then
        let signal=1
        let sum+=i
        echo "1+2+...+$sum=$sum"
    else
        let sum=sum+i
        let i++
    fi
done
