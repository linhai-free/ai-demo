#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin2011@163.com
@software: maimai
@file: test3
@time: 2022/6/9 5:01 PM
@desc:
'''
import tensorflow as tf


# def findMaxGap(nums):
#     if len(nums) < 2:
#         return 0
#     max_gap = 0
#     left_min_val = 0
#     for i in range(1, len(nums)):
#         max_gap = max(max_gap, nums[i] - nums[left_min_val])
#         if nums[i] < nums[left_min_val]:
#             left_min_val = i
#     return max_gap
#
#
# nums = [12, 23, 20, 10, 1, 2, 7, 5]
# print findMaxGap(nums)


# number = tf.feature_column.numeric_column("number")
# feature_dict = {"number": [1.1, 1.2, 1.3]}
# feature_layer = tf.keras.layers.DenseFeatures(number)
# output = feature_layer(feature_dict)
# print(output)
# print("=========================")


number = tf.feature_column.categorical_column_with_hash_bucket("number", 10)
number = tf.feature_column.embedding_column(number, 3)
feature_dict = {"number": tf.compat.v1.string_split(["搜索|算法"], sep="|")}
feature_layer = tf.keras.layers.DenseFeatures(number)
output = feature_layer(feature_dict)
print(output)
print("=========================")
