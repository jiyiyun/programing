#!/bin/bash

count=10

while [ $count -gt 0 ]
do
    echo "This is shell script test"
    echo $count
    count=$[ $count - 1 ]
done
