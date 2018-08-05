import threading


amount = 100
lock_amount = threading.Lock()


def fn_change_amount(n):
    global amount
    amount += n
    amount -= n


def fn_threading(n):
    for i in range(200000):
        fn_change_amount(n)


def fn_threading_lock(n):
    for i in range(200000):
        lock_amount.acquire()
        try:
            fn_change_amount(n)
        finally:
            lock_amount.release()


threading_1 = threading.Thread(target = fn_threading, name = 'a', args = (9,))
threading_2 = threading.Thread(target = fn_threading, name = 'b', args = (3,))

threading_1.start()
threading_2.start()
threading_1.join()
threading_2.join()

# 需要多尝试几次,才可能看到效果
print('final amount is %s' % amount)

amount = 100

threading_1 = threading.Thread(target = fn_threading_lock, name = 'a', args = (9,))
threading_2 = threading.Thread(target = fn_threading_lock, name = 'b', args = (3,))

threading_1.start()
threading_2.start()
threading_1.join()
threading_2.join()
print('use lock, the final amount is %s' % amount)










