#!/bin/bash

# example 1
echo $RANDOM |md5sum |cut -c 1-8

# example 2
openssl rand -base64 4

# example 3
cat /proc/sys/kernel/random/uuid |cut -c 1-8
