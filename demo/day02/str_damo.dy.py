#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'
#dergakio   要求生成两个新的字符串  drai  和egko
b ='dergakio'
print(b[:3])
print(b[1:5])
print(b[::2])
print(b[1::2])
# 字符串切片
d = '英语,数学,语文'
print(d.split(','))
d = '英语.数学.语文'
print(d.split('.'))

#去空格
c = '  dkjjdkfl   '
print(c.lstrip())  #去左空格
print(c.rstrip()) #去右空格
print(c.strip())  #去前后所有空格
c = '  dkjj  dkfl   '
print(c.replace(" ", "")) # 去除所有空格

c = '  dkjj  """dkfl   ' # 替换
print(c.replace('"'," '"))
print(c.replace(" ", ""))

#查找
y = 'dsjkdjsjk'
print(y.find('j'))

#长度
print(len(y ))



#GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
l = 'GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1'
l =l.split(" ")
method = l[0]
print("请求方法为："+method)
xieyibanben = l[2]
print("协议版本为：" + xieyibanben)
url = l[1]
print(url)
if('?' in url):
    print("请求数据为：" + url.split("?")[1])
    url = url.split("?")[0]
print(url)
print("协议名为：" + url[:url.find("://")])

url = url[url.find("://") + 3:]
print(url)
if(":" in url):
    print("域名或者ip为："+url.split(":")[0])
    url  = url.split(":")[1]
    print(url)
    print("端口号为：" + url[:url.find('/')])
    print("请求地址为：" + url[url.find('/'):])
else:
    print("域名或者ip为：" + url[:url.find('/')])
    print("请求地址为：" + url[url.find('/'):])


# 新增单个数据
a =[1,2,3,4,5]
a.append(6)
print(a)

# 新增多个数据
b =[7,8,9]
a.extend(b)
print(a)
c =[6,7,8]
a.extend(c)
print(a)
#删除数据
print(a.pop())
print(a)
print(a.pop(2))
print(a)
print(a.pop(-2))
print(a)
# 删除指定数据
a.remove(4)
print(a)
a.remove()
print(a)
# 修改列表中的数据
a[1]= 2
print(a)
# 排序reverse 排序规则升、默认False  降序true