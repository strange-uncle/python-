import threading
import asyncio

'''
总结一下我对这个demo执行流程的理解.

def fn_consumer():
    goods = 'default'
    while True:
        n = yield goods
        if not n:
            print('before return, n is %s' % n)
            return
        print('consumer used %s when goods is %s ' % (n, goods))

1. 第一次调用是send(None)是必须的.
2. 遇到这一行n = yield goods, 不是完整的执行完这一行代码,
而是只执行 yield goods, 相当于 return goods.
考虑到goods是被初始化为default,
所以如下两句代码
    v = f.send(None)
    print('v is %s' % v)
会打印:
    v is default

3. 第二次调用是send(2), 'n = yield goods'这一行代码已经yield过了,这次执行的是yield
的后续逻辑,可以理解成为:
    n = [send value from outside]

所以,输出先是:
    consumer used 2 when goods is default 
然后继续WHILE, 执行yield goods:   
    default

4. 第三次调用是send(3), 逻辑和第二次调用一样, goods始终没有改动了

'''


# 理解教程里面的'生产者-消费者'例子
# 既然我上面已经对consumer方法理解了,那就没有必要再看教程里面的produce方法了
# produce方法和我手动写的如下测试语句没有本质上的区别


def fn_consumer():
    goods = 'default'
    while True:
        n = yield goods
        if not n:
            print('before return, n is %s' % n)
            return
        print('consumer used %s when goods is %s ' % (n, goods))

# 没有输出,直接
# Process finished with exit code 0
fn_consumer()

f = fn_consumer()

# TypeError: 'generator' object is not callable
# f(1)

# TypeError: can't send non-None value to a just-started generator
# f.send(2)

# send(None)没有输出,但符合上一个error的限制了
v = f.send(None)

# 输出: v is default
print('v is %s' % v)

# send(2)输出: consumer used 2 when goods is default
# default
# 然后就结束了:
# Process finished with exit code 0
v2 = f.send(2)
print(v2)

# consumer used 3 when goods is default
# default
v3 = f.send(3)
print(v3)


