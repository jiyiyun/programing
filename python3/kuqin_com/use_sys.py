#!/usr/bin/python
#Filename: using_sys.py

import sys
print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe python path is",sys.path)

#它如何工作
#首先，我们利用import语句 输入 sys模块。基本上，这句语句告诉Python，我们想要使用这个模块。sys模块包含了与Python解释器和它的环境有关的函数。
#当Python执行import sys语句的时候，它在sys.path变量中所列目录中寻找sys.py模块。如果找到了这个文件，这个模块的主块中的语句将被运行，然后这个模块将能够被你 使用 。注意，初始化过程仅在我们 第一次 输入模块的时候进行。另外，“sys”是“system”的缩写。
#sys模块中的argv变量通过使用点号指明——sys.argv——这种方法的一个优势是这个名称不会与任何在你的程序中使用的argv变量冲突。另外，它也清晰地表明了这个名称是sys模块的一部分。
#sys.argv变量是一个字符串的 列表 （列表会在后面的章节详细解释）。特别地，sys.argv包含了 命令行参数 的列表，即使用命令行传递给你的程序的参数。
#如果你使用IDE编写运行这些程序，请在菜单里寻找一个指定程序的命令行参数的方法。
#这里，当我们执行python using_sys.py we are arguments的时候，我们使用python命令运行using_sys.py模块，后面跟着的内容被作为参数传递给程序。Python为我们把它存储在sys.argv变量中。
#记住，脚本的名称总是sys.argv列表的第一个参数。所以，在这里，'using_sys.py'是sys.argv[0]、'we'是sys.argv[1]、'are'是sys.argv[2]以及'arguments'是sys.argv[3]。注意，Python从0开始计数，而非从1开始。
#sys.path包含输入模块的目录名列表。我们可以观察到sys.path的第一个字符串是空的——这个空的字符串表示当前目录也是sys.path的一部分，这与PYTHONPATH环境变量是相同的。这意味着你可以直接输入位于当前目录的模块。否则，你得把你的模块放在sys.path所列的目录之一。
