#!/usr/bin/env python
# -*- coding: utf-8 -*-

'简单的用户注册和登录'

__author__='mengxg'

# 存储用户注册的信息
user_db={}

import hashlib

# 创建用户功能的类
class UserInfo:

    def __init__(self,username,password):
        self.username=username
        self.passowrd=password

    # 用户登录
    def userLogin(self):
        if(user_db.has_key(self.username)):
            if user_db[self.username]==self.__get_md5():
                print 'login success'
            else:
                print 'password error'
        else:
            print 'not exits this user'

    # 进行MD5加盐加密
    def __get_md5(self):
        md5 = hashlib.md5()
        md5.update(self.username+self.passowrd+'the salt')
        md5pwd =md5.hexdigest()
        return md5pwd
    # 用户注册
    def userRegister(self):
        user_db[self.username]=self.__get_md5()
        print 'user %s register success!' % self.username

# 实例化用户
user=UserInfo('mengxg','123123')
user.userRegister()
print user_db

user2=UserInfo('mengxg','123123')
user2.userLogin()

'''
输出内容：
user mengxg register success!
{'mengxg': 'bb05c612458cf75135df60200f4a6a29'}
login success
'''
