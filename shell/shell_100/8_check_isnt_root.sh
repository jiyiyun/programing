#!/bin/bash

USERID=`id -u`

if [ $USERID -eq 0 ];then
	echo "You are administrator account"
else
	echo "You are ordinary user"
fi
