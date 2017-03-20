#!/usr/bin/env python
# -*- coding: utf-8 -*-

'根据提供的接口获取当天的天气情况'

__author__ = 'mengxg'

'''
本文重点：
1、了解xml ParserCreate的解析过程
2、了解python的requests模块
使用实例：
新浪天气接口api  http://php.weather.sina.com.cn/xml.php?city=%B1%B1%BE%A9&password=DJOYnieT8234jlsK&day=0
北京当天的天气
返回的格式：XML
返回的天气xml实例：
<?xml version="1.0" encoding="UTF-8"?>
<!-- published at 2017-03-20 10:01:54 -->
<Profiles>
<Weather>
<city>北京</city>
<status1>小雨</status1>
<status2>阴</status2>
<figure1>xiaoyu</figure1>
<figure2>yin</figure2>
<direction1>东风</direction1>
<direction2>北风</direction2>
<power1>≤3</power1>
<power2>≤3</power2>
<temperature1>12</temperature1>
<temperature2>6</temperature2>
<ssd>0</ssd>
<tgd1>13</tgd1>
<tgd2>13</tgd2>
<zwx>2</zwx>
<ktk>7</ktk>
<pollution>3</pollution>
<xcz>3</xcz>
<zho></zho>
<diy></diy>
<fas></fas>
<chy>5</chy>
<zho_shuoming>暂无</zho_shuoming>
<diy_shuoming>暂无</diy_shuoming>
<fas_shuoming>暂无</fas_shuoming>
<chy_shuoming>风衣、大衣、夹大衣、外套、毛衣、毛套装、西服套装、薄棉外套</chy_shuoming>
<pollution_l>轻度</pollution_l>
<zwx_l>弱</zwx_l>
<ssd_l>较凉</ssd_l>
<fas_l>暂无</fas_l>
<zho_l>暂无</zho_l>
<chy_l>毛衣类</chy_l>
<ktk_l>建议开启(制热)</ktk_l>
<xcz_l>比较适宜</xcz_l>
<diy_l>暂无</diy_l>
<pollution_s>对空气污染物扩散无明显影响</pollution_s>
<zwx_s>紫外线弱</zwx_s>
<ssd_s>老年、幼儿、体弱者外出需要带上薄围巾、薄手套。</ssd_s>
<ktk_s>建议开启空调</ktk_s>
<xcz_s>洗车后未来2天内没有降水、大风或沙尘天气，比较适宜洗车</xcz_s>
<gm>2</gm>
<gm_l>易发期</gm_l>
<gm_s>天气很凉，季节转换的气候，慎重增加衣服；较易引起感冒；</gm_s>
<yd>5</yd>
<yd_l>不适宜</yd_l>
<yd_s>虽然晴空万里，但是户外运动时会感到很凉；</yd_s>
<savedate_weather>2017-03-20</savedate_weather>
<savedate_life>2017-03-20</savedate_life>
<savedate_zhishu>2017-03-20</savedate_zhishu>
<udatetime>2017-03-20 08:10:00</udatetime>
</Weather>
</Profiles>
'''

import requests
from xml.parsers.expat import ParserCreate
from urllib import quote


class Weather(object):
    def __init__(self):
        self._day = 0
        self._pwd = 'DJOYnieT8234jlsK'
        self._city = u'北京'

    @property
    def city(self):
        st = self._city.encode('gb2312')
        return quote(st)

    @city.setter
    def city(self, value):
        if isinstance(value, str):
            self._city = value
        else:
            self._city = u'北京'

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

# 解析返回xml，返回需要的node的值的json字符串
class DefaultSaxHandler(object):
    def __init__(self, nodes):
        self._curnode = ''
        self._json = {}
        self._nodes = nodes

    # 处理xml的开始标签'<name>data</name>' 的<name>
    def start_element(self, name, attrs):
        self._curnode = name

    # 处理xml的结束标签'<name>data</name>' 的</name>
    def end_element(self, name):
        # print('sax:end_element: %s' % name)
        self._curnode=''

    # 处理xml标签中的值'<name>data</name>' 的data
    def char_data(self, text):
        for st in self._nodes:
            if (self._curnode == st):
                self._json[st] = text
                print text

    def return_json(self):
        return self._json;

if __name__ == '__main__':
    w = Weather()
    result = w.getWeather()
    # print result
    nodes=['city','status1','power1','power2'];
    handler = DefaultSaxHandler(nodes)
    parser = ParserCreate()
    # 设置returns_unicode为True时，返回的所有element名称和char_data都是unicode
    parser.returns_unicode = True
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(result)
    print handler.return_json();
