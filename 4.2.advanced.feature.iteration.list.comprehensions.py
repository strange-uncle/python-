#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = list(range(1, 10))
print(l)

#'a+1' 是要生成的对象, 'for a in l' 是迭代的逻辑, 'if a > 3 and a < 6'是迭代以后要判断的逻辑.
#只有判断通过了,才能计算生成公式'a+1'
#如下,迭代出来是[1, 2, 3, 4, 5, 6, 7, 8, 9]
#然后判断满足条件的是[4,5]
#最后根据公式'a+1'生成出来的是[5,6]
print([a+1 for a in l if a > 3 and a < 6])


d = {'a':1,'b':2,'c':3,'d':4}

#如下x,y 也可以用k,v来表示 key, value
for x, y in d.items():
    print('x= ', x, 'y = ', y)

