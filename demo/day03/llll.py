#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'

# 字典新增
a={}
aa ={'name':'小明同学','sax':'女'}
aa['age']=24
print(aa)
# 删除字典
# del aa
# print(aa)
# 清空
# aa.clear()
# aa = {}
# 改
aa["name"]="小红同学"
print(aa)
# 查
print(['小红同学'])
# 获取字典长度
print(len(aa))
# 成员判断只能用key 做判断
print("name"in aa)
#字典拼接
dd ={"1":'234',"2":'567'}
ff ={"3":'567',"4":'890'}
dd.update((ff))
print(dd)
print('-------------------')
# 生成一个新的
print(dict(dd,**ff))

# 打开文件夹下文件
# ff = open("test.txt","r",encoding='utf-8')

# print(ff.readlines())

# ff.close()
# 第二种
# print(ff.read())
# ff.close()
# 写入内容write.
ff = open("test.txt","a",encoding='utf-8')
ff.write('fhdfhdsklfkdsfk\n')
ff.close()


