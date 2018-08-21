# fork() 这种调用在WINDOWS下面不存在的
# 我的理解是,fork()会把当前进程的内部信息复制到一个新的进程(叫做子进程),是进程不是线程!
# 这两个进程的内容几乎一模一样,
# 可能只有极个别系统层面的设置不同
# (我第一次接触这个概念的时候,是类比的GITHUB的fork操作)
# 复制好以后,父子进程里面的代码就是一样的了,都会继续执行下去,
# 不存在说子进程里面的代码和父进程不一样.
# 但是,
# 调用fork()方法的时候会返回一个特殊的PID(process identification,进程标识符),需要接受这个PID,
# 对父进程,这个PID就是子进程真实的PID,不是父进程的PID哈!
# 对子进程,这个ID是0, 但是在子进程内部可以通过调用os.getpid()来获得子进程真实的PID
# 然后判断当前进程是父进程还是子进程,然后对父子进程分别执行不同的条件分支


import os


print('Current PID is %s' % os.getpid())

pid = os.fork()

if pid == 0:
    print('this is child process, pid is %s and parent pid is %s' % (os.getpid(), os.getppid()))
else:
    print('this is parent process, parent pid is %s and child pid is %s' % (os.getpid(), pid))

# 执行后的效果如下,子进程的创建需要时间,所以父进程先打印完毕,然后子进程创建好以后才能打印
# Current PID is 18909
# this is parent process, parent pid is 18909 and child pid is 18910
# this is child process, pid is 18910 and parent pid is 18909









