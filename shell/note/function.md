Function

```shell
function fname()
{
    statements;
}

#或者

fname()
{
    statements;
}

#最简单的 
fname() {statements; }

（2） 只需要使用函数名就可以调用函数

$ fname ;  #执行函数

（3）函数可以按位置访问，$1 $2 ...，$1是第一个参数，$2是第二个参数。

fname arg1 arg2 ;

fname()
{
    echo $1,$2;  #访问参数1和参数2
    echo "$@";   #以列表形式一次打印所有参数
    echo "$*";   #类似于$@ 所有参数视为单个实体
    return 0;    #返回值
}

$0   脚本名称
$1   第一个参数
$2   第二个参数
$n   第N个参数
$@   被扩展成$1 $2 $3等
$*   被扩展成$1c$2c$3 其中c是IFS的第一个字符
$@   要比$* 用的多，由于$*将所有参数当作单个字符串，所以很少用

```

以下命令将所有用户进程数量限制为100
hard nproc 100

```txt
richard@richard-PC:~$ cat /etc/security/limits.conf
# /etc/security/limits.conf
#
#Each line describes a limit for a user in the form:
#
#<domain>        <type>  <item>  <value>
#
#Where:
#<domain> can be:
#        - a user name
#        - a group name, with @group syntax
#        - the wildcard *, for default entry
#        - the wildcard %, can be also used with %group syntax,
#                 for maxlogin limit
#        - NOTE: group and wildcard limits are not applied to root.
#          To apply a limit to the root user, <domain> must be
#          the literal username root.
#
#<type> can have the two values:
#        - "soft" for enforcing the soft limits
#        - "hard" for enforcing hard limits
#
#<item> can be one of the following:
#        - core - limits the core file size (KB)
#        - data - max data size (KB)
#        - fsize - maximum filesize (KB)
#        - memlock - max locked-in-memory address space (KB)
#        - nofile - max number of open files
#        - rss - max resident set size (KB)
#        - stack - max stack size (KB)
#        - cpu - max CPU time (MIN)
#        - nproc - max number of processes
#        - as - address space limit (KB)
#        - maxlogins - max number of logins for this user
#        - maxsyslogins - max number of logins on the system
#        - priority - the priority to run user process with
#        - locks - max number of file locks the user can hold
#        - sigpending - max number of pending signals
#        - msgqueue - max memory used by POSIX message queues (bytes)
#        - nice - max nice priority allowed to raise to values: [-20, 19]
#        - rtprio - max realtime priority
#        - chroot - change root to directory (Debian-specific)
#
#<domain>      <type>  <item>         <value>
#

#*               soft    core            0
#root            hard    core            100000
#*               hard    rss             10000
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
#ftp             -       chroot          /ftp
#@student        -       maxlogins       4

# End of file
```
