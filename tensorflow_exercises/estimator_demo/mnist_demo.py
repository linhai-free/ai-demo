#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: mnist_demo
@time: 2021/10/5 12:21 PM
@desc:
'''
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

tf.logging.set_verbosity(tf.logging.INFO)
mnist = input_data.read_data_sets("tensorflow/MNIST_data", one_hot=False)

feature_columns = [tf.feature_column.numeric_column("image", shape=[784])]

estimator = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    hidden_units=[500],
    n_classes=10,
    optimizer=tf.train.AdamOptimizer(),
    model_dir="tensorflow/estimator_model/log"
)

train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"image": mnist.train.images},
    y=mnist.train.labels.astype(np.int32),
    num_epochs=None,
    batch_size=128,
    shuffle=True
)

estimator.train(input_fn=train_input_fn, steps=10000)

test_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"image": mnist.test.images},
    y=mnist.test.labels.astype(np.int32),
    num_epochs=1,
    batch_size=128,
    shuffle=False
)

accuracy_score = estimator.evaluate(input_fn=test_input_fn)["accuracy"]

print "\nTest accuracy: %g %%" % (accuracy_score*100)
