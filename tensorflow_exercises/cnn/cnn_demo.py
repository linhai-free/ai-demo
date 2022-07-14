#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: cnn_demo
@time: 2021/8/8 2:47 PM
@desc:
'''
import tensorflow as tf

filter_weight = tf.get_variable('weights', [5, 5, 3, 16], initializer=tf.truncated_normal_initializer(stddev=0.1))
biases = tf.get_variable('biases', [16], initializer=tf.truncated_normal_initializer(stddev=0.1))

conv = tf.nn.conv2d(input, filter_weight, strides=[1, 1, 1, 1], padding='SAME')
bias = tf.nn.bias_add(conv, biases)
actived_conv = tf.nn.relu(bias)
pool = tf.nn.max_pool(actived_conv, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding='SAME')