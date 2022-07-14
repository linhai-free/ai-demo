#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: file_queue_demo
@time: 2021/8/14 3:21 PM
@desc:
'''
import tensorflow as tf


files = tf.train.match_filenames_once('tensorflow/tfrecords/data.tfrecords-*')

filename_queue = tf.train.string_input_producer(files, num_epochs=1, shuffle=False)

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
    serialized_example,
    features={
        'i': tf.FixedLenFeature([], tf.int64),
        'j': tf.FixedLenFeature([], tf.int64),
    }
)

with tf.Session() as sess:
    tf.local_variables_initializer().run()
    print sess.run(files)

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(6):
        print sess.run([features['i'], features['j']])
    coord.request_stop()
    coord.join()
