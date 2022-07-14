#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: chapter_10
@time: 2020/4/9 11:03 PM
@desc:
'''

"""
异常
"""

# try:
#     print 5/0
# except ZeroDivisionError:
#     print "You can't divide by zero!"

print "Give me two numbers, and I'll divide them."
print "Enter 'q' to quit."

while True:
    first_number = raw_input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = raw_input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except (ZeroDivisionError, ValueError) as reason:
        print "%s" % str(reason)
    else:
        print answer
