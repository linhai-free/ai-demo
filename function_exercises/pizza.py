#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: pizza
@time: 2020/4/1 11:26 PM
@desc:
'''


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print "\nMaking a " + str(size) + "-inch pizza with the following toppings:"
    for topping in toppings:
        print "- " + topping