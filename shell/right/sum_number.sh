#!/bin/bash

declare -x sum=0
read -p "Enter the number:>>> " number

for i in $(seq $number);
do
    sum=$[$sum+$i]
done

echo "The total of " $number is $sum
