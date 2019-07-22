from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(name):
    print('启动下载进程，pid is %d' % getpid())
    print('开始下载 %s' % name)
    cost_time = randint(5, 10)
    sleep(cost_time)
    print('文件[%s]下载完成，耗时%d秒' % (name, cost_time))
    
    
def do_download():
    start = time()
    p1 = Process(target=download_task, args=('item AAA',))
    p1.start()
    p2 = Process(target=download_task, args=('music B', ))
    p2.start()
    # join()会阻塞改进程直到其执行完毕。
    # 如果执行到这段代码的时候其进程已经执行完毕了，那么就会允许通过
    p1.join()
    p2.join()
    end = time()
    print('total cost time %s seconds' % (end - start))


if __name__ == '__main__':
    do_download()
