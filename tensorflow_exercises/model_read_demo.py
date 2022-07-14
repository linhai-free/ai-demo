#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: model_read_demo
@time: 2021/8/7 10:36 PM
@desc:
'''
import tensorflow as tf

reader = tf.train.NewCheckpointReader("tensorflow/MNIST_model/model.ckpt-29001")

global_variables = reader.get_variable_to_shape_map()
for variable_name in global_variables:
    print variable_name, global_variables[variable_name]

# print "Value for variable v1 is ", reader.get_tensor("v1")
