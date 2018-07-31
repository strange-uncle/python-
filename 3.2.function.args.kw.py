#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
POSITIONAL_OR_KEYWORD（位置参数或关键字参数）
VAR_POSITIONAL（可变参数）
KEYWORD_ONLY（关键字参数）
VAR_KEYWORD（可变关键字参数）
POSITIONAL_ONLY（位置参数）
'''


# 关键字(**kw)参数
print('关键字(**kw)参数')


def fun_kw(x, y, **kwargs):
    print('x:', x, 'y:', y, 'kw:', kwargs)
    # 判断kwargs是否传入了指定名字的参数
    if 't' in kwargs:
        print('t is :', kwargs['t'])


fun_kw('a', 'b')
# **kw要指定参数名字,比如 't = '
fun_kw('a', 'b', t = '66')


# 命名关键字(*, ?)参数 是必须要传入的
# 如果命名关键字前面定义了可选关键字,那么命名关键字就不用再加*,例如
# def fun_kw2(x, y, *args, t, z)
# 如果命名关键字前面 没有定义可选关键字,那么命名关键字就需要 加'*,',例如
# def fun_kw2(x, y, *, t, z)


print('命名关键字(*, ?)参数')


def fun_kw2(x, y, *, t, z):
    print('x:', x, 'y:', y, 't:', t, 'z:', z)


print('命名关键字(*, ?)参数在传入的时候,一定要指定参数名字,否则要报错')

# 正确的调用方法
print('命名关键字(*, ?) 正确的调用方法,必须要传入 t, z')

fun_kw2(1, 2, t='ttt', z = 'zzzz')


