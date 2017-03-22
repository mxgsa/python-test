#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python连接redis数据库，实现订阅者和发布者模式'

__author__ = 'mengxg'

'''
本文学习的重点：
1、python连接redis数据库
'''
import redis

# 定义个发布、订阅者类
class RedisConnUtils(object):
    def __init__(self, channel):
        self._channel = channel
        self._redis = redis.Redis(host='127.0.0.1', port=6379)

    # 订阅者
    def subscribe(self):
        pub = self._redis.pubsub()
        pub.subscribe(self._channel)
        pub.parse_response()
        return pub

    # 发布者
    def publish(self, msg):
        self._redis.publish(self._channel, msg)

