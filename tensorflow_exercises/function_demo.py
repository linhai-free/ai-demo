#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: function_demo
@time: 2021/6/10 5:20 PM
@desc:
'''
import tensorflow as tf

# v = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
# v = tf.constant([1.0, 2.0, 3.0])
# v1 = tf.constant([[1.0, 2.0], [3.0, 4.0]])
# v2 = tf.constant([[5.0, 6.0], [7.0, 8.0]])
v1 = tf.constant([1.0, 2.0, 3.0, 4.0])
v2 = tf.constant([4.0, 3.0, 2.0, 1.0])

with tf.Session() as sess:
    # print tf.clip_by_value(v, 2.5, 4.5).eval()
    # print tf.log(v).eval()
    # print (v1 * v2).eval()
    # print tf.matmul(v1, v2).eval()
    # print tf.reduce_mean(v).eval()
    print tf.greater(v1, v2).eval()
    print tf.where(tf.greater(v1, v2), v1, v2).eval()
