#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: class_exercises
@time: 2020/4/3 12:25 AM
@desc:
'''

"""
魔法方法__new__()
"""


class Class(object):
    __num = 0

    @classmethod
    def add_num(cls):
        cls.__num += 1

    @classmethod
    def get_num(cls):
        return cls.__num

    def __new__(cls, name):
        Class.add_num()
        return super(Class, cls).__new__(cls, name)
        # return object.__new__(cls, name)


class Student(Class):

    def __init__(self, name):
        self.name = name
        print name


a = Student('Li Lei')
b = Student('Han Meimei')
print Class.get_num()
