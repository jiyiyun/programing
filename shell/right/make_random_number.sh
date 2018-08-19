#!/bin/bash

#The number of echo
read -p "Input The number: " number

#made random number
RANDOM=$[RANDOM%100+1]

for i in $(seq $number)
do
    echo $i  $(($RANDOM%100+1)) $(date) >> ./random_test.txt
    
done

