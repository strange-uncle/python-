#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#默认参数
def a(x = 1, y = 2):
    return (x, y)

print(a(1,3))
print(a(1))
print(a(y=3))
print(a())

#return要单独用一行,不能如下这样搞
#因为LIST是可变对象,如下会返回<class 'NoneType'>
print('小心可变对象的return')
def wrong_fun(L=[]):
    return L.append('a')

x1 = [123]
#x2其实是append方法返回的数据,这种情况下返回数据是没有太大意义的,这个append函数的用处是修改数据
x2 = x1.append('6')
print(type(x2))


#默认参数要定义成不变对象
print('默认参数要定义成不变对象')
def b(L=[]):
    L.append('a')
    return L
print(b([1,2,3]))
print(b([6]))
print(type(b([6])))

print(b())
print(b())

#函数的可变参数接受tuple
print('函数的参数接受tuple')
def sum_tuple(tp):
    i = 0
    for x in tp:
        i += x
    return i

#但像如下这样写,很麻烦的
print(sum_tuple((1,2)))
print(sum_tuple((1,2,3)))

print('函数的可变参数接受tuple, 用*指定')
def sum_tuple2(*tp):
    i = 0
    for x in tp:
        i += x
    return i
#像如下这样写,可以支持不传递参数,或者传递任意个数的参数,不用把参数封装成tuple了
print(sum_tuple2())
print(sum_tuple2(1, 2))
print(sum_tuple2(1, 2, 3))



















