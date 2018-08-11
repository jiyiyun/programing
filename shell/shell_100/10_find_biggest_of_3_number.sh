#!/bin/bash

#input 3 number and find biggest middle smallest of 3 number

read -p "Input First Number: " num1
read -p "Input Second Number: " num2
read -p "Input Third Number: " num3

if [ $num1 -gt $num2 ];then
	bigger=$num1
       	small=$num2
else
	bigger=$num2
       	small=$num1
fi

if [ $bigger -gt $num3 ];then
	echo "biggest is $bigger"
	if [ $small -gt $num3 ];then
		echo "middle is $small"
		echo "smallest is $num3"
	else
		echo "middle is $num3"
		echo "smallest is $small"
	fi
else
	echo "biggest is $num3"
	echo "middle is $bigger"
	echo "smallest is $small"
fi
