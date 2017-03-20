#!/usr/bin/env python
# -*- coding: utf-8 -*-

'socket练习使用'

__author__='mengxg'

'''
本文学习的重点：
1、了解Tcp的流程
2、模拟http的Tcp链接过程
3、熟悉python的io操作
'''

# 导入socket库:
import socket

# 创建一个socket:AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.baidu.com', 80))
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
# 把所有接受的数据链接一起
data = ''.join(buffer)
# 关闭连接:
s.close()

# 拆分http的respone请求头header和body
header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的body数据写入文件:
with open('baidu.html', 'wb') as f:
    f.write(html)