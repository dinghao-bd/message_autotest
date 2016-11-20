#!/usr/bin/env python
# encoding: utf-8
from uiautomator import device as d

from framework.page_object import PageObject
import util

"""
@version: 1
@author: ding hao
@mail: 619015618@qq.com
@file: send_message.py
@time: 2016/11/20 21:53
"""


class SendBox(PageObject):
    def __init__(self):
        super(SendBox, self).__init__()

    def visible(self):
        return d(textContains="收信人").wait.exists(timeout=util.TIMEOUT)
