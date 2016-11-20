#!/usr/bin/env python
# encoding: utf-8
from uiautomator import device as d

"""
@version: 1
@author: ding hao
@mail: 619015618@qq.com
@file: page_object.py
@time: 2016/11/11 11:43
"""


class PageObject(object):
    def __init__(self):
        # self.driver = driver
        self.screen = {'width': d.info['displayWidth'], 'height': d.info['displayHeight']}

    def visible(self):
        pass
