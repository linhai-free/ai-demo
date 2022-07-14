#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: coordinator_demo
@time: 2021/8/14 2:30 PM
@desc:
'''
import tensorflow as tf
import numpy as np
import threading
import time


def MyLoop(coord, worker_id):
    while not coord.should_stop():
        if np.random.rand() < 0.1:
            print 'Stoping from id: %d\n' % worker_id
            coord.request_stop()
        else:
            print 'Working on id: %d\n' % worker_id
        time.sleep(1)


coord = tf.train.Coordinator()
threads = [threading.Thread(target=MyLoop, args=(coord, i)) for i in range(5)]
for t in threads:
    t.start()
coord.join(threads)
