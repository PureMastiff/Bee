# coding=utf-8

import os
import time
import random
from multiprocessing import Process, Queue, Manager, Pool


def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put {} to queue...'.format(value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print 'Get {} from queue'.format(value)
            time.sleep(random.random())
        else:
            break


def fun1():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pw.join()

    pr.start()
    pr.join()

    print ''
    print '所有数据都写入并且读完'


def reader(q):
    print('reader启动{}.父进程为{}'.format(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print('reader从Queue获取消息：{}'.format(q.get(True)))


def writer(q):
    print('writer启动{}.父进程为{}'.format(os.getpid(), os.getppid()))
    for i in 'dongGe':
        q.put(i)


def func2():
    print('({}) start'.format(os.getpid()))
    q = Manager().Queue()
    po = Pool()
    po.apply(writer, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print('{} End'.format(os.getpid()))


if __name__ == '__main__':
    func2()
