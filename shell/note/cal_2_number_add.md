简单数学加法运算a+b
===

```txt

#使用bc运算器
richard@richard-PC:~$ echo '3*12' |bc
36
richard@richard-PC:~/shell_study$ a=3
richard@richard-PC:~/shell_study$ b=4
richard@richard-PC:~/shell_study$ echo $a +$b |bc
7

--------------------------------------------------------
#使用expr

richard@richard-PC:~/shell_study$ expr $a + $b
7
--------------------------------------------------------
使用echo

richard@richard-PC:~/shell_study$ echo $[$a + $b]
7

--------------------------------------------------------
richard@richard-PC:~$ echo '3*12' |bc
36
richard@richard-PC:~$ a=10
richard@richard-PC:~$ b=20
richard@richard-PC:~$ let c=$a+$b
richard@richard-PC:~$ echo $c
30
richard@richard-PC:~$ echo $[$b-$a]
10

```

