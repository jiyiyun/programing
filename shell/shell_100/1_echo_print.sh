#!/bin/bash

echo "Hello shell script --use echo"

printf "You houstname is %s \nYou account is %s \nToday is %s %s %s --use printf \n" $HOSTNAME `whoami` $(date +%c)
