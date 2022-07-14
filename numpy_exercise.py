#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import pandas as pd

# small_counts = np.random.randint(0, 100, 20)
# print small_counts
#
# print np.floor_divide(small_counts, 10)
#
# large_counts = [296, 8286, 64011, 80, 3, 725, 867, 2215, 7689, 11495, 91897, 44, 28, 7971, 926, 122, 22222]
#
# np.floor(np.log10(large_counts))

large_counts = [296, 8286, 64011, 80, 3, 725, 867, 2215, 7689, 11495, 91897, 44, 28, 7971, 926, 122, 22222]
# 将数据映射到所需数量的分位数
print pd.qcut(large_counts, 4, labels=False)
# 计算指定分位数点的数据
large_counts_series = pd.Series(large_counts)
# print large_counts_series
print large_counts_series.quantile([0.25, 0.5, 0.75])