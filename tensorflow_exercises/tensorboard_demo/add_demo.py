#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: add_demo
@time: 2021/10/5 5:25 PM
@desc:
'''
import tensorflow as tf

with tf.name_scope("input1"):
    input1 = tf.constant([1.0, 2.0, 3.0], name="input1")

with tf.name_scope("input2"):
    input2 = tf.Variable(tf.random_uniform([3]), name="input2")

output = tf.add_n([input1, input2], name="add")

writer = tf.summary.FileWriter("tensorflow/tensorboard_demo/log", tf.get_default_graph())
writer.close()

#  tensorboard --logdir=tensorflow/tensorboard_demo/log
