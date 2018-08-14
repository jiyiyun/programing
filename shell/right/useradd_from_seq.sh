#!/bin/bash

MINDAYS=7
MAXDAYS=90
WARNING=10
INACTIVE=15

for n in `seq 01 15`
do
    echo redhat$n
    useradd redhat$n 
    echo redhat$n | passwd --stdin redhat$n
    chage -m $MINDAYS redhat$n
    chage -M $MAXDAYS redhat$n
    chage -W $WARNING redhat$n
    chage -I $INACTIVE redhat$n
    echo -e "username=redhat$n \t password=redhat$n \n" >> user.log
done

read -p "User name: " username
read -p "Number of user" number
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
    echo -e "user=$username$m \t password=$password" >>user_password.log
done

# seq -w 01 10  To made  -w, --equal-width
