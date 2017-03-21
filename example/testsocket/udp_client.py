#!/usr/bin/env python
# -*- coding: utf-8 -*-

'socket udp协议练习使用'

__author__ = 'mengxg'

'''
本文学习的重点：
1、了解udp的流程
'''

import  socket

# 设置客户端链接方式为udp方式
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 设置链接地址
addr=('127.0.0.1',9000)
# 定义循环标志
flag=True
while flag:
    # 用户输入数据
    content=str(raw_input('please input :'))
    # 发送数据到服务端
    client.sendto(content,addr)
    # 接受数据
    data,addr=client.recvfrom(1024)
    print 'receive data:%s'% data
    # 如果服务端返回数据exit，结束循环
    if data=='exit':
        flag=False
client.close()
print 'client shutdown!'


