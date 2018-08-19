#!/bin/bash

read -p "Enter IP: " ip

if [[ $ip =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]];then
    echo "It is an IP"
else
    echo "This is not IP "
fi
