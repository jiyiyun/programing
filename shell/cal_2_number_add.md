简单数学加法运算a+b
===

```txt
richard@richard-PC:~/shell_study$ a=3
richard@richard-PC:~/shell_study$ b=4
richard@richard-PC:~/shell_study$ echo $a +$b |bc
7
#使用bc运算器

richard@richard-PC:~/shell_study$ expr $a + $b
7
#使用expr

richard@richard-PC:~/shell_study$ echo $[$a + $b]
7
使用echo
```
