#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = list(range(20))

print(l)

#注意下标的起点是0
#[x:y] 的终点y元素不包含
print(l[2:5])

print(l[2:])
print(l[:5])

print('负数是倒数,最后一个元素的位置是-1')
print(l[-3:])
print(l[-2:-1])
print('指定步长')
print(l[-6::2])

print('INDEX的顺序要从小到大,否则没有数据,返回的是[],如下:')
print(l[6:2])
print(l[-2:-6])
