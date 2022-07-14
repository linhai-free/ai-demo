#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: chapter_7
@time: 2020/3/28 12:32 AM
@desc:
'''

"""
函数input()的工作原理
"""

# message = input('Tell me something, and I will repeat it back to you: ')
# print message

# name = input("Please enter your name: ")
# print "Hello， " + name + "!"

# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += '\nWhat is your name? '
#
# name = input(prompt)
# print '\nHello, ' + name + '!'

# age = input('How old are you? ')
# print age
# print type(age)
# int(age)
# print type(age)

# print 4 % 3


"""
while 循环简介
"""

# current_number = 1
# while current_number <= 5:
#     print current_number
#     current_number += 1


prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program. '

# message = ''
# while message != 'quit':
#     message = input(prompt)
#     print message

# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print message

# while True:
#     message = input(prompt)
#
#     if message == 'quit':
#         break
#     else:
#         print message


# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print current_number

# x = 1
# while x <= 5:
#     print x


"""
使用while 循环来处理列表和字典
"""

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print "Verifying user: " + current_user.title()
#     confirmed_users.append(current_user)
#
# print "\nThe following users have been confirmed:"
# for confirmed_user in confirmed_users:
#     print confirmed_user.title()
# print unconfirmed_users
# print confirmed_users


# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print pets
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print pets

responses = {}
polling_active = True
while polling_active:
    name = raw_input('\nWhat is your name? ')
    response = raw_input('Which mountain would you like to climb someday? ')

    responses[name] = response
    repeat = raw_input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        polling_active = False


print '\n--- Poll Results ---'
for name, response in responses.items():
    print name + " would like to climb " + response + "."
