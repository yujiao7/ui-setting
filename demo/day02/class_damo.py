#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'
#    类方法进行打包
class ClassDamo():
    def aaa(self):
        print("我是aaa")
    def bbb(self):
        print("我是bbb")
        self.aaa()
if __name__ == '__main__':
    c = ClassDamo()
    c.aaa()
    c.bbb()
    c.bbb()
    c.aaa()
