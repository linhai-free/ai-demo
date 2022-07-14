#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin2011@163.com
@software: maimai
@file: test
@time: 2022/5/20 10:47 AM
@desc:
'''


def find_index(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print find_index(nums=[-1,0,3,5,9,12], target=9)

