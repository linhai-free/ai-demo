#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin2011@163.com
@software: maimai
@file: test2
@time: 2022/6/6 4:11 PM
@desc:
'''


def simple_multiply(num1, num2):
    if not num1 or not num2:
        return None
    for i in num1:
        if i not in "0123456789":
            return None
    for i in num2:
        if i not in "0123456789":
            return None
    res = ""
    _sum = 0
    m, n = len(num1), len(num2)
    print m, n
    for i in range(m-1, -1, -1):
        n1 = int(num1[i]) * (10 ** (m-i-1))
        for j in range(n-1, -1, -1):
            n2 = int(num2[j]) * (10 ** (n-j-1))
            _sum += n1 * n2
    if _sum == 0:
        return "0"
    while _sum > 0:
        res += str(_sum % 10)
        _sum = _sum / 10
    res = res[::-1]
    return res


print simple_multiply("8888888888", "8888888888")
