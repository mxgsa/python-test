#!/usr/bin/env python
# -*- coding: utf-8 -*-

'引用函数别名'

__author__='mengxg'

# Python标准库一般会提供StringIO和cStringIO两个库
# 两个库的接口和功能是一样的，但是cStringIO是C写的，速度更快,
# 如果引用cStringIO失败，就引入StringIO
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

# 当python版本不一样的时候，内置的一些模块也不一样
# 下面的例子就是解决不同版本的问题
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5