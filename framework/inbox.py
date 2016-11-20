#!/usr/bin/env python
# encoding: utf-8
from uiautomator import device as d

from framework.page_object import PageObject
import util
"""
@version: 1
@author: ding hao
@mail: 619015618@qq.com
@file: inbox.py
@time: 2016/11/20 21:49
"""


class Inbox(PageObject):
    def __init__(self):
        super(Inbox, self).__init__()

    def visible(self):
        return d(text="短信").wait.exists(timeout=util.TIMEOUT)
