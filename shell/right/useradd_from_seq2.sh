#!/bin/bash

MINDAYS=7
MAXDAYS=90
WARNING=10
INACTIVE=15

read -p "User name: " username
read -p "Number of user: " number
for m in $(seq -w $number)
do
    password=`echo $RANDOM | md5sum | cut -c1-9`
    #password=`echo "date $RANDOM" | md5sum | cut -c2-11`
    #password=`openssl rand -base64 8 | md5sum | cut -c1-9`
    useradd $username$m
    echo $password | passwd --stdin $username$m
    chage -m $MINDAYS $username$m
    chage -M $MAXDAYS $username$m
    chage -W $WARNING $username$m
    chage -I $INACTIVE $username$m
    echo  "user=$username$m \t password=$password"
    echo -e "user=$username$m \t password=$password" >>user_password.log
done

# seq -w 01 10  To made  -w, --equal-width

#userdel  ,This is use case 

read -p "Delete the user you create before: y|n yes|no " command

case $command in
y|yes)
    for n in $(seq -w $number)
    do
        userdel -r $username$n
        echo "$username$n is deleted"
    done
rm -f ./user_password.log
;;
n|no)
    exit
;;
esac
