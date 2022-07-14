#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: dataset_demo
@time: 2021/8/14 5:50 PM
@desc:
'''
import tensorflow as tf

input_data = [1, 2, 3, 5, 8]

dataset = tf.data.Dataset.from_tensor_slices(input_data)

iterator = dataset.make_one_shot_iterator()
x = iterator.get_next()
y = x * x

with tf.Session() as sess:
    for i in range(len(input_data)):
        print sess.run(y)
