#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: demo
@time: 2021/1/21 9:23 PM
@desc:
'''
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a + b
with tf.Session() as sess:
    print(sess.run(result))




