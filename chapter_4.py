#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: chapter_4
@time: 2020/3/27 12:21 AM
@desc:
'''

"""
遍历整个列表
"""

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     # print magician
#     print magician.title() + ", that was a great trick!\n"
#
# print "I can't wait to see your next trick, " + magician.title() + ".\n"


"""
创建数字列表
"""

# for value in range(1, 5):
#     print value

# numbers = list(range(1, 6))
# print numbers
# event_numbers = list(range(1, 12, 2))
# print event_numbers

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print squares
#
# digits = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print min(digits)
# print max(digits)
# print sum(digits)


# squares = [value ** 2 for value in range(1, 11)]
# print squares

"""
切片
"""

# players = ['charles', 'martina', 'micheal', 'florence', 'eli']
# print players[1:-1]
# for player in players[1:-1]:
#     print player

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friends_foods = my_foods[:]
# print my_foods
# print friends_foods
# # friends_foods[0] = 'fish'
# my_foods.append('cannoli')
# friends_foods.append('ice cream')
# print my_foods
# print friends_foods

# my_foods_copy = my_foods
# my_foods_copy[0] = 'chicken'
# print my_foods
# print my_foods_cop


"""
元组
"""

dimensions = (200, 50)
# print dimensions
# print dimensions[0]
# print dimensions[1]

# dimensions[0] = 100
# print dimensions
# print dimensions[0]

for dimension in dimensions:
    print dimension

dimensions = (400, 100)
print dimensions
