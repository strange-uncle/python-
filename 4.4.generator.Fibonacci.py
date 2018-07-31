#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# fibonacci: 1,1,2,3,5,8,13,21,34,...
# 可以在最前面假设一个0的存在
# 那么就变形为:
# position:     1,2,3,4,5,6,7, 8, 9,...
# value:     0, 1,1,2,3,5,8,13,21,34,...
# 这样可以在函数里面写死第一个数字是1,
# 第二个是假设的0 + 第一位的1,
# 第三个是1+(第二位计算出来的数字),etc

print('普通函数的实现')


def fn_fibonacci(cnt):
    idx = 0
    previous = 0
    current = 1
    while idx < cnt:
        print(current)
        previous, current = current, previous + current
        idx += 1
    print('finished.')


fn_fibonacci(9)
print('生成器的实现')


def fn_fibonacci_g(cnt):
    idx = 0
    previous = 0
    current = 1
    while idx < cnt:
        yield current
        previous, current = current, previous + current
        idx += 1
    return 'finished.'


f = fn_fibonacci_g(9)

for a in f:
    print(a)







