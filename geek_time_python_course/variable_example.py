g_x = 100

def access_gloabl_var(i:int):
    # 要修改全局变量的值，这里才需要加上global
    # 如果只是读取，那么就不需要加global
    # 例如下面只是读取，就不用加global：
    # x = g_x + 1
    global g_x
    g_x += i
    print(g_x)


access_gloabl_var(20)
# not_defined_foo('abc')


# 在前面调用这个方法，是会报错的，因为这个方法在运行的时候才是现场建立
def not_defined_foo(s: str):
    print(f'{s} - this fun is not defined before execute.')


# def只是声明定义了一个fun,调用之前都不会实际建立，所以这个可以“引用”一个后面才def的foo_2
def foo_1(s1):
    print(f'into foo_1 - {s1}')
    foo_2(s1)

# foo_2 还没建立，会报错
# foo_1('test')


def foo_2(s2):
    print(f'into foo_2 - {s2}')


foo_1('test')

