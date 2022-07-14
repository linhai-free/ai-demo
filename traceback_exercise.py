#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: traceback_exercise
@time: 2020/8/5 3:12 PM
@desc:
'''
import sys
import traceback
import logging

logging.basicConfig()
logger = logging.getLogger('traceback_test')


def func1():
    raise NameError("--func1 exception--")


def func2():
    func1()


def main():
    try:
        func2()
    except Exception as e:
        # print e
        # exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        # print "exc_type: %s" % exc_type
        # print "exc_value: %s" % exc_value
        # print "exc_traceback_obj: %s" % exc_traceback_obj
        # traceback.print_tb(exc_traceback_obj)
        # traceback.print_exception(exc_type, exc_value, exc_traceback_obj, limit=3, file=sys.stdout)
        # traceback.print_exc(limit=1, file=sys.stdout)
        logger.error(traceback.format_exc())


if __name__ == '__main__':
    main()
