#!/bin/bash

#made a random number(0~100),and guess , return bigger or smaller,when guess the right number exit


#made random number(0~100)
NUM=$[RANDOM%100+1]
count=0
while :
do
	read -p "Input your guess number: " guess_number
	let count+=1
	if [ $guess_number -gt $NUM ];then
		echo Too Bigger \ This is your $count times 
	elif [ $guess_number -lt $NUM ];then
		echo Too Small \ This is your $count times
	else
		echo "You guess OK"
		echo "Your guess count is $count"
		exit
	fi
done
