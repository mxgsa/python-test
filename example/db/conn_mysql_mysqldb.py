#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python连接mysql数据库，实现增删改查'

__author__ = 'mengxg'

'''
本文学习的重点：
1、python连接mysql数据库
2、mysql数据库的增删改查
'''


# 简单介绍MySQL-python的使用方法
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    db='python_test',
)
cur = conn.cursor()

# 创建数据表
# cur.execute("create table p_users(id int ,username varchar(20),password varchar(30),nickname varchar(10))")

# 插入一条数据 插入多套executemany
# cur.execute("insert into p_users values('mengxg','password','mengxg')")


# 修改查询条件的数据
# cur.execute("update p_users set password='password111' where username = 'mengxg'")

# 删除查询条件的数据
# cur.execute("delete from p_users where id=1")

# 查询数据
# fetchone() 游标逐条记录获取
# scroll(0,'absolute') 定位到第一条数据
sql = "select * from p_users"
result=cur.execute(sql)
# 打印总记录数
print 'total data record:',result
print cur
# 逐条获取数据
print 'fetchone data:',cur.fetchone()

#打印获取的总记录,会发现只有一条记录，是因为签名的fetchone的原因
print 'total data:',cur.fetchmany(result)

# 定位到第一条数据，再去获取所有记录
cur.scroll(0,'absolute')
#打印获取的总记录
print 'total data:',cur.fetchmany(result)


conn.commit()
conn.close()

# 输出
# total data record: 2
# <MySQLdb.cursors.Cursor object at 0x00000000028D06A0>
# fetchone data: (1L, 'mengxg', 'password', 'mengxg')
# total data: ((2L, 'mengxg', 'password', 'mengxg'),)
# total data: ((1L, 'mengxg', 'password', 'mengxg'), (2L, 'mengxg', 'password', 'mengxg'))
