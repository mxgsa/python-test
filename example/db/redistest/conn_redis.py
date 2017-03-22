#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python连接redis数据库，实现简单的操作'

__author__ = 'mengxg'

'''
本文学习的重点：
1、python连接redis数据库
2、redis数据库的简单操作
'''

# 简单介绍redis-py的使用方法
# 引用redis模块
import redis
import time

'''
#在Redis中设置值，默认不存在则创建，存在则修改
r.set('name', 'zhangsan')
参数：
     set(name, value, ex=None, px=None, nx=False, xx=False)
     ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
     xx，如果设置为True，则只有name存在时，当前set操作才执行
'''


# 常规连接方法
def basic_conn():
    # 建立redis数据库连接
    redisdb = redis.Redis(host='127.0.0.1', port=6379)
    # 设置简单的key value
    redisdb.set('username', 'mengxg')
    print 'key=username value：', redisdb.get('username')
    print 'key=username1 value：', redisdb.get('username1')
    redisdb.set('username', 'mengxg1')
    print 'key=username value：', redisdb.get('username')

    # 增加过期时间2秒
    redisdb.setex('username', 'mengxg', 2)
    # 修改3秒后读取数据
    time.sleep(3)
    print 'setex() key=username value：', redisdb.get('username')

    # 批量设置值
    redisdb.mset({"name1": 'zhangsan', "name2": 'lisi'})
    # 打印单一值
    print 'mset() key=name1 value：', redisdb.get('name1')
    print 'mset() key=name1 name2 value：', redisdb.mget('name1', 'name2')

    # 设置新值，打印原值
    print 'getset():', redisdb.getset("name1", "wangwu")
    print 'getset() new:', redisdb.get("name1")

    # 获取自增整数,每次自定递增，默认递增数为1，自定义递增数可以设置amount
    print 'incr() default :', redisdb.incr("mount")
    print 'incr() amount=2 :', redisdb.incr("mount", amount=5)  # 输出:2
    # 相同函数 incrbyfloat(self, name, amount=1.0) 类似 incr() 自增,amount为自增数(浮点数)

    # 自减函数
    print 'decr() default :', redisdb.decr("mount")

    # 当然还有其他操作，具体使用场景也不一样，大家可以自行研究
    # hash操作 redis中的Hash 在内存中类似于一个name对应一个dic来存储
    # List 操作 redis中的List在在内存中按照一个name对应一个List来存储
    # Set 操作 Set集合就是不允许重复的列表
    # Z操作有序集合 在集合的基础上，为每元素排序，元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。


'''
输出：
key=username value： mengxg
key=username1 value： None
key=username value： mengxg1
setex() key=username value： None
mset() key=name1 value： zhangsan
mset() key=name1 name2 value： ['zhangsan', 'lisi']
getset(): zhangsan
getset() new: wangwu
incr() default : 6
incr() amount=2 : 11
decr() default : 10
'''


def poolcoon():
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    redisdb = redis.Redis(connection_pool=pool)
    redisdb.set('username', 'mengxg')
    print (redisdb.get('username'))
    # 其他常规操作都类似，可以参考上面，也可自行研究


'''
输出
mengxg
'''


# redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
# 如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。
# 经过测试 插入1000条数据，不使用管道耗时328毫秒 使用管道耗时37毫秒
# 测试10万条数据的时候，不使用管道要40秒，实用管道378毫秒。速度提升很大啊
def pipeconn():
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    redisdb = redis.Redis(connection_pool=pool)
    # 使用管道模式
    pipe = redisdb.pipeline(transaction=True)
    redisdb.set('usermane', 'mengxg')
    redisdb.set('password', 'password')
    redisdb.set('nickname', 'mengxg')
    # 一起提交数据
    pipe.execute()

if __name__ == '__main__':
# basic_conn()
# poolcoon()
    pipeconn()

