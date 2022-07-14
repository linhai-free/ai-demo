#!/usr/bin/env python
# encoding: utf-8

__author__ = 'luodejin'

'''
@author: luodejin
@license: (C) Copyright 2019-2029, Beijing TaoYou World Technology Corporation Limited.
@contact: luodejin@taou.com
@software: maimai
@file: gevent_monkey
@time: 2020/7/21 11:05 AM
@desc: 使用gevent + monkey.patch_all()自动调度IO协程
'''
import gevent
import requests
import time
from gevent import monkey

monkey.patch_all()


def get_page_text(url, order=0):
    print 'No%d:%s请求开始...' % (order, url)
    resp = requests.get(url)  # 发起网络请求，返回需要时间——阻塞IO

    html = resp.text
    # print html.encode('utf-8')
    print 'No%d:%s成功返回：长度%d' % (order, url, len(html))


if __name__ == '__main__':
    start = time.time()
    time.clock()
    gevent.joinall([
        gevent.spawn(get_page_text, 'http://www.sina.com', order=1),
        gevent.spawn(get_page_text, 'http://www.qq.com', order=2),
        gevent.spawn(get_page_text, 'http://www.baidu.com', order=3),
        gevent.spawn(get_page_text, 'http://www.163.com', order=4),
        gevent.spawn(get_page_text, 'http://www.4399.com', order=5),
        gevent.spawn(get_page_text, 'http://www.sohu.com', order=6),
        gevent.spawn(get_page_text, 'http://www.youku.com', order=7),
        gevent.spawn(get_page_text, 'http://www.iqiyi.com', order=8),
    ])
    end = time.time()
    print 'over, 耗时%d秒' % (end - start)
    # time.clock() 在不同的系统上含义不同：
    #     在UNIX系统上，它返回的是"进程时间"，它是用秒表示的浮点数（时间戳）。
    #     而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
    print time.clock()



