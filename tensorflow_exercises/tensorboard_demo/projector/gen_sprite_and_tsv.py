#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: gen_sprite_and_tsv
@time: 2021/10/6 9:59 PM
@desc:
'''
from skimage import io
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
from tensorflow.examples.tutorials.mnist import input_data

LOG_DIR = 'tensorflow/tensorboard_demo/projector/log'
SPRITE_FILE = 'mnist_sprite.jpg'
META_FILE = 'mnist_meta.tsv'


def create_sprite_image(images):
    if isinstance(images, list):
        images = np.array(images)
    img_h = images.shape[1]
    img_w = images.shape[2]
    m = int(np.ceil(np.sqrt(images.shape[0])))

    sprite_image = np.ones((img_h * m, img_w * m))

    for i in range(m):
        for j in range(m):
            cur = i * m + j
            if cur < images.shape[0]:
                sprite_image[i * img_h: (i + 1) * img_h, j * img_w: (j + 1) * img_w] = images[cur]

    return sprite_image


mnist = input_data.read_data_sets("tensorflow/MNIST_data", one_hot=False)

to_visualise = 1 - np.reshape(mnist.test.images, (-1, 28, 28))
sprite_image = create_sprite_image(to_visualise)

path_for_mnist_sprites = os.path.join(LOG_DIR, SPRITE_FILE)
plt.imsave(path_for_mnist_sprites, sprite_image, cmap='gray')
plt.imshow(sprite_image, cmap='gray')

path_for_mnist_metadata = os.path.join(LOG_DIR, META_FILE)
with open(path_for_mnist_metadata, 'w') as f:
    f.write('Index\tLabel\n')
    for index, label in enumerate(mnist.test.labels):
        f.write("%d\t%d\n" % (index, label))
