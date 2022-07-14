#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: demo
@time: 2021/2/18 8:41 PM
@desc:
'''
import numpy as np
from hmmlearn import hmm

states = ["box 1", "box 2", "box 3"]
n_states = len(states)

observations = ["red", "white"]
n_observations = len(observations)

start_probability = np.array([0.2, 0.4, 0.4])

transition_probability = np.array([
    [0.5, 0.2, 0.3],
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5]
])

emission_probability = np.array([
    [0.5, 0.5],
    [0.4, 0.6],
    [0.7, 0.3]
])

model = hmm.MultinomialHMM(n_components=n_states)
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability


seen = np.array([[0, 1, 0]]).T
logprob, box = model.decode(seen, algorithm="viterbi")
print "The ball picked:" + ", ".join(map(lambda x: observations[x[0]], seen))
print "The hidden box" + ", ".join(map(lambda x: states[x], box))
print model.score(seen)


box2 = model.predict(seen)
print("The ball picked:", ", ".join(map(lambda x: observations[x[0]], seen)))
print("The hidden box", ", ".join(map(lambda x: states[x], box2)))





