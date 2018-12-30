file IO
===

open 打开文件
read 读取文件
write 写入文件
close 关闭文件
readline  行读取
readlines 多行读取
seek 文件指针操作
tell 指针位置

open(file,mode='r',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)

文件操作最常用的就是读和写

open函数
r 默认的，只读打开
w 只写打开
x 创建并写入一个新文件
a 写入打开，如果文件存在，则追加
b 二进制模式
t 缺省的,文本模式
+ 读写打开一个文件

```shell
>>> f=open('test.txt','a')
>>> f.write('this is a test file')
19
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x0000002EDA27EA68>

>>> print(f.read())
this is a test file
```