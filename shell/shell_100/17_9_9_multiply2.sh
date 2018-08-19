#!/bin/bash

for m in {1..9}
do
	for n in $(seq $m)
	do
	    printf "%d*%d=%d\t" $n $m `echo $[ $m * $n ]`
	done
	echo
done

