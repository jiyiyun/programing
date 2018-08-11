#!/bin/bash

for i in {1..3}
do
read -p "user name: " username
read -p "password: " password

if [ $username == 'tom' -a $password == '123456' ];then
	echo "Login Success"
	exit
fi
done
    echo "Login Failed"
