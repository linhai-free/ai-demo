#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: dataset_handle
@time: 2021/8/11 10:05 AM
@desc:
'''
import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile


INPUT_DATA = 'tensorflow/flower_photos'
OUTPUT_FILE = 'tensorflow/flower_photos/flower_processed_data.npy'

VALIDATION_PERCENTAGE = 10
TEST_PERCENTAGE = 10


def create_image_lists(sess, testing_percentage, validation_percentage):
    sub_dirs = [x[0] for x in os.walk(INPUT_DATA)]
    is_root_dir = True

    print 'sub_dirs:', sub_dirs

    training_images = []
    training_labels = []
    testing_images = []
    testing_labels = []
    validation_images = []
    validation_labels = []
    current_label = 0

    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
        file_list = []
        dir_name = os.path.basename(sub_dir)
        for extension in extensions:
            file_glob = os.path.join(INPUT_DATA, dir_name, '*.' + extension)
            file_list.extend(glob.glob(file_glob))
        if not file_list:
            continue

        for file_name in file_list:
            print 'sub_dir: %s, file_name:%s' % (sub_dir, file_name)

            image_raw_data = gfile.FastGFile(file_name, 'rb').read()
            image = tf.image.decode_jpeg(image_raw_data)
            if image.dtype != tf.float32:
                print 'sub_dir: %s, file_name:%s, convert_image_dtype' % (sub_dir, file_name)
                image = tf.image.convert_image_dtype(image, dtype=tf.float32)
            image = tf.image.resize_images(image, [299, 299])
            image_value = sess.run(image)

            chance = np.random.randint(100)
            if chance < validation_percentage:
                print 'sub_dir: %s, file_name:%s, chance:%d, validation_image_add' % (sub_dir, file_name, chance)
                validation_images.append(image_value)
                validation_labels.append(current_label)
            elif chance < (testing_percentage + validation_percentage):
                print 'sub_dir: %s, file_name:%s, chance:%d, testing_image_add' % (sub_dir, file_name, chance)
                testing_images.append(image_value)
                testing_labels.append(current_label)
            else:
                print 'sub_dir: %s, file_name:%s, chance:%d, training_image_add' % (sub_dir, file_name, chance)
                training_images.append(image_value)
                training_labels.append(current_label)
        current_label += 1

    print 'training_image_cnt: %d, validation_image_cnt: %d, testing_image_cnt: %d' % (
        len(training_images), len(validation_images), len(testing_images))
    state = np.random.get_state()
    np.random.shuffle(training_images)
    np.random.set_state(state)
    np.random.shuffle(training_labels)

    return np.asarray([training_images, training_labels,
                       validation_images, validation_labels,
                       testing_images, testing_labels])


def main():
    with tf.Session() as sess:
        processed_data = create_image_lists(sess, TEST_PERCENTAGE, VALIDATION_PERCENTAGE)
        np.save(OUTPUT_FILE, processed_data)


if __name__ == '__main__':
    main()
