#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: dice
@time: 2020/4/4 4:36 PM
@desc: class_exercises exercise
'''
from random import randint


class Die(object):
    """骰子"""
    slides = 6

    def __init__(self, slides):
        self.slides = slides

    def roll_die(self):
        return randint(1, self.slides)


# die = Die(6)
# print die.slides
die = Die(10)

for i in range(10):
    print str(i) + " : " + str(die.roll_die())




