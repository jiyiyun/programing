#!/bin/bash

for m in {1..9}
do
	for n in {1..9}
	do
	    echo "$n * $m = "$[ $m * $n ]
	done
done

