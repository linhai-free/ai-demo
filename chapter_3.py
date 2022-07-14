#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: chapter_3
@time: 2020/3/27 12:02 AM
@desc:
'''

"""
列表是什么
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print bicycles
# print bicycles[3]
# print bicycles[3].upper()
# print bicycles[-2].title()

"""
修改、添加和删除元素
"""

motocycles = ['honda', 'yamaha', 'suzuki']
# print motocycles
motocycles[0] = 'ducati'
# print motocycles
# motocycles.append('honda')
# print motocycles
motocycles.insert(-1, 'honda')
# print motocycles

# del motocycles[0]
# print motocycles

# popped_motocycle = motocycles.pop(1)
# print popped_motocycle
# print motocycles

motocycles.remove('honda')
# print motocycles

"""
组织列表
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
# print cars
# cars.sort()
# print cars
# cars.sort(reverse=True)
# print cars
# print sorted(cars, reverse=True)
cars.reverse()
print cars
print len(cars)

motocycles = []
# print motocycles[-1]
print cars[-1]


