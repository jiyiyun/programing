#!/bin/bash

case $# in
0)
	echo "You enter $# vars You vars is $*"
;;
1)
	echo "Enter vars is $# Vars is $* "
;;
2)
	echo "Enter vars  is $# vars is $* "
;;
*)
	echo "The var is more than 2 The var number is $# The var is $*"
;;
esac

