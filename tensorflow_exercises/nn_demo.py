#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: nn_demo
@time: 2021/5/23 10:43 PM
@desc:
'''
import tensorflow as tf
# NumPy 是一个科学计算的工具包，这里通过 NumPy 工具包生成模拟数据集
from numpy.random import RandomState

# 定义训练数据 batch 的大小
batch_size = 8

# 定义神经网路的参数， 这里还是沿用 3.4.2 小节中给出的神经网络结构
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 在 shape 的一个维度上使用 None 可以方便使用不同的 batch 大小。在训练时需要把数据分成比较小的 batch，但是在测试时，可以一次性使用全
# 部的数据。当数据集比较小时这样比较方便测试i，但数据集比较大时，将大量数据放入一个 batch 可能会导致内存溢出。
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

# 定义神经网络前向传播的过程。
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播的算法。
y = tf.sigmoid(y)

cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)) +
    (1 - y_) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0))
)
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 通过随机数生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
# 定义规则来给出样本的标签。在这里所有 x1+x2<1 的样例都被认为是正样本（比如零件合格），而其他为负样本（比如零件不合格）。和 TensorFlow
# 游乐场中的表示法不大一样的地方是，在这里使用 0 来表示负样本，1 来表示正样本。大部分解决分类问题的神经网络都会采用 0 和 1 的表示方法。
Y = [[int(x1 + x2) < 1] for (x1, x2) in X]

# 创建一个会话来运行 TensorFlow 程序
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    # 初始化变量
    sess.run(init_op)

    print sess.run(w1)
    print sess.run(w2)
    '''
    在训练之前神经网络参数的值：
    w1 = [[-0.81131822, 1.48459876, 0.06532937]
            [-2.44270396, 0.0992484, 0.59122431]]
    w2 = [[-0.81131822], [1.48459876], [0.06532937]]
    '''

    # 设定训练的轮数。
    STEPS = 5000
    for i in range(STEPS):
        # 每次选取 batch_size 个样本进行训练
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        # 通过选取的样本训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 1000 == 0:
            # 每隔一段时间计算在所有数据上的交叉熵并输出。
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
            print("After %d training step(s), cross entropy on all data is %g" % (i, total_cross_entropy))
            '''
            输出结果：
            After 0 training step(s), cross entropy on all data is 1.89805
            After 1000 training step(s), cross entropy on all data is 0.655075
            After 2000 training step(s), cross entropy on all data is 0.626172
            After 3000 training step(s), cross entropy on all data is 0.615096
            After 4000 training step(s), cross entropy on all data is 0.610309

            通过这个结果可以发现随着训练的进行，交叉熵是逐渐变小的。交叉熵越小说明预测的结果和真实的结果差距越小。
            '''

    print sess.run(w1)
    print sess.run(w2)
    '''
    在训练之后神经网络参数的值：
    w1 = [[ 0.02476989, 0.5694868, 1.6921941 ]
            [-2.19773507 -0.23668915  1.1143899 ]]
    w2 = [[-0.81131822], [1.48459876], [0.06532937]]
    
    
    '''