#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是有序的,没有什么特别的.
# 唯一需要留意的就是起点是0
# 可以用-1来倒序获取数据

l = ['a', 123, '哈哈哈', '666']

print(l[1], l[3])
print(l[-1], l[-2])

# tuple如果只有一个元素,不能直接写
t = (1)
print(t, type(t))

# 而是要加一个逗号
t2 = (1,)
print(t2, type(t2))

#tuple里面元素的指向是不能修改的
#'tuple' object does not support item assignment
l2 = [123,456]

print('tuple里面元素的指向是不能修改的')
t3 = ('a',123, l2)

print(t3)
#tuple指向l2是没有改变的,但l2内部的数据可以改变
#注意,是str是不可变对象, list才是可变对象
l2[1] = '666'
print(t3)



# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])






