#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: main_exercise
@time: 2020/8/12 7:29 PM
@desc:
'''
import sys


# 传入3个参数，具体操作根据个人情况
# 「argv」是「argument variable」参数变量的简写形式，一般在命令行调用的时候由系统传递给程序。
# 这个变量其实是一个List列表，argv[0] 一般是被调用的脚本文件名或全路径，和操作系统有关，argv[1]和以后就是传入的数据了。
def main(argv):
    print argv[0]
    print argv[1]
    print argv[2]
    print argv[3]


if __name__ == '__main__':
    main(sys.argv)

