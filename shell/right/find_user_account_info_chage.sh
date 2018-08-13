#!/bin/bash

read -p "Input user name: " username

#find is this user exsist

user=`cat /etc/passwd |awk -F: '{print $1}' |grep $username`
RETVAL=$?

if [ $RETVAL -eq 0 ];then
	echo "user $username is exsist"
else
	echo "user $username is not exist"
fi

# export user chage list
sudo  chage -l $username
