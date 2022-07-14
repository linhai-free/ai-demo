#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: names
@time: 2020/4/12 9:36 PM
@desc:
'''
from name_function import get_formatted_name


print "Enter 'q' at any time to quit."
while True:
    first = raw_input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = raw_input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print "\tNeatly formatted name: " + formatted_name + '.'
