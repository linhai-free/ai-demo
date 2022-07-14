#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: gevent_sleep
@time: 2020/7/21 10:52 AM
@desc: 使用gevent + sleep自动将CPU执行权分配给当前未睡眠的协程
'''
import gevent


def func1():
    gevent.sleep(1)
    print '大梦谁先觉'

    gevent.sleep(13)
    print '1:over'


def func2():
    gevent.sleep(3)
    print '平生我自知'

    gevent.sleep(9)
    print '2:over'


def func3():
    gevent.sleep(5)
    print '草堂春眠足'

    gevent.sleep(5)
    print '3:over'


def func4():
    gevent.sleep(7)
    print '窗外日迟迟'

    gevent.sleep(1)
    print '4:over'


def simple_gevent():
    gr1 = gevent.spawn(func1)
    gr2 = gevent.spawn(func2)
    gr3 = gevent.spawn(func3)
    gr4 = gevent.spawn(func4)
    gevent.joinall([
        gr1, gr2, gr3, gr4
    ])


if __name__ == '__main__':
    simple_gevent()
    print '...finished'


