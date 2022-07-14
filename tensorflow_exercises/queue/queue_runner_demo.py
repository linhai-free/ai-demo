#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: queuerunner_demo
@time: 2021/8/14 2:38 PM
@desc:
'''
import tensorflow as tf

queue = tf.FIFOQueue(100, "float")
enqueue_op = queue.enqueue([tf.random_normal([1])])

qr = tf.train.QueueRunner(queue, [enqueue_op] * 5)
tf.train.add_queue_runner(qr)

out_tensor = queue.dequeue()


with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for _ in range(3):
        print sess.run(out_tensor)[0]

    coord.request_stop()
    coord.join(threads)
