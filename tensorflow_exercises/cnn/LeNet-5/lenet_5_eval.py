#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: mnist_eval
@time: 2021/8/7 10:44 PM
@desc:
'''
import numpy as np
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import lenet_5_inference
import lenet_5_train


EVAL_INTERVAL_SECS = 10


def evaluate(mnist):
    with tf.Graph().as_default() as g:
        size = len(mnist.validation.images)
        print 'size:', size

        x = tf.placeholder(tf.float32, [
            size,
            lenet_5_inference.IMAGE_SIZE,
            lenet_5_inference.IMAGE_SIZE,
            lenet_5_inference.NUM_CHANNELS],
                           name='x-input')
        y_ = tf.placeholder(tf.float32, [
            size,
            lenet_5_inference.OUTPUT_NODE],
                            name='y-input')

        validate_feed = {
            x: np.reshape(mnist.validation.images, [
                size,
                lenet_5_inference.IMAGE_SIZE,
                lenet_5_inference.IMAGE_SIZE,
                lenet_5_inference.NUM_CHANNELS]),
            y_: mnist.validation.labels
        }

        y = lenet_5_inference.inference(x, False, None)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.arg_max(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        variable_averages = tf.train.ExponentialMovingAverage(lenet_5_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(lenet_5_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    # print ckpt.model_checkpoint_path
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    # print 'global_step =', global_step
                    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                    print "After %s training step(s), validation accuracy = %g " % (global_step, accuracy_score)
                else:
                    print 'No checkpoint file found'
            time.sleep(EVAL_INTERVAL_SECS)


def main(argv=None):
    mnist = input_data.read_data_sets("tensorflow/MNIST_data", one_hot=True)
    evaluate(mnist)


if __name__ == '__main__':
    tf.app.run()
