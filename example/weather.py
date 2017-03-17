#!/usr/bin/env python
# -*- coding: utf-8 -*-

'根据提供的接口获取当天的天气情况'

__author__ = 'mengxg'

'''
新浪天气接口api  http://php.weather.sina.com.cn/xml.php?city=%B1%B1%BE%A9&password=DJOYnieT8234jlsK&day=0
北京当天的天气
返回的格式：XML
'''

import requests
from xml.parsers.expat import ParserCreate


class Weather(object):
    def __init__(self):
        self._day = 0
        self._pwd = 'DJOYnieT8234jlsK'
        self._city = '%B1%B1%BE%A9'

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str):
            self._city = value
        else:
            self._city = '%B1%B1%BE%A9'

    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, value):
        if isinstance(value, str):
            self._pwd = value
        else:
            self._pwd = 'DJOYnieT8234jlsK'

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            self._day = 0
        else:
            self._day = value

    def getWeather(self):
        url = 'http://php.weather.sina.com.cn/xml.php?city=' + self.city + '&password=' + self.pwd + '&day=' + str(
            self.day)
        print url
        r = requests.get(url)
        return r.content


import xml.dom.minidom

ELEMENT_NODE = xml.dom.Node.ELEMENT_NODE

class SimpleXmlGetter(object):
    def __init__(self, data):
        if type(data) == str:
            self.root = xml.dom.minidom.parse(data)
        else:
            self.root = data

    def __getattr__(self, name):  # support . operation
        if name == 'data':
            return self.root.firstChild.data
        for c in self.root.childNodes:
            if c.nodeType == ELEMENT_NODE and c.tagName == name:
                return SimpleXmlGetter(c)

    def __getitem__(self, index):  # support [] operation
        eNodes = [e for e in self.root.parentNode.childNodes
                  if e.nodeType == ELEMENT_NODE and e.tagName == self.root.tagName]
        return SimpleXmlGetter(eNodes[index])

    def __call__(self, *args, **kwargs):  # support () openration, for query conditions
        for e in self.root.parentNode.childNodes:
            if e.nodeType == ELEMENT_NODE:
                for key in kwargs.keys():
                    if e.getAttribute(key) != kwargs[key]:
                        break
                else:
                    return SimpleXmlGetter(e)

'''
if __name__ == "__main__":
    x = SimpleXmlGetter("sysd.xml")
    print x.sysd.sysagent.param[2].data
    print x.sysd.sysagent.param(name="querytimeout", type="second").data
'''

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


if __name__ == '__main__':
    w = Weather()
    result = w.getWeather()
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.returns_unicode = True
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(result)
