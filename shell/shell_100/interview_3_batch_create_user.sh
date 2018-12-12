#!/bin/bash

DATE=$(date +%F_%T)
USER_FILE=user.txt
echo_color(){
    if [ $1 == "green" ];then
        echo -e "\033[32;40m$2\033[0m"
    elif [ $1 == "red" ];then
        echo -e "\033[31;40m$2\033[0m"
    fi
}

for USER in user{1..9};do
    if ! id $USER &>/dev/null;then
        PASS=$USER
	useradd $USER
	echo $PASS |passwd --stdin $USER &>/dev/null
	echo -e "$USER User create successful"
    else
	echo_color red "$USER User are already exists!"
    fi
done

ROOT_PASS=t
LST=`echo $ROOT_PASS| sudo --stdin cat /etc/passwd |grep "^user"|awk -F: '{print $1}'`
for NAME in $LST;do
    echo $NAME
done

for DEL_USER in $LST;do
    userdel -r $DEL_USER >>/dev/null 2>&1
    echo "User Delete Sucess"
done

echo $ROOT_PASS |sudo --stdin cat /etc/passwd
