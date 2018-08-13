#!/bin/bash

# declare: usage: declare [-aAfFgilrtux] [-p] [name[=value] ...]

declare -i sum=0

for num in {1..100};
do
	let sum+=$num
done

echo $sum
