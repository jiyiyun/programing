#!/bin/bash

if [ -e ./namefile ];then
    for NAME in `cut -d: -f1 ./namefile`;
    do
        useradd $NAME &>/dev/null
        MINDAYS=$(grep $NAME ./namefile |cut -d: -f2)
        MAXDAYS=$(grep $NAME ./namefile |cut -d: -f3)
        WARNING=$(grep $NAME ./namefile |cut -d: -f4)
        INACTIVE=$(grep $NAME ./namefile |cut -d: -f5)
        
        chage -m $MINDAYS $NAME
        chage -M $MAXDAYS $NAME
        chage -W $MINDAYS $NAME
        chage -I $MINDAYS $NAME
        echo $NAME | passwd --stdin $NAME &>/dev/null
    done
else
    echo "check you passwd or namefile"
fi

# cat namefile
#tom:10:90:31:21
#jack:13:94:30:22
#harry:15:96:32:23
#jeff:14:97:17:24
#machal:17:98:22:25
#mark:4:97:22:26
