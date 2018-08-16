#!/bin/bash

users=$(awk -F: '$3>1000 {print $1}' /etc/passwd)

for i in $users
do
	userdel -r $i
        echo "user $i is deleted"
done
