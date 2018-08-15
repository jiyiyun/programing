#!/bin/bash

# 192.168.4.x 

# Usage: ping [-aAbBdDfhLnOqrRUvV64] [-c count] [-i interval] [-I interface]
#             [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
#	      [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
#             [-w deadline] [-W timeout] [hop1 ...] destination

declare -x count=0

for i in {1..254}
do
	echo This time go $i
	ping -c2  -i0.2 -W0.3 192.168.4.$i &>/dev/null
	if [ $? -eq 0 ];then
		echo "192.168.4.$i is up"
		let count+=1
	fi
done

echo "The total PC online is $count"
