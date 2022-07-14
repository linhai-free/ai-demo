#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: variable_manage_demo
@time: 2021/8/5 9:01 AM
@desc:
'''
import tensorflow as tf


# v = tf.get_variable("v", shape=[1], initializer=tf.constant_initializer(1.0))
# v1 = tf.get_variable("v", [1])
# print v1.name
#
# with tf.variable_scope("foo"):
#     v2 = tf.get_variable("v", [1])
#     print v2.name
#
# with tf.variable_scope("foo"):
#     with tf.variable_scope("bar"):
#         v3 = tf.get_variable("v", [1])
#         print v3.name
#
#     v4 = tf.get_variable("v1", [1])
#     print v4.name

with tf.name_scope("a"):
    # 受 tf.name_scope 影响
    a = tf.Variable([1])
    print a.name
    b = tf.Variable([1])
    print b.name
    c = tf.Variable([1])
    print c.name

    # 不受 tf.name_scope 影响
    a = tf.get_variable("b", [1])
    print a.name


with tf.name_scope("b"):
    tf.get_variable("b", [1])
