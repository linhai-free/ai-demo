#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: my_gasoline_car
@time: 2020/4/3 10:53 PM
@desc:
'''
from car import GasolineCar

my_audi = GasolineCar('audi', 'a4', 2016)

# 实例方法
my_audi.get_descriptive_name()

# 类方法
my_audi.get_energy()
GasolineCar.get_energy()

# 静态方法
my_audi.show_time()
GasolineCar.show_time()

# 静态方法
my_audi.say_hello()
GasolineCar.say_hello()

my_audi.fill_gas_tank(40)
