# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

class Base(object):
    def __init__(self, task):
        raise NotImplementedError

    def start(self):
        """
        Do crawl
        :return:
        """
        raise NotImplementedError

    def crawl(self):
        """
        Crawl behavior
        :return:
        """
        raise NotImplementedError

    def parse(self):
        """
        Parse raw data to specific model
        :return:
        """
        raise NotImplementedError