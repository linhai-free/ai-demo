#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: dataset_demo
@time: 2021/8/10 7:46 PM
@desc:
'''
import tensorflow as tf


dataset = tf.data.Dataset.from_tensor_slices([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dataset = dataset.flat_map(lambda x: dataset.from_tensor_slices(x))
# print list(dataset.as_numpy_iterator())

iterator = dataset.make_one_shot_iterator()
one_element = iterator.get_next()

with tf.Session() as sess:
    for i in range(9):
        print(sess.run(one_element))