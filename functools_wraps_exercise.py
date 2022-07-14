#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: functools_wraps_exercise
@time: 2020/4/28 9:01 PM
@desc:
'''
from functools import wraps


def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print '%s(%s,%s) -> %s' % (func.__name__,args, kwargs, result)
        return result
    return wrapper


@tracer
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(3)
print fibonacci
print 'help'
# help(fibonacci)