#!/bin/bash

read -p "Input the number: " number

declare -x sum=0

for i in $(seq $number);
do
	let sum+=$i
done

echo The Sum of 1 to $number is : $sum
