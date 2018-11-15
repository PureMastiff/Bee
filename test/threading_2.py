# coding=utf-8

from threading import Thread, Lock
import time

g_num = 0


def work1():
    global g_num
    for i in range(100000):
        g_num += 1

    print('---in work1, g_num is {}'.format(g_num))


def work2():
    global g_num
    print('---in work2, g_num is {}'.format(g_num))


print('---线程创建之前 g_num is {}'.format(g_num))


def func1():
    t1 = Thread(target=work1)
    t1.start()

    #time.sleep(1)

    t2 = Thread(target=work2)
    t2.start()


def test1():
    global g_num

    for i in range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()

    print('---in test1, g_num is {}'.format(g_num))


def test2():
    global g_num
    for i in range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()

    print('---in test2, g_num is {}'.format(g_num))


mutex = Lock()


def func2():

    p1 = Thread(target=test1)
    p1.start()

    time.sleep(1)

    p2 = Thread(target=test2)
    p2.start()

    print('---in fun2, g_num is {}'.format(g_num))


if __name__ == '__main__':
    func2()