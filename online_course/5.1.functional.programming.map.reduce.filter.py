#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
from functools import reduce

# map(fn,Iterable),第一个参数是要应用的函数, 第二个参数是Iterable 可迭代的对象.
# 返回的是 Iterator对象.

# 注意Iterable和Iterator不一样.
# Iterable是可迭代的,比如str, list
# Iterator是迭代器,特指可以被next()处理的对象. 显然我们不能用next()处理str.

l = [1,2,3,4,5]


def fn_int2str(a):
    return str(a)


def fn_str2int(a, b):
    return a*10 + b


a = map(fn_int2str, l)

print(l)
print('map fn_int2str result is ', list(a))

# reduce 效果如下:
# reduce(f, 1, 2, 3, 4) = f(f(f(1,2),3),4)
b = reduce(fn_str2int, l)

print('reduce fn_str2int result is', b)


# filter(fn, Iterable ) 用于过滤一个序列
# 把fn依次应用于 第二个序列里面的每一个元素,看fn返回true or false来决定时候保留当前元素
l2 = list(range(0,12))


def fn_filter(a):
    if a % 2 == 0:
        return True
    return False


print('apply filter() to get odd:')
odd = filter(fn_filter, l2)
for i in odd:
    print(i)







