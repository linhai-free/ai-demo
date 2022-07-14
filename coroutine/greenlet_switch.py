#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: greenlet_switch
@time: 2020/7/21 10:22 AM
@desc: 使用greenlet + switch实现协程调度
'''
import time
from greenlet import greenlet


def func1():
    print "开门走进卫生间"
    time.sleep(3)
    gr2.switch()  # 把CPU执行权交给gr2

    print "飞流直下三千尺"
    time.sleep(3)
    gr2.switch()


def func2():
    print "一看拖把放旁边"
    time.sleep(3)
    gr1.switch()

    print "疑是银河落九天"


if __name__ == '__main__':
    gr1 = greenlet(func1)
    gr2 = greenlet(func2)
    gr1.switch()  # 把CPU执行权交给gr1