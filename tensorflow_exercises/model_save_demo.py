#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: model_save_demo
@time: 2021/8/6 10:16 AM
@desc:
'''
import tensorflow as tf
# from tensorflow.python.framework import graph_util
# from tensorflow.python.platform import gfile

v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
result = v1 + v2
# v = tf.Variable(0, dtype=tf.float32, name="v")

# ema = tf.train.ExponentialMovingAverage(0.99)
# maintain_average_op = ema.apply(tf.global_variables())
# print ema.variables_to_restore()

# for variables in tf.global_variables():
#     print variables.name

saver = tf.train.Saver()
# saver = tf.train.import_meta_graph("/Users/luodejin/PycharmProjects/demo-pure/tensorflow/model/model_v1/model.ckpt.meta")
# saver = tf.train.Saver({"v/ExponentialMovingAverage": v})
# saver = tf.train.Saver(ema.variables_to_restore())
saver.export_meta_graph("/Users/luodejin/PycharmProjects/demo-pure/tensorflow/model/model_v1/model.ckpt.meta.json", as_text=True)

# init_op = tf.global_variables_initializer()
# with tf.Session() as sess:
    # sess.run(init_op)

    # sess.run(tf.assign(v, 10))
    # sess.run(maintain_average_op)
    # saver.save(sess, "/Users/luodejin/Downloads/tensorflow/model/model_v2/model.ckpt")
    # saver.restore(sess,  "/Users/luodejin/Downloads/tensorflow/model/model_v2/model.ckpt")
    # print sess.run(result)
    # print sess.run(tf.get_default_graph().get_tensor_by_name("add:0"))
    # print sess.run([v, ema.average(v)])
    # print sess.run(v)

    # graph_def = tf.get_default_graph().as_graph_def()
    # output_graph_def = graph_util.convert_variables_to_constants(sess, graph_def, ['add'])
    # with tf.gfile.GFile("/Users/luodejin/Downloads/tensorflow/model/model_v3/combined_model.pb", "wb") as f:
    #     f.write(output_graph_def.SerializeToString())
    # model_filename = "/Users/luodejin/Downloads/tensorflow/model/model_v3/combined_model.pb"
    # with gfile.FastGFile(model_filename, 'rb') as f:
    #     graph_def = tf.GraphDef()
    #     graph_def.ParseFromString(f.read())
    #
    # result = tf.import_graph_def(graph_def, return_elements=["add:0"])
    # print sess.run(result)
