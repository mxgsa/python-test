#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python连接mysql数据库，实现增删改查'

__author__ = 'mengxg'

'''
本文学习的重点：
1、python连接mysql数据库
2、mysql数据库的增删改查
'''

# 使用纯python的mysql连接驱动
# 使用 Connector/Python 进行查询操作。
import mysql.connector
import logging


class MysqlUtils:
    def __init__(self, **config):
        # 初始化数据库连接
        self._conn = mysql.connector.connect(**config)

    # 创建游标
    def __cursor(self):
        return self._conn.cursor()

    # 执行查询操作
    def select(self, sql, params=None):
        cursor = self.__cursor()
        result_ret = None
        try:
            cursor.execute(sql, params)
            result_ret = cursor.fetchall()
        except Exception, e:
            logging.error(
                "Error. SQL = %s, params = %s, Error.msg=%s " % (sql, str(params).encode(" utf8 "), e))
        finally:
            cursor.close()
        return result_ret

    def __commit(self):
        # 如果数据库引擎为Innodb，执行完成后需执行_conn.commit()进行事务提交
        self._conn.commit()

    def insert(self, sql, params=None):
        cursor = self.__cursor()
        last_id = -1
        try:
            cursor.execute(sql, params)
            last_id = cursor.lastrowid
        except Exception, e:
            logging.error(
                " Error SQL = %s, params = %s, Error.msg=%s " % (sql, str(params).encode(" utf8 "), e))
        finally:
            self.__commit()
            cursor.close()
        return last_id

    def close(self):
        self._conn.close()


if __name__ == '__main__':
    # 数据库连接dict
    config = {'host': '127.0.0.1',  # 默认127.0.0.1
              'user': 'root',
              'password': '',
              'database': 'python_test',
              'use_unicode': 'True'
              }
    myutils = MysqlUtils(**config)
    # 插入sql语句
    sql_insert = 'insert into p_users(username,password,nickname) VALUES (%s,%s,%s)'
    # 传入参数值
    params = ('mengxg', 'password', 'mengxg')
    last_id = myutils.insert(sql_insert, params)
    if last_id > -1:
        print 'insert user success id:', last_id

    # 查询sql语句
    sql_select = 'select * from p_users'
    result = myutils.select(sql_select)
    for row in result:
        print "id:%d, username:%s, password:%s, nickname:%s" % (row[0], row[1], row[2], row[3])
    # 关闭数据库连接
    myutils.close()

    # 输出 ：
    # insert user success id: 2
    # id:1, username:mengxg, password:password, nickname:mengxg
    # id:2, username:mengxg, password:password, nickname:mengxg


