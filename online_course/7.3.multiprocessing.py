from multiprocessing import Process, Pool, Queue, Manager
import os
import random
import time


def fn_print(*args):
    print('This is child process, arg is: %s and pid is %s' % (args, os.getpid()))


print('parent process pid is %s' % os.getpid())
p = Process(target = fn_print, name = 'process test name', args = ('a', 'b', 123))
print('child process name is %s' % p.name)
p.start()

# join()是等待子进程结束的意思,然后再继续执行父进程
p.join()
print('all done.')


# 进程池
def fn_run_random(arg):
    print('Start to run sub process with arg: %s, pid is %s' % (arg, os.getpid()))
    start_time = time.time()
    time.sleep(random.random() * 10)
    end_time = time.time()
    print('sub process % s finished in %s seconds' % (arg, end_time - start_time) )


# 执行了apply_async以后,马上在主进程里面执行fn_run_callback, 这时候子进程多半还没有执行完毕
def fn_run_callback(arg):
    print('callback for arg: %s with pid is %s, but this sub process is not finished yet...' % (arg, os.getpid()))


process_pool = Pool(5)
print('Start to apply 10 sub processes...')
for i in range(10):
    process_pool.apply_async(func = fn_run_random, args = (i,), callback = fn_run_callback(i))
process_pool.close()
process_pool.join()
print('All done for 10 sub processes.')


# 进程间通信
print('进程间通信 ---> 手动创建进程')


def fn_write(q):
    print('Start to put new values into Queue')
    for item in range(6):
        q.put(item)
        print('put %s done.' % item)
        time.sleep(0)


def fn_read(q):
    while True:
        print('Get value %s from Queue.' % q.get())


def fn_read_with_limit(q, times = 3):
    cnt = 0
    while True:
        t = q.get()
        if cnt > times:
            break
        elif t is not None:
            cnt += 1
            print('Get value %s from Queue within Pool' % t)


_queue = Queue()

# 如下是手动创建进程,可以work
p_write = Process(target = fn_write, args = (_queue,))
p_read = Process(target = fn_read, args = (_queue,))
p_write.start()
p_read.start()

p_write.join()
time.sleep(6)
p_read.terminate()

print('Queue test is done.')

print('进程间通信 ---> 利用进程池')

# 在利用POOL的时候,之前的_queue = Queue()看不出来效果, 但是也没有报错信息
# 修改成为manager.Queue()以后就好了
manager = Manager()
_queue2 = manager.Queue()

p2 = Pool(3)
p2.apply_async(func = fn_write, args = (_queue2,))
p2.apply_async(func = fn_read_with_limit, args = (_queue2, 3))
p2.close()
p2.join()

print('进程间通信 ---> 利用进程池 is done.')




