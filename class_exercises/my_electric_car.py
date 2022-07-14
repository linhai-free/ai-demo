#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: my_electric_car
@time: 2020/4/3 10:50 PM
@desc:
'''
from car import ElectricCar

my_telsa = ElectricCar('telsa', 'model s', 2016)

# 实例方法
my_telsa.get_descriptive_name()
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()
my_telsa.fill_gas_tank()

# 静态方法
my_telsa.show_time()
ElectricCar.show_time()

# 类方法
my_telsa.get_energy()
ElectricCar.get_energy()