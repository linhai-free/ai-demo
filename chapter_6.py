#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: chapter
@time: 2020/3/28 12:06 AM
@desc:
'''

"""
字典
"""
alien_0 = {}
alien_0.update({
    'color': 'green',
    'points': 5
})
# print alien_0['color']
# print alien_0['points']
# for item in alien_0.values():
#     print item
# for k, v in alien_0.iteritems():
#     print k + ' ' + str(v)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print alien_0

# alien_0['color'] = 'yellow'
# print alien_0

# del alien_0['color']
# print alien_0

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()):
    print name.title() + ', thank you for taking the poll.'