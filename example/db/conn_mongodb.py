#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python连接mongodb数据库，实现增删改查'

__author__ = 'mengxg'

'''
本文学习的重点：
1、python连接mongodb数据库
2、mongodb数据库的增删改查
'''

# 使用PyMongo模块对MongoDB进行操作 版本3.4.0
# 有可能不同版本的操作方法不一样

from pymongo import MongoClient
import pymongo

# 获取mongodb的连接 默认ip：127.0.0.1 port：27017
connection = MongoClient()

# 选择python_test库
db = connection.python_test

# 使用p_users集合
collection = db.p_users

# 清空集合 remove 删除所有数据，
# remove() 用于删除单个或全部文档，删除后的文档无法恢复
collection.remove()

# 插入一条数据
collection.insert({'username': 'mengxg', 'password': 'password', 'nickname': 'mengxg', 'age': 0,})

# 初始化生成多条数据
insert_data = []
for i in range(10):
    data = {'username': 'mengxg' + str(i), 'password': 'password' + str(i), 'nickname': 'mengxg' + str(i), 'age': i}
    insert_data.append(data)

# 插入多条数据
collection.insert(insert_data)

# 查询 age 小于 1 的
print  '(+)age 小于 1------------------------------'
for u in collection.find({"age":{"$lt":1}}): print u

# 查询 username 等于 mengxg8 的
print  '(+)username 等于 mengxg8------------------------------'
for u in collection.find({"username":"mengxg8"}): print u

# 查询特定键值的
print  '(+)特定键值 age=9------------------------------'
for u in collection.find({"age":9}, ["username", "nickname"]): print u

# 多条件查询
print  '(+)多条件查询 ------------------------------'
for u in collection.find({'age': {'$gt': 3, '$lt': 15}, 'username': 'mengxg5'}): print u

#  排序sort
#  pymongo.ASCENDING 也可以用 1 来代替
# pymongo.DESCENDING 也可以用 -1 来代替
# 按照age正序排 order by age asc
print  '(+)order by age asc 3条记录------------------------------'
for u in collection.find().sort([("age", pymongo.ASCENDING)]).limit(3): print u

# 按照age倒序排列  order by age desc
print  '(+)order by age desc 3条记录------------------------------'
for u in collection.find().sort([("age", pymongo.DESCENDING)]).limit(3): print u

# order by age asc, username desc
print  '(+)order by age asc, username desc 3条记录------------------------------'
for u in collection.find().sort([("age", pymongo.ASCENDING), ("username", pymongo.DESCENDING)]).limit(3): print u
# sort 的另一种写法
print  '(+)order by age asc, username desc 另一种写法3条记录------------------------------'
for u in collection.find(sort = [("age", pymongo.ASCENDING), ("username", pymongo.DESCENDING)]).limit(3): print u
# 组合写法
print  '(+)order by age asc, username asc and username=mengxg9------------------------------'
for u in collection.find({"username":"mengxg9"}, sort=[['age',1],['username',1]]): print u


# 获取总数
print 'totalcount:', collection.count()

# 获取所有数据
print  '(+)所有数据------------------------------'
for u in collection.find(): print u

# 获取 age>7的 或者 age<3的数据
# $where: 用 JS 代码来代替有些丑陋的 $lt、$gt。
# MongoDB 内置了 Javascript Engine (SpiderMonkey)。
# 可直接使用 JS Expression，甚至使用 JS Function 写更复杂的 Code Block。
print  '(+)获取age>7 || age<3的数据------------------------------'
for u in collection.find({'$where':'this.age > 7 || this.age < 3'}): print u
print '------'
for u in collection.find().where("this.age > 7 || this.age < 3"): print u
print '------'
for u in collection.find().where('function(){ return this.age > 7 || this.age < 3;}'): print u

# 输出结果
'''
(+)age 小于 1------------------------------
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
(+)username 等于 mengxg8------------------------------
{u'username': u'mengxg8', u'password': u'password8', u'age': 8, u'_id': ObjectId('58d0f816aca12b27b4079695'), u'nickname': u'mengxg8'}
(+)特定键值 age=9------------------------------
{u'username': u'mengxg9', u'_id': ObjectId('58d0f816aca12b27b4079696'), u'nickname': u'mengxg9'}
(+)多条件查询 ------------------------------
{u'username': u'mengxg5', u'password': u'password5', u'age': 5, u'_id': ObjectId('58d0f816aca12b27b4079692'), u'nickname': u'mengxg5'}
(+)order by age asc 3条记录------------------------------
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg1', u'password': u'password1', u'age': 1, u'_id': ObjectId('58d0f816aca12b27b407968e'), u'nickname': u'mengxg1'}
(+)order by age desc 3条记录------------------------------
{u'username': u'mengxg9', u'password': u'password9', u'age': 9, u'_id': ObjectId('58d0f816aca12b27b4079696'), u'nickname': u'mengxg9'}
{u'username': u'mengxg8', u'password': u'password8', u'age': 8, u'_id': ObjectId('58d0f816aca12b27b4079695'), u'nickname': u'mengxg8'}
{u'username': u'mengxg7', u'password': u'password7', u'age': 7, u'_id': ObjectId('58d0f816aca12b27b4079694'), u'nickname': u'mengxg7'}
(+)order by age asc, username desc 3条记录------------------------------
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg1', u'password': u'password1', u'age': 1, u'_id': ObjectId('58d0f816aca12b27b407968e'), u'nickname': u'mengxg1'}
(+)order by age asc, username desc 另一种写法3条记录------------------------------
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg1', u'password': u'password1', u'age': 1, u'_id': ObjectId('58d0f816aca12b27b407968e'), u'nickname': u'mengxg1'}
(+)order by age asc, username asc and username=mengxg9------------------------------
{u'username': u'mengxg9', u'password': u'password9', u'age': 9, u'_id': ObjectId('58d0f816aca12b27b4079696'), u'nickname': u'mengxg9'}
totalcount: 11
(+)所有数据------------------------------
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
{u'username': u'mengxg1', u'password': u'password1', u'age': 1, u'_id': ObjectId('58d0f816aca12b27b407968e'), u'nickname': u'mengxg1'}
{u'username': u'mengxg2', u'password': u'password2', u'age': 2, u'_id': ObjectId('58d0f816aca12b27b407968f'), u'nickname': u'mengxg2'}
{u'username': u'mengxg3', u'password': u'password3', u'age': 3, u'_id': ObjectId('58d0f816aca12b27b4079690'), u'nickname': u'mengxg3'}
{u'username': u'mengxg4', u'password': u'password4', u'age': 4, u'_id': ObjectId('58d0f816aca12b27b4079691'), u'nickname': u'mengxg4'}
{u'username': u'mengxg5', u'password': u'password5', u'age': 5, u'_id': ObjectId('58d0f816aca12b27b4079692'), u'nickname': u'mengxg5'}
{u'username': u'mengxg6', u'password': u'password6', u'age': 6, u'_id': ObjectId('58d0f816aca12b27b4079693'), u'nickname': u'mengxg6'}
{u'username': u'mengxg7', u'password': u'password7', u'age': 7, u'_id': ObjectId('58d0f816aca12b27b4079694'), u'nickname': u'mengxg7'}
{u'username': u'mengxg8', u'password': u'password8', u'age': 8, u'_id': ObjectId('58d0f816aca12b27b4079695'), u'nickname': u'mengxg8'}
{u'username': u'mengxg9', u'password': u'password9', u'age': 9, u'_id': ObjectId('58d0f816aca12b27b4079696'), u'nickname': u'mengxg9'}
(+)获取age>7 || age<3的数据------------------------------
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
{u'username': u'mengxg1', u'password': u'password1', u'age': 1, u'_id': ObjectId('58d0f816aca12b27b407968e'), u'nickname': u'mengxg1'}
{u'username': u'mengxg2', u'password': u'password2', u'age': 2, u'_id': ObjectId('58d0f816aca12b27b407968f'), u'nickname': u'mengxg2'}
{u'username': u'mengxg8', u'password': u'password8', u'age': 8, u'_id': ObjectId('58d0f816aca12b27b4079695'), u'nickname': u'mengxg8'}
{u'username': u'mengxg9', u'password': u'password9', u'age': 9, u'_id': ObjectId('58d0f816aca12b27b4079696'), u'nickname': u'mengxg9'}
------
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
{u'username': u'mengxg1', u'password': u'password1', u'age': 1, u'_id': ObjectId('58d0f816aca12b27b407968e'), u'nickname': u'mengxg1'}
{u'username': u'mengxg2', u'password': u'password2', u'age': 2, u'_id': ObjectId('58d0f816aca12b27b407968f'), u'nickname': u'mengxg2'}
{u'username': u'mengxg8', u'password': u'password8', u'age': 8, u'_id': ObjectId('58d0f816aca12b27b4079695'), u'nickname': u'mengxg8'}
{u'username': u'mengxg9', u'password': u'password9', u'age': 9, u'_id': ObjectId('58d0f816aca12b27b4079696'), u'nickname': u'mengxg9'}
------
{u'username': u'mengxg', u'password': u'password', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968c'), u'nickname': u'mengxg'}
{u'username': u'mengxg0', u'password': u'password0', u'age': 0, u'_id': ObjectId('58d0f816aca12b27b407968d'), u'nickname': u'mengxg0'}
{u'username': u'mengxg1', u'password': u'password1', u'age': 1, u'_id': ObjectId('58d0f816aca12b27b407968e'), u'nickname': u'mengxg1'}
{u'username': u'mengxg2', u'password': u'password2', u'age': 2, u'_id': ObjectId('58d0f816aca12b27b407968f'), u'nickname': u'mengxg2'}
{u'username': u'mengxg8', u'password': u'password8', u'age': 8, u'_id': ObjectId('58d0f816aca12b27b4079695'), u'nickname': u'mengxg8'}
{u'username': u'mengxg9', u'password': u'password9', u'age': 9, u'_id': ObjectId('58d0f816aca12b27b4079696'), u'nickname': u'mengxg9'}
'''