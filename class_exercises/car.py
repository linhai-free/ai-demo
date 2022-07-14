#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: car
@time: 2020/4/2 12:15 AM
@desc:
'''
import time
from datetime import datetime

"""
1、继承与覆盖
2、静态方法（staticmethod）、类方法（classmethod）、实例方法
"""


class Car(object):
    """一次模拟汽车的简单尝试"""
    energy = ''

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.litres = 20

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程碑读数设置为指定的值
        拒绝将里程表往回拨
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print "You cant't roll back an odometer!"

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self, litres):
        """给汽车加油"""
        self.litres += litres
        print "Fill " + str(litres) + " liters, there are " + str(self.litres) + " liters in the gas tank now."

    @classmethod
    def get_energy(cls):
        """打印汽车消耗的能源"""
        print "This car consumes " + cls.energy + "."

    @staticmethod
    def show_time():
        """打印当前时间"""
        print time.strftime("%H:%M:%S", time.localtime())

    @staticmethod
    def say_hello():
        """问候语"""
        if 6 <= datetime.now().hour < 18:
            print "Good morning, your have a amazing car!"
        else:
            print "Good evening, your have a wonderful car"


class GasolineCar(Car):
    """汽油车"""
    energy = 'gasoline'

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        Car.__init__(self, make, model, year)




