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

RAW_DATA = "tensorflow_exercises/machine_translation/data/train.txt.zh"
VOCAB_OUTPUT = "tensorflow_exercises/machine_translation/data/ted.vocab.zh"
VOCAB_LEN = 4000  # 英文10000，中文4000

counter = collections.Counter()
with codecs.open(RAW_DATA, "r", "utf-8") as f:
    for line in f:
        for word in line.strip().split():
            counter[word] += 1

sorted_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
sorted_words = [x[0] for x in sorted_word_to_cnt]

# sorted_words = ["<eos>"] + sorted_words
sorted_words = ["<unk>", "<sos>", "<eos>"] + sorted_words
if len(sorted_words) > VOCAB_LEN:
    sorted_words = sorted_words[:VOCAB_LEN]

with codecs.open(VOCAB_OUTPUT, "w", "utf-8") as file_output:
    for word in sorted_words:
        file_output.write(word + "\n")


# 英文切词：moses 切词工具
# perl /Users/luodejin/Padre/mosesdecoder/scripts/tokenizer/tokenizer.perl -no-escape -l en < tensorflow/iwlst_ted/zh-en/train.en > tensorflow_exercises/machine_translation/data/train.txt.en

# 中文切词：linux 环境才能执行
# sed 's/ //g; s/\B/ /g' tensorflow/iwlst_ted/en-zh/train.zh > tensorflow_exercises/machine_translation/data/train.txt.zh