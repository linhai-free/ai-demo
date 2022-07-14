#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: test1
@time: 2020/4/3 2:02 PM
@desc:
'''

"""
魔法方法__new__()

1、只有新式类才有魔法方法__new__()，从object类继承的子类，都是新式类。
2、object将__new__()定义成静态方法。
3、传入的参数至少一个cls参数，cls表示需要实例化的类。
"""


class A(object):
    def __init__(self, value):
        print "into A __init__"
        self.value = value

    def __new__(cls, *args, **kwargs):
        print "into A __new__"
        return object.__new__(cls, *args, **kwargs)


# 在调用__init__()初始化前，先调用了__new__()
# 在新式类中，__new__()对当前类进行了实例化，并将实例返回，传给了__init__()，__init__()方法中是self就是__new__()传过来的
# a = A(10)


class B(A):
    def __init__(self, value):
        print "into B __init__"
        self.value = value

    def __new__(cls, *args, **kwargs):
        print "into B __new__"
        return super(B, cls).__new__(cls, *args, **kwargs)
        # return super(B, cls).__new__(A, *args, **kwargs)


# 执行了__new__()，并不一定会进入__init__()，只有__new__()返回了当前类cls的实例，当前类的__init__()才会进入
# b = B(10)


"""
__new__的作用
（1）__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。
（2）实现单例

一些说明
（1）在定义子类时没有重新定义__new__()时，Python默认是调用该类的直接父类的__new__()方法来构造该类的实例，如果该类的父类也没有重写
     __new__()，那么将一直按此规矩追溯至object的__new__()方法，因为object是所有新式类的基类。
（2）除了一项两个作用外，一般__new__()使用较少，能通过__init__()实现的尽量用__init__()实现。
"""


class PositiveInteger(int):
    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))


i = PositiveInteger(-3)
print i


class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))


i = PositiveInteger(-3)
print i
print PositiveInteger.__mro__
