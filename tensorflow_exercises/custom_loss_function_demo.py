#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: custom_loss function_demo
@time: 2021/6/20 7:50 PM
@desc:
'''
import tensorflow as tf
# NumPy 是一个科学计算的工具包，这里通过 NumPy 工具包生成模拟数据集
from numpy.random import RandomState

# 定义训练数据 batch 的大小
batch_size = 8

# 两个输入节点
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
# 回归问题一般只有一个输出节点
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

# 定义一个单层的神经网络前向传播的过程，这里就是简单加权和
w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))

# 定义神经网络前向传播的过程。
y = tf.matmul(x, w1)

# 定义损失函数和反向传播的算法。
loss_less = 10
loss_more = 1
loss = tf.reduce_sum(tf.where(tf.greater(y, y_), (y - y_) * loss_more, (y_ - y) * loss_less))
# loss = tf.reduce_mean(tf.square(y_ - y))  # 均方误差
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 通过随机数生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[x1 + x2 + rdm.rand() / 10.0 - 0.05] for (x1, x2) in X]

# 创建一个会话来运行 TensorFlow 程序
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    # 初始化变量
    sess.run(init_op)
    # 设定训练的轮数。
    STEPS = 5000
    for i in range(STEPS):
        # 每次选取 batch_size 个样本进行训练
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        # 通过选取的样本训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
    print sess.run(w1)
