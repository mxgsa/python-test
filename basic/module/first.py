#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a first create module'

__author__='mengxg'

# 第1行和第2行是标准注释，第1行注释可以让该文件直接在Unix/Linux/Mac上运行，
# 第2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串，表示模块的文档注释，可以填写该文件写的功能描述
# 第6行表是文档的作者
# 上面为python的标准文件模版，也可以全部去掉，最好按照标准来写，没有坏处

#引入内建的sys模块
import sys

#定义一个函数test
def test():
    args=sys.argv
    #argv用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    print args[0]
    #判断args有几个参数，根据参数不同进行相应的操作
    if len(args)==1:
        print 'hello world!'
    elif len(args)==2:
        print 'hello ',args[1]
    else:
        print 'args:',args

# 定义一个私有的加法操作
def __private_add(x,y):
    return x+y

# 定义一个私有的减法操作
def __private_sub(x,y):
    return x-y

# 定义的public公开的函数，根据类型调用相应的操作
def opt(x,y,opt_type):
    if opt_type==1:
        return __private_add(x,y)
    else:
        return __private_sub(x,y)


# Python解释器把一个特殊变量__name__置为__main__，如果该文件被引用，将不执行该操作，可以作为模块单元测试使用
if __name__=='__main__':
    test()

