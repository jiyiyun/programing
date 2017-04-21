#!bin/bash

a=123
b=789

c=`expr $b \* $a`

echo a=$a
echo b=$b
echo "$a * $b ="$c
