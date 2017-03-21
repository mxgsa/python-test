#!/usr/bin/env python
# -*- coding: utf-8 -*-

'socket udp协议练习使用'

__author__ = 'mengxg'

'''
本文学习的重点：
1、了解udp的流程
'''

# 导入socket库:
import socket

'''
UdpServer类，创建一个udp的服务端
用法：
    p = UdpServer('127.0.0.1',8090)
    p.start()
无限循环监听端口，process重写数据处理方式
'''
class UdpServer:
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.bind((ip, port))

    def reveicedata(self):
        data, addr = self.udp.recvfrom(1024)
        print 'receive data:%s  from:%s ' % (data, addr)
        return (data, addr)

    def senddata(self, addr, data):
        self.udp.sendto(data, addr)

    def process(self, data):
        result = ''
        if data == 'hello':
            result = 'welcome!'
        else:
            result = data
        return result
    def close(self):
        self.udp.close()

    def start(self):
        while True:
            print 'wait for connect'
            data,addr = self.reveicedata()
            result=self.process(data)
            self.senddata(addr,result)
        self.close()


if __name__=='__main__':
    p=UdpServer('127.0.0.1',9000)
    p.start()

