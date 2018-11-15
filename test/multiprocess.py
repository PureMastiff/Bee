# coding=utf-8

import os
import time
from time import sleep
from multiprocessing import Process


def func1():
    num = 0
    pid = os.fork()

    if pid == 0:
        num += 1
        print('haha1---num={}'.format(num))
    else:
        sleep(1)
        num += 1
        print('haha2---num={}'.format(num))

    print('aaaaaa')


def func2():
    pid = os.fork()
    if pid == 0:
        print('haha1')
    else:
        print('haha2')

    pid = os.fork()
    if pid == 0:
        print('haha3')
    else:
        print('haha4')

    print('-------')


def run_proc(name, age, **kwargs):
    for i in range(100):
        print('子进程运行中， name={}, age={}, pid={}'.format(name, age, os.getpid()))
        print(kwargs)
        sleep(0.5)

def func3():
    print('父进程{}'.format(os.getpid()))
    p = Process(target=run_proc, args=('test', 28), kwargs={'m': 20})
    print('子进程要执行')
    p.start()
    sleep(10)
    p.terminate()
    print('11111')
    p.join() #join()方法等子进程结束后再继续往下运行，通常用于进程间的同步
    #sleep(2)
    print('子进程已结束')


def work_1(interval):
    print("work_1 父进程({}), 当前进程({})".format(os.getppid(), os.getpid()))
    t_start = time.time()
    sleep(interval)
    t_end = time.time()
    print("work_1, 执行时间为{}".format(t_end - t_start))


def work_2(interval):
    print("work_2 父进程({}), 当前进程({})".format(os.getppid(), os.getpid()))
    t_start = time.time()
    sleep(interval)
    t_end = time.time()
    print("work_2, 执行时间为{}".format(t_end - t_start))


def func4():
    print("进程ID：{}".format(os.getpid()))

    p1 = Process(target=work_1, args=(2,))
    p2 = Process(target=work_2, name='dog', args=(1,))

    p1.start()
    p2.start()

    print('p2.is_alive={}'.format(p2.is_alive()))

    print('p1.name={}'.format(p1.name))
    print('p1.pid={}'.format(p1.pid))
    print('p2.name={}'.format(p2.name))
    print('p2.pid={}'.format(p2.pid))

    p1.join()
    print('p1.is_alive={}'.format(p1.is_alive()))


if __name__ == '__main__':
    func4()