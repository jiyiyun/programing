#!/bin/bash

# sum all chars
# awk has NR for line
# awk has length() count chars on line ,every line has a secrt $ in end of line for linux
# wc can count $ on every line  ,use cat -A see 
# $0 is filename  $1 first parameter

awk '{chars+=length($0)+1;words+=NF} END{print NR,words,chars}' $1
