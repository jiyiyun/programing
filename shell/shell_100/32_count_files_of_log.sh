#!/bin/bash

sum=0

read -p "Input the dir:" dir

if [ -d $dir ];then
	echo "$dir is dir"
else
	echo "$dir is not dir "
	exit
fi

cd $dir

for i in `ls -R *`
do
	if [ -f $i ];then
		echo "file name is $i"
		let sum+=1
	fi
done
echo "Total files is: $sum"
