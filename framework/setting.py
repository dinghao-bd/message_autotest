#!/usr/bin/env python
# encoding: utf-8
from uiautomator import device as d

from framework.page_object import PageObject
import util
"""
@version: 1
@author: ding hao
@mail: 619015618@qq.com
@file: setting.py
@time: 2016/11/20 22:00
"""
class Setting(PageObject):
    def __init__(self):
        super(Setting, self).__init__()

    def visible(self):
        return d(textContains="设置").wait.exists(timeout=util.TIMEOUT)