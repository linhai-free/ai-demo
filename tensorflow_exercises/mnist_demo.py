#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: mnist_demo
@time: 2021/8/1 4:10 PM
@desc:
'''
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("/Users/luodejin/Downloads/MNIST_data", one_hot=True)

print "Training data size: ", mnist.train.num_examples
print "Validating data size: ", mnist.validation.num_examples
print "Testing data size: ", mnist.test.num_examples

print "Example training data: ", mnist.train.images[0]
print "Example training data label: ", mnist.train.labels[0]

batch_size = 100
xs, ys = mnist.train.next_batch(batch_size)
print "X shape:", xs.shape
print "Y shape:", ys.shape
