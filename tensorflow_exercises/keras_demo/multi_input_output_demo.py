#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: multi_input_output_demo
@time: 2021/10/5 11:13 AM
@desc:
'''
import keras
from keras.datasets import mnist
from keras.layers import Input, Dense
from keras.models import Model

num_classes = 10

(trainX, trainY), (testX, testY) = mnist.load_data()
trainX = trainX.reshape(trainX.shape[0], 784)
testX = testX.reshape(testX.shape[0], 784)
trainX = trainX.astype('float32')
testX = testX.astype('float32')
trainX /= 255.0
testX /= 255.0

# one-hot 编码
trainY = keras.utils.to_categorical(trainY, num_classes)
testY = keras.utils.to_categorical(testY, num_classes)

input1 = Input(shape=(784,), name='input1')
input2 = Input(shape=(10,), name='input2')

x = Dense(1, activation='relu')(input1)
output1 = Dense(10, activation='softmax', name='output1')(x)

y = keras.layers.concatenate([x, input2])
output2 = Dense(10, activation='softmax', name='output2')(y)

model = Model(inputs=[input1, input2], outputs=[output1, output2])

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(),
              loss_weights=[1, 1],
              metrics=['accuracy'])
model.fit([trainX, trainY], [trainY, trainY],
          batch_size=128,
          epochs=20,
          validation_data=([testX, testY], [testY, testY]))
