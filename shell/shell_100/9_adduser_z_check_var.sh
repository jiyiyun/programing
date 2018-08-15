#!/bin/bash

read -p "User Name: " username

if [ -z $username ];then
    echo "Please enter username: "
    exit 2
fi

# stty -echo close shell output on screen
# stty open shell output on screen

stty -echo

read -p "Password: " pass
stty echo
pass=${pass:-123456}
useradd "$username"
echo "$pass" | passwd --stdin "$username"
echo username=$username password=$pass 

read -p "Delete the account you create before ？(y|n) (yes|no) " command
case $command in
y|yes)
    userdel -r $username
    echo $username is deleted
;;
n|no)
    exit
;;
*)
    echo "Input right choice"
;;
esac
