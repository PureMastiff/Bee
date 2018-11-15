# coding=utf-8

import os
import time
import random
from multiprocessing import Pool


def worker(msg):
    t_start = time.time()
    print("{}开始执行， 进程号为{}".format(msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print('{}, 执行完毕，耗时{}'.format(msg, t_stop-t_start))


if __name__ == '__main__':
    po = Pool(3)
    for i in range(0, 10):
        #po.apply_async(worker, (i,)) #非阻塞
        po.apply(worker, (i,))  #阻塞

    print('- - - start - - -')
    po.close()
    po.join()
    print('- - - end - - -')