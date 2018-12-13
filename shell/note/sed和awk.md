sed和awk
---

$ sed 's/is/aaaaa/' a.txt

$ sed -e 's/is/aaaaaa/; s/a/bbbbbbb/' a.txt

cat 可以将字符串追加到行尾，sed 可以替换

cat /etc/aaa >> /usr/bbb  #将aaa文件内容追加到bbb

------------------------------------------------------------------------------

AWK 报表生成器，格式化文本输出

基本用法：
awk [options] 'program' var=value file ...
awk [options] -f programfile var=value file...
awk [options] 'BEGIN{action;...} pattern{action;...} END{action;...}' file...
awk通常由BEGIN语句块，能够使用模式匹配的通用语句块，END语句块
program通常被单引号或者双引号中

选项
-F 指明字段分隔符filed
-v var=value :自定义变量

$ which awk
/usr/bin/awk
root@rich:~# ls -l  /usr/bin/awk 
lrwxrwxrwx 1 root root 21 4月   5 10:00 /usr/bin/awk -> /etc/alternatives/awk

# awk '{print "hello awk"}'
sfs
hello awk

# awk 'BEGIN{print "hello awk"}'
hello awk

program: pattern{action

做数字运算
$ awk 'BEGIN {print 3**4}'
81

