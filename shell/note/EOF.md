
```shell
#!/bin/bash
cat <<EOF>log.txt
This is a generated file
EOF

```

重定向操作符>   和>> 可以将输出发送到文件中而不是终端，> 会清空原文件，>>是追加

处理错误输出的时候，一般把输出倒入到/dev/null 中，/dev/null是个特殊设备文件，会丢弃任何收到的数据，null是设备黑洞，数据进去不付复返


将文件重定向到命令
cmd < file

2 重定向脚本内部的文本块

cat <<EOF>log
This is a generated file
EOF

出现在cat <<EOF>log 与下一个EOF行之间的所有文本都会被当作stdin数据


