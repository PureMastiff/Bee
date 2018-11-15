# coding=utf-8

import os
import time
from time import sleep


def sing():
    for i in range(3):
        print("正在唱歌... %d"%i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞... %d"%i)
        sleep(1)


def main():
    rpid = os.fork()
    if rpid<0:
        print('fork调用失败')
    if rpid == 0:
        print('我是子进程{}， 我是父进程{}'.format(os.getpid(), os.getppid()))
    else:
        print('我是父进程{}， 我是子进程{}'.format(os.getpid(), rpid))

    print("父子进程都可以执行这里的代码")


if __name__ == '__main__':
    main()