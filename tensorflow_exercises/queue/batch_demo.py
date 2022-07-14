#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: batch_demo
@time: 2021/8/14 3:39 PM
@desc:
'''
import tensorflow as tf

# 读取文件样例
files = tf.train.match_filenames_once('tensorflow/tfrecords/data.tfrecords-*')

filename_queue = tf.train.string_input_producer(files, shuffle=False)

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
    serialized_example,
    features={
        'i': tf.FixedLenFeature([], tf.int64),
        'j': tf.FixedLenFeature([], tf.int64),
    }
)

#  组合训练数据
example, label = features['i'], features['j']

batch_size = 3
capacity = 1000 + 3 * batch_size

example_batch, label_batch = tf.train.batch([example, label], batch_size=batch_size, capacity=capacity)

with tf.Session() as sess:
    sess.run(tf.local_variables_initializer(),  tf.global_variables_initializer())
    print sess.run(files)

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(90):
        print sess.run([features['i'], features['j']])

    for i in range(3):
        cur_example_batch, cur_label_batch = sess.run([example_batch, label_batch])
        print cur_example_batch, cur_label_batch

    coord.request_stop()
    coord.join()







