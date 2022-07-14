#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: write_message
@time: 2020/4/6 9:50 PM
@desc: file write. mode: 'r'-read, 'w'-write, 'a'-append, 'r+'-read and write, default 'r'
'''


filename = 'programming.txt'
lines = None
with open(filename, 'r+') as file_object:
    file_object.write("I love Python.")
    lines = file_object.readlines()

for line in lines:
    print line



