#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python连接redis数据库，实现订阅者模式'

__author__ = 'mengxg'

from RedisConnUtils import RedisConnUtils

def subscibe_demo():
    utils = RedisConnUtils("chat_channel")
    sub = utils.subscribe()
    while True:
        resut=sub.parse_response()
        print 'receive the publish msg:', resut

if __name__=='__main__':
    subscibe_demo()
