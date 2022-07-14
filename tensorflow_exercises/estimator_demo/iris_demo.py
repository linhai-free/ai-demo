#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: iris_demo
@time: 2021/10/5 4:44 PM
@desc:
'''
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)


def my_input_fn(file_path, perform_shuffle=False, repeat_count=1):
    def decode_csv(line):
        parsed_line = tf.decode_csv(line, [[0.], [0.], [0.], [0.], [0]])
        return {"x": parsed_line[:-1]}, parsed_line[-1:]

    dataset = (tf.data.TextLineDataset(file_path).skip(1).map(decode_csv))
    if perform_shuffle:
        dataset = dataset.shuffle(buffer_size=256)
    dataset = dataset.repeat(repeat_count)
    dataset = dataset.batch(32)
    iterator = dataset.make_one_shot_iterator()
    batch_features, batch_labels = iterator.get_next()
    return batch_features, batch_labels


feature_columns = [tf.feature_column.numeric_column("x", shape=[4])]
classifier = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    hidden_units=[10, 10],
    n_classes=3
)

classifier.train(input_fn=lambda: my_input_fn("tensorflow/iris_data/iris_training.csv", True, 100))

test_results = classifier.evaluate(input_fn=lambda: my_input_fn("tensorflow/iris_data/iris_test.csv", False, 1))
print "\nTest accuracy: %g %%" % (test_results["accuracy"]*100)

