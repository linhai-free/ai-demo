#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: file_reader
@time: 2020/4/6 6:54 PM
@desc:
'''

"""
文件和异常
"""


# filename = r'/Users/luodejin/PycharmProjects/demo-pure/files_exercises/text_files/pi_digits'  # 绝对路径
# filename = r'text_files/pi_digits'  # 相对路径
# filename = r'pi_digits'  # 相对路径
filename = r'/Users/luodejin/PycharmProjects/demo-pure/.git/index.lock'  # 相对路径
lines = None
with open(filename) as file_object:
    lines = file_object.readlines()
    # contents = file_object.read().rstrip()
    # print contents
    for line in lines:
        print line.rstrip()


# file_object = open('pi_digits')
# contents = file_object.read()
# print contents
# file_object.close()

# pi_string = ''
# license_ids = []
# for line in lines:
#     if line:
#         license_ids.append(int(line[1:-2].strip()))
    # pi_string += line.strip()

# print pi_string[:52] + "..."
# print len(pi_string)

# print ','.join(map(lambda license_id: str(license_id), license_ids[32:]))
# print len(license_ids)

"""
圆周率中包含你的生日吗
"""

# birthday = raw_input("Enter you birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print "Your birthday appears in the first million digits of pi!"
# else:
#     print "Your birthday does not appear in the first million digits of pi."


"""
replace()方法
    S.replace(old, new[, count]) -> string
        
    Return a copy of string S with all occurrences of substring old replaced by new.  
    If the optional argument count is given, only the first count occurrences are replaced.
"""

# message = "I really like dogs."
# print message
# print message.replace("dog", "cat")
# # print message.rstrip()
# print message

