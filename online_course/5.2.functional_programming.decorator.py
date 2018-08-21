import datetime
import functools


def fn_print_str(x = ''):
    print('function works for:', x)


fn_print_str('a')
fn_print_str()
fn_print_str('0')


# decorator本身不接受参数
def log_arg(fn):
    def wrapper(*args, **kwargs):
        print(datetime.datetime.now())
        return fn(*args, **kwargs)
    return wrapper


@log_arg
def fn_print_arg(a):
    print('function fn_print_arg:', a)


fn_print_arg('1')


# decorator接受参数
def log_arg2(x):
    def log(fn):
        def wrapper(*args, **kwargs):
            print(x, '--', datetime.datetime.now())
            return fn(*args, **kwargs)
        return wrapper
    return log


# decorator接受参数9, 看清楚这不是函数的参数,是decorator的参数
@log_arg2('9')
def fn_print_arg2(a):
    print('function fn_print_arg2:', a)


fn_print_arg2('666')


# decorator接受参数,包含的函数在执行前后分别打印文字
def log_arg_3(x):
    def log(fn):
        def wrapper(*args, **kwargs):
            print('函数执行之前 ->')
            f = fn(*args, **kwargs)
            print('函数执行之后 ->', x)
            return None
        return wrapper
    return log


@log_arg_3('log的参数')
def fn_print_arg3(a):
    print('function fn_print_arg2:', a)


fn_print_arg3('123')
f2 = log_arg_3(fn_print_arg3('print name below'))
# 打印出来是'log', 实际上我们需要的是被包装的函数的内部属性,而不是装饰器的属性.
print(f2.__name__)


# 所以需要把函数的内部属性赋值给装饰器
# 完整版的装饰器, 还可以获取函数返回的值
def log_arg_wrapper(s):
    def log(fn):
        # 关键的代码,需要放在能够访问fn的范围
        functools.wraps(fn)

        def wrapper(*args, **kwargs):
            print('before wrapper -> ', s)
            f = fn(*args, **kwargs)
            print('after wrapper ->', s)
            # 将fn的返回值传递出去.如果不需要,可以return None
            return f
        return wrapper
    return log


@log_arg_wrapper('full version of wrapper')
def fn_int2str(i):
    print('this is fn_int2str')
    return str(i)


def fn_int2str_no_wrapper(i):
    print('this is fn_int2str_no_wrapper')
    return str(i)


print('测试完整版的wrapper. fn_int2str_no_wrapper')
a = fn_int2str_no_wrapper(123)
print('a is ', a)


print('测试完整版的wrapper. fn_int2str')
b = fn_int2str(123)
print('b is ', b)
