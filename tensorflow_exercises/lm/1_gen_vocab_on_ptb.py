#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: gen_vocab
@time: 2021/8/21 4:15 PM
@desc:
'''
import codecs
import collections
from operator import itemgetter

RAW_DATA = "tensorflow/simple-examples/data/ptb.train.txt"
VOCAB_OUTPUT = "tensorflow_exercises/lm/ptb.vocab"

counter = collections.Counter()
with codecs.open(RAW_DATA, "r", "utf-8") as f:
    for line in f:
        for word in line.strip().split():
            counter[word] += 1

sorted_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
sorted_words = [x[0] for x in sorted_word_to_cnt]

sorted_words = ["<eos>"] + sorted_words

with codecs.open(VOCAB_OUTPUT, "w", "utf-8") as file_output:
    for word in sorted_words:
        file_output.write(word + "\n")

