#!/bin/bash

# 192.168.4.x 

# Usage: ping [-aAbBdDfhLnOqrRUvV64] [-c count] [-i interval] [-I interface]
#             [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
#	      [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
#             [-w deadline] [-W timeout] [hop1 ...] destination

myping(){
    ping -c2 -i0.3 -W1 $1 &>/dev/null
    if [ $? -eq 0 ];then
	    echo $1 is up
            echo $1 >>/tmp/ip.log
    fi
}

for i in {1..254}
do
	myping 192.168.4.$i &
done
wait
count=`cat /tmp/ip.log |wc -l`
echo Total PC online is $count
rm -f /tmp/ip.log
exit
