#!bin/bash
#testing multiple commands

testuser=richard
if grep $testuser /etc/passwd
then
    echo the bash files for user $testuser are :
    ls -a /home/$testuser
fi
