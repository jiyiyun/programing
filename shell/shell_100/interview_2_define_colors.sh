#!/bin/bash

#example 1
function echo_color() {
    if [ $1 == "green" ];then
        echo -e "\033[32;40m$2\033[0m"
    elif [ $1 == "red" ]; then
        echo -e "\033[31;40m$2\033[0m"
    fi
}

#example 2
function echo_color2() {
    case $1 in
        green)
	    echo -e "\033[32;40m$2\033[0m"
	    ;;
	red)
	    echo -e "\033[31;40m$2\033[0m"
	    ;;
	*)
            echo "choose: green | red"
    esac
}

echo_color green "test"

echo_color2 red "red"
