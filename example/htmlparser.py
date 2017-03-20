#!/usr/bin/env python
# -*- coding: utf-8 -*-

'解析html文本，实例：解析豆瓣首页的正在热映的部分，标题，评分'

__author__ = 'mengxg'

'''
本文要点：
1、充分理解HTMLParser的解析过程
2、了解python的正则表达式re模块
3、了解requests模块
'''

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import requests
import re

# 解决UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._flag = {'titlediv': False, 'pingfendiv': False, 'title': False, 'pingfen': False}
        self._move = {}
        self._json = []

    # 处理类似<div></div>的开始标签<div>
    def handle_starttag(self, tag, attrs):
        #  返回标签的属性
        def _attr(attrlist, attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return None

        if tag == 'div' and _attr(attrs, 'class') == 'title':
            self._flag['titlediv'] = True
        elif self._flag['titlediv'] and tag == 'a':
            self._flag['title'] = True
        elif tag == 'div' and _attr(attrs, 'class') == 'rating':
            self._flag['pingfendiv'] = True
        elif tag == 'i' and self._flag['pingfendiv']:
            self._flag['pingfen'] = True

    # 处理类似<div></div>的开始标签</div>
    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        pass

    # 处理类似<img />的开始结束标签
    def handle_startendtag(self, tag, attrs):
        pass
        # print('<%s/>' % tag)

    # 返回类似标签<div>data</div>里面的内容data
    def handle_data(self, data):
        if self._flag['title']:
            self._move['title'] = data;
            self._flag['titlediv'] = False
            self._flag['title'] = False
        if self._flag['pingfen']:
            self._move['pingfen'] = data
            self._json.append(self._move)
            self._move = {}
            self._flag['pingfen'] = False
            self._flag['pingfendiv'] = False

    # 处理注释
    def handle_comment(self, data):
        pass
        # print('<!-- -->')

    # 处理特殊字符串，就是以&#开头的，一般是内码表示的字符
    def handle_entityref(self, name):
        pass
        # print('&%s;' % name)

    # 处理一些特殊字符，以&开头的，比如 &nbsp;
    def handle_charref(self, name):
        pass
        # print('&#%s;' % name)

    # 处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    def handle_decl(self, decl):
        pass
        # Overridable -- handle processing instruction

    # 处理形如<?instruction>的东西
    def handle_pi(self, data):
        pass

    # 处理未知的标签定义
    def unknown_decl(self, data):
        # self.error("unknown declaration: %r" % (data,))
        pass

    def return_data(self):
        return self._json;


def get_movies():
    try:
        url = 'https://www.douban.com/'
        r = requests.get(url)
        result = r.content;
        # 使用正则表达式获取<div class="movie-list list"></div>的内容
        matchs = re.findall(r'<div class="movie-list list">(.*?)</ul>\n</div>', result, re.S)
        # 得到div里面的内容
        result=matchs[0];
        # 使用htmlparser解析div里面的内容
        parser = MyHTMLParser()
        parser.feed(result)
        # 获取返回值
        movies = parser.return_data()
        # 打印值
        for each in movies:
            print('%(title)s|%(pingfen)s' % each)
    except StandardError,e:
        print 'error:',e
    finally:
        r.close()

if __name__=='__main__':
    get_movies()