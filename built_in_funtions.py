#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: built_in_funtions
@time: 2020/4/18 5:01 PM
@desc:
'''

# enumerate()函数
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print list(enumerate(seasons))
# for i, e in enumerate(seasons, start=1):
#     print str(i) + ': ' + e
#     # print type(item)

# split()函数
# text = '你好！吃早饭了吗？再见。'
# for e in text.split('！|？'):
#     print e.decode('utf-8')

# re模块的split()函数
import re
text = '你好！吃早饭了吗？再见。'
for e in re.split('！|？', text):
    print e.decode('utf-8')

