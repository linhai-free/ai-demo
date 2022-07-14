#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: my_car
@time: 2020/4/3 10:47 PM
@desc:
'''
# from car import Car, ElectricCar
# from car import *
from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
my_new_car.get_descriptive_name()

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()


# my_new_car = Car('subaru', 'outback', 2013)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(23500)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()


my_telsa = ElectricCar('telsa', 'model s', 2016)
my_telsa.get_descriptive_name()
