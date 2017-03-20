#!/usr/bin/env python
# -*- coding: utf-8 -*-

'socket服务端创建'

__author__='mengxg'

'''
本文学习的重点：
1、了解Tcp的流程
2、tcp多线程
3、两种类型的写法
'''

# 常规的socket服务端写法
'''
import socket
import threading,time

def server_start():
    server=socket.socket()
    server.bind('127.0.0.1',8090)
    server.listen(10)
    flag=True
    print 'server:127.0.0.1:8080 start success'
    print 'wait for connection...'

    while flag:
        # 接受一个新连接:
        sock, addr = server.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcpconn, args=(sock, addr))
        t.start()

def tcpconn(sock,addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome user'+addr[0])
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('you input: %s!' % data)
    sock.close()

    if __name__=='__main__':
        server_start()

'''







# 采用内部封装好的SocketServer模块
'''
SocketServer内部使用 IO多路复用 以及 “多线程” 和 “多进程” ，
从而实现并发处理多个客户端请求的Socket服务端。即：每个客户端请求连接到服务器时，
Socket服务端都会在服务器是创建一个“线程”或者“进 程” 专门负责处理当前客户端的所有请求。
注：导入模块的时候 3.x版本是socketserver 2.x版本是SocketServer
'''
import SocketServer

class MySever(SocketServer.BaseRequestHandler):
    def handle(self):
        print 'server:127.0.0.1:8080 start success'
        print 'wait for connection...'
        conn=self.request
        conn.sendall('Welcome user '+self.client_address[0])
        flag=True
        while flag:
            data=conn.recv(1024)
            print 'receive data:',data,' from ip:'+self.client_address[0]
            if data=='exit':
                conn.sendall('exit')
                flag=False
                print 'server stop'
            else:
                conn.sendall('you input:'+data)

if __name__=='__main__':
    print 'server:127.0.0.1:8080 ready to start'
    print 'wait for connection...'
    server=SocketServer.ThreadingTCPServer(('127.0.0.1',8090),MySever)
    server.serve_forever()
