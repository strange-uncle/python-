from time import time
from multiprocessing import Process, Queue


def main_slow():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for i in number_list:
        total += i
    print(total)
    end = time()
    print('total time cost is: %.3f s' % (end - start))


def task_handler(sub_list, result:'Queue'):
    total = 0
    for i in sub_list:
        total += i
    result.put(total)


def main_multi_processing():
    number_list = [x for x in range(1, 100000001)]
    process_list = []
    result_queue = Queue()
    index = 0
    total = 0
    for i in range(8):
        p = Process(target=task_handler, args=(number_list[index:index+12500000], result_queue))
        process_list.append(p)
        index += 12500000
        p.start()
    
    start = time()
    for p in process_list:
        p.join()
    
    while not result_queue.empty():
        total += result_queue.get()
    print('total is %s' % total)
    end = time()
    print('total cost is %.3f s' % (end - start))


if __name__ == '__main__':
    # 5000000050000000
    # 4.549 s
    # main_slow()

    # total is 5000000050000000
    # total cost is 1.084 s
    main_multi_processing()
