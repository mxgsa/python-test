#!/usr/bin/env python
# -*- coding: utf-8 -*-

'简单处理Memcached的操作'

# 引入模块
import memcache

def conn():
    mem=memcache.Client(['127.0.0.1:11211'])
    # 集成的写法
    # mem = memcache.Client([('127.0.0.1:11211',1)],[('192.168.1.222:11211',2)])
    # 添加一条键值对，如果已经存在的 key，重复执行add操作异常
    mem.add('name','mengxg')
    print mem.get('name')
    # 输出 mengxg

    # 设置不存在添加，存在就replace
    mem.set('name','mengxg1')
    print mem.get('name')
    # 输出 mengxg1

    # 替换一条键值对，如果不存在的 key，会操作异常
    mem.replace('name','mengxg2')
    print mem.get('name')
    # 输出 mengxg2

    # 设置多个键值对
    mem.set_multi({'name':'mengxg','password':'123456','nickname':'mengxg'})
    print mem.get_multi(['name','password','nickname'])
    # 输出 {'password': '123456', 'nickname': 'mengxg', 'name': 'mengxg'}
    print mem.get('password')
    # 输出 123456

    mem.set('count',0)
    # incr  自增，将Memcached中的某一个值增加 N （ N默认为1 ）
    mem.incr('count',100)
    print mem.get('count')
    # 输出 100

    mem.incr('count')
    print mem.get('count')
    # 输出 101

    # decr 自减，将Memcached中的某一个值减少 N （ N默认为1 ）
    mem.decr('count',10)
    print mem.get('count')
    # 输出 91

    # 删除key键值对
    mem.delete('count')

    print mem.get('count')
    # 输出 None

if __name__=='__main__':
    conn()