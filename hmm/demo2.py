#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: demo2
@time: 2021/2/18 11:02 PM
@desc:
'''
import numpy as np
import math
from hmmlearn import hmm

states = ["box 1", "box 2", "box 3"]
n_states = len(states)

observations = ["red", "white"]
n_observations = len(observations)

model2 = hmm.MultinomialHMM(n_components=n_states, n_iter=20, tol=0.01)
X2 = np.array([[0], [1], [0], [1], [0], [0], [0], [1], [1], [0], [1], [1]])
model2.fit(X2, lengths=[4, 4, 4])
print model2.startprob_
print model2.transmat_
print model2.emissionprob_
print model2.score(X2)
print math.pow(math.e, model2.score(X2))

model2.fit(X2)
print model2.startprob_
print model2.transmat_
print model2.emissionprob_
print model2.score(X2)
print math.pow(math.e, model2.score(X2))

model2.fit(X2)
print model2.startprob_
print model2.transmat_
print model2.emissionprob_
print model2.score(X2)
print math.pow(math.e, model2.score(X2))
