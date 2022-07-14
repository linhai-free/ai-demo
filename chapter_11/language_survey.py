#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: language_survey
@time: 2020/4/12 10:26 PM
@desc:
'''
from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print "Enter 'q' at any time to quit.\n"
while True:
    response = raw_input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print "\nThank you to everyone who participated in the survey!"
my_survey.show_results()
