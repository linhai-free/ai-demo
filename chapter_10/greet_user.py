#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: greet_user
@time: 2020/4/10 12:15 AM
@desc: 重构
'''
import json

FILENAME = 'username.json'


def get_stored_username():
    """如何存储了用户名，就获取它"""
    try:
        with open(FILENAME) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = raw_input("What is your name? ")
    with open(FILENAME, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print "Wellcome back, " + username + "!"
    else:
        username = get_new_username()
        print "We'll remember you when you come back, " + username + "!"


greet_user()


