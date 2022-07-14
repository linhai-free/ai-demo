#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: remember_me
@time: 2020/4/10 12:13 AM
@desc:
'''
import json

username = raw_input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print "We'll remember you when you come back, " + username + "!"
