#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python连接redis数据库，实现发布者模式'

__author__ = 'mengxg'

from RedisConnUtils import RedisConnUtils

def publish_demo():
    utils = RedisConnUtils("chat_channel")
    for i in range(1,4):
        content=raw_input('please input publish msg:')
        utils.publish(content)

if __name__=='__main__':
    publish_demo()
