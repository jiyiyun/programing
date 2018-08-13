#!/bin/bash

echo "Please number1"
read num1

echo "Please number2"
read num2

echo "$num1 + $num2 = " $[ $num1 + $num2 ]
echo "$num1 - $num2 = " $[ $num1 - $num2 ]
echo "$num1 * $num2 = " $[ $num1 * $num2 ]
echo "$num1 / $num2 = " $[ $num1 / $num2 ]

echo "The end $?"

