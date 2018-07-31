#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(ord('A'))
print(ord('哈'))

print(chr(21704))
print('\u4e2d\u6587')
print('\\u4e2d\\u6587')

print('abc is %s, 123 is %d, 1.23 is %.3f' % ('abc',129,1.23))


print('%4d-%02d' % (123, 1))
print('%.2f' % 3.1415926)


# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
print('%3.1f%%' % float(((85-72)/72)*100))







