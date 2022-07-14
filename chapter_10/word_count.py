#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: word_count
@time: 2020/4/9 11:50 PM
@desc:
'''


# def count_words(filename):
#     """计算一个文件大致包含多少个单词"""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except IOError:
#         # msg = "Sorry, the file " + filename + " does not exist."
#         # print msg
#         pass
#     else:
#         # 计算文件大致包含多少个单词
#         words = contents.split()
#         num_words = len(words)
#         print "The file " + filename + " has about " + str(num_words) + " words."
#
#
# # filename = 'alice.txt'
# # count_words(filename)
#
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)


line = "Row, row, row your boat"
print line.count('row')
print line.lower().count('row')
