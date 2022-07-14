#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: super
@time: 2020/4/3 2:39 PM
@desc:
'''

"""
super()
1、当我们调用 super() 的时候，实际上是实例化了一个 super 类。
2、super 包含了两个非常重要的信息: 一个 MRO 以及 MRO 中的一个类。
   2.1 super(a_type, obj)： MRO 指的是 type(obj) 的 MRO, MRO 中的那个类就是a_type，isinstance(obj, a_type) == True
   2.2 super(type1, type2)：MRO 指的是 type2 的 MRO, MRO 中的那个类就是 type1，issubclass(type2, type1) == True
3、super() 提供一个 MRO 以及一个 MRO 中的类 C ， super() 将返回一个从 MRO 中 C 之后的类中查找方法的对象。查找方式时不是像常规方法一样从所有的 MRO 类中查找，而是从 MRO 的 tail 中查找。
"""


class A(object):
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super(B, self).add(m)
        self.n += 3


# b = B()
# b.add(2)
# print(b.n)


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super(C, self).add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super(C, self).add(m)
        self.n += 5


d = D()
d.add(2)
print(d.n)
print(D.__mro__)  # 查看 D 的 MRO 信息
