#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: gen_train
@time: 2021/8/21 4:27 PM
@desc:
'''
import codecs
import sys

RAW_DATA = "tensorflow_exercises/machine_translation/data/train.txt.zh"
VOCAB_OUTPUT = "tensorflow_exercises/machine_translation/data/ted.vocab.zh"
OUTPUT_DATA = "tensorflow_exercises/machine_translation/data/ted.valid.zh"


with codecs.open(VOCAB_OUTPUT, "r", "utf-8") as f_vocab:
    vocab = [w.strip() for w in f_vocab.readlines()]
word_to_id = {k: v for (k, v) in zip(vocab, range(len(vocab)))}


def get_id(word):
    return word_to_id[word] if word in word_to_id else word_to_id["<unk>"]


fin = codecs.open(RAW_DATA, "r", "utf-8")
fout = codecs.open(OUTPUT_DATA, "w", "utf-8")
for line in fin:
    words = line.strip().split() + ["<eos>"]
    out_line = " ".join([str(get_id(w)) for w in words]) + "\n"
    fout.write(out_line)
fin.close()
fout.close()
