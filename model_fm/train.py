#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin2011@163.com
@software: maimai
@file: train
@time: 2022/5/20 2:35 PM
@desc:
'''
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import OneHotEncoder
from collections import Counter

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 对每一个样本计算损失
def logit(y, y_hat):
    return np.log(1 + np.exp(-y * y_hat))


def df_logit(y, y_hat):
    return sigmoid(-y * y_hat) * (-y)


class FactorizationMachine(BaseEstimator):
    def __init__(self, k=5, learning_rate=0.01, iternum=100):
        self.w0 = None
        self.W = None
        self.V = None
        self.k = k
        self.alpha = learning_rate
        self.iternum = iternum

    def _FM(self, Xi):
        interaction = np.sum((Xi.dot(self.V)) ** 2 - (Xi ** 2).dot(self.V ** 2))
        y_hat = self.w0 + Xi.dot(self.W) + interaction / 2
        return y_hat[0]

    def _FM_SGD(self, X, y):
        m, n = np.shape(X)
        # 初始化参数
        self.w0 = 0
        self.W = np.random.uniform(size=(n, 1))
        self.V = np.random.uniform(size=(n, self.k))  # #Vj是第j个特征的隐向量  Vjf是第j个特征的隐向量表示中的第f维

        for it in range(self.iternum):
            total_loss = 0

            for i in range(m):  # 遍历训练集
                y_hat = self._FM(Xi=X[i])  # #X[i]是第i个样本  X[i,j]是第i个样本的第j个特征

                total_loss += logit(y=y[i], y_hat=y_hat)  # 计算logit损失函数值
                dloss = df_logit(y=y[i], y_hat=y_hat)  # 计算logit损失函数的外层偏导

                dloss_w0 = dloss * 1   # 公式中的w0求导，计算复杂度O(1)
                self.w0 = self.w0 - self.alpha * dloss_w0

                for j in range(n):
                    if X[i, j] != 0:
                        dloss_Wj = dloss * X[i, j]  # 公式中的wi求导，计算复杂度O(n)
                        self.W[j] = self.W[j] - self.alpha * dloss_Wj

                        for f in range(self.k):  # 公式中的vif求导，计算复杂度O(kn)
                            dloss_Vjf = dloss * (X[i, j] * (X[i].dot(self.V[:, f])) - self.V[j, f] * X[i, j] ** 2)
                            self.V[j, f] = self.V[j, f] - self.alpha * dloss_Vjf

            if it % 20 == 0:
                print("iter={}, loss={:.4f}".format(it, total_loss / m))

        return self

    def _FM_predict(self, X):
        predicts, threshold = [], 0.5  # sigmoid阈值设置
        for i in range(X.shape[0]):  # 遍历测试集
            y_hat = self._FM(Xi=X[i])  # FM的模型方程
            predicts.append(-1 if sigmoid(y_hat) < threshold else 1)
        return np.array(predicts)

    def fit(self, X, y):
        if isinstance(X, pd.DataFrame):
            X = np.array(X)
            y = np.array(y)
        return self._FM_SGD(X, y)

    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            X = np.array(X)
        return self._FM_predict(X)

    def predict_proba(self, X):
        pass


"""
Data
"""
print "Data********************"

path = '/Users/luodejin/Downloads/ml-1m/'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_csv(path + 'users.dat', sep='::', header=None, names=unames, engine='python')
print users.head()
print users.shape


rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(path + 'ratings.dat', sep='::', header=None, names=rnames, engine='python')
print ratings.head()
print ratings.shape

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_csv(path + 'movies.dat', sep='::', header=None, names=mnames, engine='python')
print movies.head()
print movies.shape

# 合并数据
df = pd.merge(pd.merge(ratings, users, on='user_id'), movies, on='movie_id')
print df.head()
print df.shape
print df['rating'].value_counts()

# 构造2分类数据集
df = df[df['rating'] != 3]
print df['rating'].value_counts()
print df.shape

# 数据量比较大，单纯为了验证FM的效果，这里挑选有20～35次打分的movie_id
movie_group = df.groupby('movie_id').size()
print movie_group.head()
movie_group = pd.Series(movie_group).where(lambda x: x < 35).dropna()
movie_list = pd.Series(movie_group).where(lambda x: x > 20).dropna().index.values
print len(movie_list)

df = df[df['movie_id'].isin(movie_list)]
print df.head()
print df.shape

# 这里挑选有>20次打分行为的user_id
user_group = df.groupby('user_id').size()
print user_group.head()
user_list = pd.Series(user_group).where(lambda x: x > 20).dropna().index.values
print len(user_list)

df = df[df['user_id'].isin(user_list)]
print df.head()
print df.shape

print df['user_id'].nunique(), df['movie_id'].nunique()  # 一共37个人，评分的总电影数是317部
print df.head()

print df['rating'].value_counts()
df['rating'] = df['rating'].map(lambda x: -1 if x > 3 else 1)  # 1,2是label=1  4,5是label=0


"""
Processing
"""
print "Processing********************"

print df[['age']].describe([0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]).T  # age是被分段后的，没有异常值


# - Age is chosen from the following ranges:

# 	*  1:  "Under 18"
# 	* 18:  "18-24"
# 	* 25:  "25-34"
# 	* 35:  "35-44"
# 	* 45:  "45-49"
# 	* 50:  "50-55"
# 	* 56:  "56+"

# 时间处理
# df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
# df['date'] = df['timestamp'].apply(lambda x: x.strftime('%Y%m%d'))

print df.info()

# one-hot encoder
columns = ['user_id', 'movie_id']
for i in columns:
    get_dummy_feature = pd.get_dummies(df[i])
    df = pd.concat([df, get_dummy_feature], axis=1)
    df = df.drop(i, axis=1)

print df.head()
print df.shape  # 8 + 37 +317

# label encoder
# from sklearn.preprocessing import LabelEncoder
# columns = ['gender', 'zip', 'genres']
# for i in columns:
#     le = LabelEncoder(df[i])
#     df[i] = le.fit_transform(df[i])
#
# df.head()

df = df.drop(['timestamp','gender','age','occupation','zip','title','genres'], axis=1)
#这些特征可以进一步挖掘。这里都不要了，只保留one-hot特征

from sklearn.model_selection import train_test_split
X = df.drop('rating', axis=1)
Y = df['rating']

X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.3, random_state=123)
X_train.shape, X_val.shape

Y.value_counts()



