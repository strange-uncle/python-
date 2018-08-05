import asyncio
import random

'''
@asyncio.coroutine
def fn_simulate_io(arg):
    t = random.random() * 30
    asyncio.sleep(t)
    # 不能用time.sleep来模拟,这会使得当前线程真的sleep,而不会异步
    # time.sleep(t)
    return 'work result for %s with %f seconds' % (arg, t)


@asyncio.coroutine
def fn_do_work(arg):
    print('start work for task name: %s' % arg)
    # yield from后面的也需要被标记成@asyncio.coroutine
    t = yield from asyncio.async(fn_simulate_io(arg))
    print('result is %s' % t)


loop = asyncio.get_event_loop()
tasks = [fn_do_work(6), fn_do_work('abc')]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''

# python 3.5以后提供了新的语法,可以和上面的语法并存
# 装饰器@asyncio.coroutine 改成了async,不是装饰器了,是def的前缀
# yield from 改成了await
print('3.5新语法')

# 需要将上面的第一个loop注释掉,否则会报错
async def fn_simulate_io2(arg):
    t = random.random() * 30
    asyncio.sleep(t)
    # 不能用time.sleep来模拟,这会使得当前线程真的sleep,而不会异步
    # time.sleep(t)
    return 'work result for %s with %f seconds' % (arg, t)


async def fn_do_work2(arg):
    print('start work for task name: %s' % arg)
    t = await fn_simulate_io2(arg)
    print('result is %s' % t)

loop1 = asyncio.get_event_loop()
tasks1 = [fn_do_work2(6), fn_do_work2('abc')]
loop1.run_until_complete(asyncio.wait(tasks1))
loop1.close()



