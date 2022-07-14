#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: lstm_demo
@time: 2021/8/14 10:10 PM
@desc:
'''
import tensorflow as tf

lstm = tf.nn.rnn_cell.BasicLSTMCell(lstm_hidden_size)
state = lstm.zero_state(batch_size, tf.float32)

loss = 0.0
for i in range(num_steps):
    if i > 0:
        tf.get_variable_scope().reuse_variables()

    lstm_output, state = lstm(current_input, state)
    final_output = fully_connected(lstm_output)
    loss += calc_loss(final_output, expected_output)