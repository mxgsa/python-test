#!/usr/bin/env python
# -*- coding: utf-8 -*-

'引入 first模块'

__author__='mengxg'

# 引入 first模块
import first

# 定义测试函数，调用first的test（）函数
def test():
    first.test()

def test2():
    print  first.opt(1,2,1)

if __name__=='__main__':
    # 执行second模块test（）函数
    test()
    # 输出 hello world!

    test2()
    # 输出 3
