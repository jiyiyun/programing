#!/bin/bash

# Leap Year is can divied by 4 but not 100 ,and can be devided by 400

read -p "Enter the year: " year

if [ -z $year ];then
	echo "Warning! Please  Input a year: "
	exit
elif [[ $year =~ [a-zA-Z] ]];then
	echo "Please Enter number ! "
	exit
fi

if [  $[$year%4] -eq 0 ] && [ $[$year%100] -ne 0 ];then
	echo "$year is Leap Year"
	exit
elif [ $[$year%400] -eq 0 ];then
	echo "$year is Leap Year"
else
	echo common year
fi
