#!/usr/bin/env python
# -*- coding: utf-8 -*-

'读取bmp图片的信息'

__author__='mengxg'

'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
struct unpack https://docs.python.org/2/library/struct.html#format-characters
'''

import struct

def getbmpinfo(path):
    try :
        # 以二进制方式读取文件
        with open(path,'rb') as f:
            # 读取长度30字节
            bt=f.read(30);
            # 转换字节，根据上面内容去判断
            info=struct.unpack('<ccIIIIIIHH',bt)
            if info[0]=='B' and info[1]=='M':
                print 'this image is bmp'
                print 'image size:%s*%s' % (info[6],info[7])
                print 'image color is:%s' % info[9]
            else:
                print 'this image is not bmp'
    except StandardError,e:
        print 'StandardError:',e

if __name__=='__main__':
    getbmpinfo('1.bmp')