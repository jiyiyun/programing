#!/bin/bash

read -p "User Name: " users
read -p "Enter mysql $user passwd: " password
while :
do
    count=`mysqladmin -u$users -p$password status | awk '{print $3 $4}'`
    echo "`date +%F `  mutitreads is $count"
    exit
done
