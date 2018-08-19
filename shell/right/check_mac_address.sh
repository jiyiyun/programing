#!/bin/bash

read -p "Enter MAC address: " mac

if [[ $mac =~ ^([0-9a-fA-F]{2}\:){5}[0-9a-fA-F]{2}$ ]];then
    echo "This is a MAC address"
else
    echo "This is not MAC address"
fi
