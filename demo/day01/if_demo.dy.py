#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/4'
# if （条件）
'''
if分支语句
if
print()
else
'''
a =1 # 1代表有水果，0代表没有水果
if(a == 1):
   print('水果')
else:
    print('没有')

# 80分为优秀 60-80为优秀 60及格 60以下不及格
ss = 90
if(ss >= 80):
    print('为优秀')
if(ss >= 60 and ss < 80):
    print('良好')
if(ss < 60):
    print('为不及格')
if(ss >= 80):
    print('为优秀')
elif(ss > 60):
    print('良好')
else:
    print('不及格')
if (ss > 80):
    print('最优秀')
elif(ss > 60):
    print('良好')
else:
    print('不及格')