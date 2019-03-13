# coding=utf-8
'''python 官方建议 废弃apply， 尽量使用apply_async'''


import time
import os
from multiprocessing import Pool


def test():
    print(
        "---进程池中的进程--- pid={}, ppid={}---").format(os.getpid(), os.getppid())
    for i in range(3):
        print("---{}----".format(i))
        time.sleep(1)
    return 'hahahh'


def test2(args):
    print("---callback func---pid={}".format(os.getpid()))
    print("---callback func---args={}".format(args))


pool = Pool(3)
pool.apply_async(func=test, callback=test2)
pool.close()
pool.join()

#time.sleep(4)

print("---主进程-pid={}".format(os.getpid()))