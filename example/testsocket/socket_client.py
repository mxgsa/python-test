#!/usr/bin/env python
# -*- coding: utf-8 -*-

'socket客户端链接服务端'

__author__='mengxg'

'''
本文学习的重点：
1、了解Tcp的流程
2、tcp收发数据
'''
import socket

class SocketClient:
    def __init__(self,ip,port):
        self._ip=ip
        self._port=port

    def start(self):
        ip_port=(self._ip,self._port)
        client=socket.socket()
        print ip_port
        client.connect(ip_port)
        while True:
            data=client.recv(1024)
            if data=='exit':
                print 'server stop!'
                break
            print 'receive data:'+data
            instr=raw_input('please input string:')
            # 发送数据，返回发送数据字节数，有可能没有发送完字符串的数据
            # client.send(instr)
            # 一次性发送所有字符串数据
            client.sendall(instr)
        client.close()

if __name__=='__main__':
    try:
        s_client=SocketClient('127.0.0.1',8090)
        s_client.start()
    except StandardError,e:
        print 'socket error ',e



