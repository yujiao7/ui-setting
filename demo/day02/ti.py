#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'
def jiujiu ():  # 取别名
 for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,'=',i*j,'\t',end='')
    print()

jiujiu() # 按别名打印
# 老师的例题
# 求出1+2+3.。。+100和
def qiu_he():
    s = 0
    for i in range(100):
        s = s + i + 1
    print(s)
# 求出100! 1*2*3*4....*100
def qiu_jie_cheng():
    s = 1
    for i in range(1,101):
        s *= i
    print(s)
# 求出100以内的质数
def zhi_shu():
    for i in range(2,101):
        if(i == 2):
            print(i)
            continue
        f = 1 # 1代表这个数是质数，0代表这个数不是质数
        for j in range(2, i):
            if (i % j == 0):
                f = 0
                break
        if(f == 1):
            print(i)


# 打印出九九乘法表（循环嵌套）
def jiu_jiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j,"X",i,'=',i*j,"\t",end="")
        print()
# 冒泡排序
def mao_pao():
    a = [90, 43, 2, 63, 6, 3, 4]
    #外层循环确定待排序的位置
    for i in range(len(a)-1,0,-1):
        #内层循环依次取相邻的两个数据
        for j in range(i):
            # if判断比较相邻两个数据的大小，如果前边大于后边的，则交换位置
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
    print(a)



if __name__ == '__main__':
    a = [90, 43, 2, 63, 6, 3, 4]
    #外层循环确定待排序的位置
    for i in range(len(a)-1,0,-1):
        #内层循环依次取相邻的两个数据
        for j in range(i):
            # if判断比较相邻两个数据的大小，如果前边大于后边的，则交换位置
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
    print(a)

#方法定义 有参数有返回值
def jianfa(a,b):
    print(a - b)
#方法调用
jianfa(8,3)
jianfa(50,3)

#无参数有返回值
def jianfa(a,b):
      return a - b
c = jianfa(9,0)
print(c)

def jianfa():
    a = 5
    b = 1
#进行打包
def aaa(*args,**kwargs):
    print(args)
    print(kwargs)
aaa(1,2,3,4,a = 20 ,b =40 )
def bbb(a,b=40):
    return a+b
print(bbb(20))
print(bbb(10,20))


# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)

# 求出1+2+3.。。+100和
s = 0
for i in range(1,101):
    s += i
print(s)

# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)

for i in range(2,100):
    f = False # 标记i是否被整除
    for j in range(2,i):
        if(i%j==0):
            f = True #如果i被整除，把f值改成True
            break
    if (not f):
        print(i)

# 打印出九九乘法表（循环嵌套）
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"X",i,'=',i*j,'\t',end='')
    print()

    # 冒泡排序
    a = [90, 43, 2, 63, 6, 3, 4]
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)