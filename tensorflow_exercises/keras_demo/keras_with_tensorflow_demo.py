#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: keras_with_tensorflow_demo
@time: 2021/10/5 11:37 AM
@desc:
'''
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist_data = input_data.read_data_sets("tensorflow/MNIST_data", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784], name='x-input')
y_ = tf.placeholder(tf.float32, [None, 10], name='y-input')

net = tf.keras.layers.Dense(500, activation='relu')(x)
y = tf.keras.layers.Dense(10, activation='softmax')(net)

loss = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_, y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

acc_value = tf.reduce_mean(tf.keras.metrics.categorical_accuracy(y_, y))

with tf.Session() as sess:
    tf.global_variables_initializer().run()

    for i in range(10000):
        xs, ys = mnist_data.train.next_batch(100)
        _, loss_value = sess.run([train_step, loss], feed_dict={x: xs, y_: ys})

        if i % 1000 == 0:
            print "After %d training step(s), loss on training batch is %g." % (i, loss_value)

    print acc_value.eval(feed_dict={x: mnist_data.test.images, y_: mnist_data.test.labels})
