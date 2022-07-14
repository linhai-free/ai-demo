#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: color
@time: 2020/4/3 12:20 AM
@desc:
'''

"""
1、继承与覆盖
2、静态方法（staticmethod）、类方法（classmethod）、实例方法
"""


class Color(object):
    color = "color"
    spectrum = 'visible light'

    X = 1
    Y = 2

    @classmethod
    def value(cls):
        print cls.color

    @staticmethod
    def averag(*mixes):
        print sum(mixes) / 1

    @staticmethod
    def static_method():
        print Color.averag(Color.X, Color.Y)

    @classmethod
    def class_method(cls):
        print cls.averag(cls.X, cls.Y)


class Red(Color):
    color = "red"
    spectrum = 'red light'

    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):
        print sum(mixes) / 2


class Green(Color):
    color = "green"
    spectrum = 'green light'

    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):
        print sum(mixes) / 2


g = Green()

# 类方法
# g.value()
# Green.value()

# 子类继承了父类的静态方法，调用该方法，还是调用的父类的方法和类属性
Green.static_method()

# 子类继承了父类的类方法，调用该方法，调用的是子类的方法和子类的类属性。
Green.class_method()

