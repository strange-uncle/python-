#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 列表生成式(list comprehensions)是完整生成一个列表,所以生成后就占据了完整的内存.
# 而生成器(generator)是惰性的.
# 定义的时候并没有马上生成完整的内容
# 而是在调用的时候,调一次,生成一个内容
# 可以有效降低内存占用

# 语法上的重点就是用小括号(),而不是列表生成式的方括号[]
l = list(range(10))

l1 = [a for a in l if a < 3]
l2 = (a for a in l if a < 3)

# <class 'list'> <class 'generator'>
print(type(l1), type(l2))

# 持续调用next(fn())来获得generator的结果'
# 但是会遇到 StopIteration错误
# for i in range(6):
#    print(next(l2))

# 正确的方式是不要直接调用next(),而是要去迭代这个 generator,
# 自然就可以获得生成器内部的数据了
for i in l2:
    print(i)










