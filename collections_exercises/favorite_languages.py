#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: favorite_languages
@time: 2020/4/4 4:22 PM
@desc:
'''
from collections import OrderedDict

# favorite_languages = OrderedDict()
favorite_languages = dict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print name.title() + "'s favorite language is " + language.title() + "."