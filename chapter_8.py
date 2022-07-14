#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: function_exercises
@time: 2020/3/28 11:23 PM
@desc:
'''

"""
函数
"""

import json


# def greet_user(username):
#     """显示简单的问候语"""
#     print "Hello, " + username.title() + "!"


# greet_user('jesse')


# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print "\nI have a " + animal_type + "."
#     print "My " + animal_type + "'s name is " + pet_name.title() + "."


# # describe_pet('hamster', 'harry')
# # describe_pet('dog', 'willie')
# # describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='willie')

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print musician


# def build_person(first_name, last_name):
#     """返回一个字典信息，其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     print person
#     print type(person)
#     return json.dumps(person)
#
#
# musician = build_person('jimi', 'hendrix')
# print musician
# print type(musician)

# while True:
#     print '\nPlease tell me your name:'
#     print "enter 'q' at any time to quit"
#
#     f_name = raw_input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = raw_input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print '\nHello, ' + formatted_name + '!'


"""
传递列表
"""


# def greet_users(names):
#     """向列表中的每位用户都发出"""
#     for name in names:
#         msg = "Hello, " + name.title() + '!'
#         print msg
#
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         print "Printing model: " + current_design
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     print "\nThe following models have been printed:"
#     for completed_model in completed_models:
#         print completed_model
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print unprinted_designs


# def make_pizza(size,  *toppings):
#     """概述要制作的比萨"""
#     print "\nMaking a " + str(size) + "-inch pizza with the following toppings:"
#     for topping in toppings:
#         print "- " + topping
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print user_profile









