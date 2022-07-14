#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: migrate_learning
@time: 2021/8/12 9:57 AM
@desc:
'''
import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile
import tensorflow.contrib.slim as slim

import tensorflow.contrib.slim.python.slim.nets.inception_v3 as inception_v3

INPUT_DATA = 'tensorflow/flower_photos/flower_processed_data.npy'
TRAIN_FILE = 'tensorflow/Inception-v3_model2'
CKPT_FILE = 'tensorflow/Inception-v3_model/inception_v3.ckpt'

LEARNING_RATE = 0.0001
STEPS = 300
BATCH = 32
N_CLASSES = 5

CHECKPOINT_EXCLUDE_SCOPES = 'InceptionV3/Logits,InceptionV3/AuxLogits'
TRAINABLE_SCOPES = 'InceptionV3/Logits,InceptionV3/AuxLogits'


def get_tuned_variables():
    exclusions = [scope.strip() for scope in CHECKPOINT_EXCLUDE_SCOPES.split(',')]

    variables_to_restore = []
    for var in slim.get_model_variables():
        excluded = False
        for exclusion in exclusions:
            if var.op.name.startswith(exclusion):
                excluded = True
                break
        if not excluded:
            variables_to_restore.append(var)
    return variables_to_restore


def get_trainable_variables():
    scopes = [scope.strip() for scope in TRAINABLE_SCOPES.split(',')]

    variables_to_train = []
    for scope in scopes:
        variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope)
        variables_to_train.extend(variables)
    return variables_to_train


def main(argv=None):
    processed_data = np.load(INPUT_DATA)
    training_images = processed_data[0]
    n_training_example = len(training_images)
    training_labels = processed_data[1]
    validation_images = processed_data[2]
    validation_labels = processed_data[3]
    testing_images = processed_data[4]
    testing_labels = processed_data[5]
    print '%d training examples, %d validation examples and %d testing examples.' % (
        n_training_example, len(validation_images), len(testing_images))

    images = tf.placeholder(tf.float32, [None, 299, 299, 3], name='input_images')
    labels = tf.placeholder(tf.int64, [None], name='labels')

    with slim.arg_scope(inception_v3.inception_v3_arg_scope()):
        logits, _ = inception_v3.inception_v3(images, num_classes=N_CLASSES)
    trainable_variables = get_trainable_variables()
    tf.losses.softmax_cross_entropy(tf.one_hot(labels, N_CLASSES), logits, weights=1.0)
    train_step = tf.train.RMSPropOptimizer(LEARNING_RATE).minimize(tf.losses.get_total_loss())

    with tf.name_scope('evaluation'):
        correct_prediction = tf.equal(tf.argmax(logits, 1), labels)
        evaluation_step = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    tuned_variables = get_tuned_variables()
    print 'tuned_variables:', tuned_variables
    load_fn = slim.assign_from_checkpoint_fn(CKPT_FILE, tuned_variables, ignore_missing_vars=True)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        print 'Loading tuned variables from %s' % CKPT_FILE
        load_fn(sess)

        start = 0
        end = BATCH
        for i in range(STEPS):
            sess.run(train_step, feed_dict={
                images: training_images[start:end],
                labels: training_labels[start:end]})

            if i % 30 == 0 or i + 1 == STEPS:
                saver.save(sess, TRAIN_FILE, global_step=i)
                validation_accuracy = sess.run(evaluation_step, feed_dict={
                    images: validation_images, labels: validation_labels})
                print 'Step %d: Validation accuracy = %.1f%%' % (i, validation_accuracy * 100.0)

            start = end
            if start == n_training_example:
                start = 0

            end = start + BATCH
            if end > n_training_example:
                end = n_training_example

        test_accuracy = sess.run(evaluation_step, feed_dict={images: testing_images, labels: testing_labels})
        print 'Final test accuracy = %.1f%%' % (test_accuracy * 100)


if __name__ == '__main__':
    tf.app.run()
