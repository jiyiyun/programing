shell编程1环境变量可变数组
---

环境变量

- 查看全局环境变量printenv
- 查看局部环境变量set

```txt
suseserver:~ # test=100                        #设置环境变量
suseserver:~ # echo $test                      #查看
100
suseserver:~ # export test                     #将环境变量设为全局环境变量
suseserver:~ # unset test                       #删除环境变量
suseserver:~ # echo $test
```

- /etc/profile文件是系统默认的启动文件，每个用户都有的，
- $HOME目录下的启动文件

```txt
$HOME/.bash_profile
$HOMR/.bash_login
$HOMR/.profile
```

交互式shell
---

如果不是系统登录的时候启动的，(比如敲命令的时候执行的) 称为交互式shell,如果bash作为交互式shell启动的，
不会去访问用户的/etc/profile文件，而是去用户的HOME目录检查.bashrc是否存在

.bashrc有两个作用

- 查看/etc目录下的共用bashrc文件
- 为用户提供了一个定制自己的命令别名和私有脚本函数的地方

通用的/etc/bashrc启动文件会被系统上每个交互式shell会话的用户执行

cat /etc/bashrc


可变数组
---

```bash
suseserver:~ # mytest=[1,2,3,4,5,6]
suseserver:~ # echo $mytest
[1,2,3,4,5,6]

suseserver:~ # mytest1=(1,2,3,4,5,6)
suseserver:~ # echo $mytest1
1,2,3,4,5,6

suseserver:~ # mytest2=(one two three four five)
suseserver:~ # echo $mytest2
one                                               #问题出现了，应该全部显示，现在只出现一个
```

```bash
suseserver:~ # echo ${mytest2[2]}
three

suseserver:~ # echo ${mytest2[*]}
one two three four five

```

> 是覆盖写入某个文件 ，>> 是追加写入
---

```shell
suseserver:~ # date > a.txt 
suseserver:~ # cat a.txt 
Sun Apr 16 16:58:38 CST 2017
suseserver:~ # who > a.txt 
suseserver:~ # cat a.txt 
richard  :0           Apr 16 15:55 (console)
richard  console      Apr 16 15:55 (:0)
root     pts/0        Apr 16 15:56 (192.168.100.1)
suseserver:~ # date > a.txt 
suseserver:~ # cat a.txt 
Sun Apr 16 16:59:21 CST 2017
suseserver:~ # who >> a.txt 
suseserver:~ # cat a.txt 
Sun Apr 16 16:59:21 CST 2017
richard  :0           Apr 16 15:55 (console)
richard  console      Apr 16 15:55 (:0)
root     pts/0        Apr 16 15:56 (192.168.100.1)
```

command <  file  #将文件内容提取出来给命令使用

```shell
suseserver:~ # wc < a.txt 
  4  24 165

suseserver:~ # cat a.txt 
Sun Apr 16 16:59:21 CST 2017
richard  :0           Apr 16 15:55 (console)
richard  console      Apr 16 15:55 (:0)
root     pts/0        Apr 16 15:56 (192.168.100.1)
Sun Apr 16 17:08:16 CST 2017

suseserver:~ # sort a.txt          #等价于sort < a.txt
Sun Apr 16 16:59:21 CST 2017
Sun Apr 16 17:08:16 CST 2017
richard  :0           Apr 16 15:55 (console)
richard  console      Apr 16 15:55 (:0)
root     pts/0        Apr 16 15:56 (192.168.100.1)

suseserver:~ # cat a.txt     #可以看到sort 没有动源文件 
Sun Apr 16 16:59:21 CST 2017
richard  :0           Apr 16 15:55 (console)
richard  console      Apr 16 15:55 (:0)
root     pts/0        Apr 16 15:56 (192.168.100.1)
Sun Apr 16 17:08:16 CST 2017

```

管道 | pip
---

```shell
suseserver:~ # rpm -qa|grep bin|sort|more   #查找bin名称的rpm包并sort ,more
bind-libs-32bit-9.9.9P1-46.1.x86_64
bind-libs-9.9.9P1-46.1.x86_64
bind-utils-9.9.9P1-46.1.x86_64
binutils-2.26.1-9.12.1.x86_64
libdcerpc-binding0-32bit-4.4.2-29.4.x86_64
libdcerpc-binding0-4.4.2-29.4.x86_64
libgstbasecamerabinsrc-1_0-0-1.8.3-9.6.x86_64
libinput10-1.1.1-2.1.x86_64
rpcbind-0.2.3-21.4.x86_64
samba-winbind-32bit-4.4.2-29.4.x86_64
samba-winbind-4.4.2-29.4.x86_64
yast2-perl-bindings-3.1.2-1.11.x86_64
yast2-pkg-bindings-3.1.34-6.1.2.x86_64
yast2-ruby-bindings-3.1.51-9.1.2.x86_64
yast2-ycp-ui-bindings-3.1.9-1.6.x86_64
ypbind-1.37.2-5.8.x86_64
```

```txt
suseserver:~ # rpm -qa|grep dhcp > dhcp.test
suseserver:~ # cat dhcp.test 
dhcp-4.3.3-9.1.x86_64
dhcp-client-4.3.3-9.1.x86_64
yast2-dhcp-server-3.1.11-10.1.2.noarch
```
```txt
suseserver:~ # rpm -qa|grep dhcp |sort  > dhcp.test
suseserver:~ # cat dhcp.test 
dhcp-4.3.3-9.1.x86_64
dhcp-client-4.3.3-9.1.x86_64
yast2-dhcp-server-3.1.11-10.1.2.noarch
```

数学运算 expr
---

```shell
suseserver:~ # expr 1+5
1+5
suseserver:~ # expr 1 + 5
6

suseserver:~ # expr 4 * 5
expr: syntax error
suseserver:~ # expr 4*5
4*5
suseserver:~ # expr 4 \* 5    #要用转义符 \
20

suseserver:~/shell-test # expr 4 \/ 2
2
```
```shell
#!bin/bash

a=123
b=321

c=expr `$b \* $a`
echo $c
```
上述有报错

```shell
#!bin/bash

a=123
b=321

c=`expr $b \* $a`
echo $a \* $b is $c
```

```txt
suseserver:~/shell-test # sh expr-1.sh 
123 * 321 is 39483
```
反引号要放在expr外边，否则报错

使用[]
---

```shell
#!bin/bash

a=123
b=321
c=93

d=$[$a * ($b + $c)]
echo $d  
```
