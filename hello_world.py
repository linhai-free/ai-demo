#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: hello
@time: 2020/3/26 11:38 PM
@desc:
'''

# print 'Hello, William!'


from memory_profiler import profile


class Person(object):
    '''自定义类型'''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


@profile(precision=10)
def main():
    '''入口函数'''
    p = Person('tom', 18, '男')
    print(p)
    p2 = Person('tom', 18, '男')
    print(p)


if __name__ == "__main__":
    for i in xrange(10):
        main()


