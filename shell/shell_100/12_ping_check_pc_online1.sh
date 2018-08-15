#!/bin/bash

# 192.168.4.x 

# Usage: ping [-aAbBdDfhLnOqrRUvV64] [-c count] [-i interval] [-I interface]
#             [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
#	      [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
#             [-w deadline] [-W timeout] [hop1 ...] destination

read -p "192.168.x.0/24 Input x: " x

if [ $x -ge 0 ] && [ $x -le 255 ];then
	echo $x is in range
else
	echo "$x is not in range(0,255),x  should in {0,254}"
	exit
fi

for i in {1..254}
do {
      	ping -c4  -i1 -W2 192.168.$x.$i &>/dev/null
	if [ $? -eq 0 ];then
		echo "192.168.$x.$i is up"
		echo 192.168.$x.$i >>/tmp/ip.log
	fi
}&
done
wait
count=`cat /tmp/ip.log|wc -l`
echo "Total PC online on net $x is $count"
rm -f /tmp/ip.log
