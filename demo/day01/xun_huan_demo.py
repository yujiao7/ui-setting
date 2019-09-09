#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/4'
# for 循环
# for i in range

#打印100以内，遇到10终止
for i in range(100):
    if(i == 10):
        break
    print(i)

#打印100以内被5整除跳过
for i in range(100):
    if( i%5 == 0):
        continue
    print(i)

#求1+2+3+4+5......+100的和
def qiuhe():
 a = 0
for i in range(1, 101):
    a = a + i
print(a)

#求出100以内的质数
num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)
#打印出九九乘法表（循环嵌套）
row = 1 # 行号
while row<=9:
    col = 1 # 列号
    while col<=row:
        # print("*",end="")
        print("%d * %d = %d" %(col,row,col*row) ,end="\t") # 用转义字符 \t 使输出结果对齐
        col += 1
    print("")
    row += 1

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,'=',i*j,'\t',end='')
    print()

#冒泡排序
a = [90,43,2,63,6,3,4]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if(a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
print(a)
#求出100的乘积
s = 1
for i in range(1,101):
    s *= i
print(s)



qiuhe()


i = 1
while(i<101):

    print(i)
    i += 1