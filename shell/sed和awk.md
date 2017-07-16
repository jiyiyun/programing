sed和awk
---

$ sed 's/is/aaaaa/' a.txt

$ sed -e 's/is/aaaaaa/; s/a/bbbbbbb/' a.txt

cat 可以将字符串追加到行尾，sed 可以替换

cat /etc/aaa >> /usr/bbb  #将aaa文件内容追加到bbb
