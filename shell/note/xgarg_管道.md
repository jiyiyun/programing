```txt
find /etc -user test -exec cp -a {} /root/find-file  \;
$ sudo find /var/log/ -name *.log -exec cp -a {} /tmp/ \;
$ find /tmp/ -name *.log -exec rm -f {} \;

fine /etc -user test |xargs chown test2
-exec 是找完再执行第二个动作，有可能导致内存溢出
xargs 是找出一个执行一个，只有一个线程
```
