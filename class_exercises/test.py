#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: test
@time: 2020/4/3 11:27 AM
@desc:
'''

"""
python2 中，必须总要把一个方法声明为静态的，从而能够不带一个实例而调用它。
python3 中，如果方法只通过类调用，而不需要通过实例调用的话，不用非要声明为静态的。
"""


class Test(object):

    def show(self):
        print ("show")

    def click(self):
        print ("click")


test = Test()
test.show()
