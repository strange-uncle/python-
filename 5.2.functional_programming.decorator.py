import datetime


def fn_print_str(x = ''):
    print('function works for:', x)


fn_print_str('a')
fn_print_str()
fn_print_str('0')


def log_arg(fn):
    def wrapper(*args, **kwargs):
        print(datetime.datetime.now())
        return fn(*args, **kwargs)
    return wrapper


@log_arg
def fn_print_arg(a):
    print('function fn_print_arg:', a)


fn_print_arg('1')


def log_arg2(x):
    def log(fn):
        def wrapper(*args, **kwargs):
            print(x, '--', datetime.datetime.now())
            return fn(*args, **kwargs)
        return wrapper
    return log


@log_arg2('9')
def fn_print_arg2(a):
    print('function fn_print_arg2:', a)


fn_print_arg2('666')








