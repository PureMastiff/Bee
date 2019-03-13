# coding=utf-8

import time

from concurrent.futures import ThreadPoolExecutor
from tornado import gen


thread_pool = ThreadPoolExecutor(2)


def anysleep(count):
    for i in range(count):
        time.sleep(1)

@gen.coroutine
def call_backing():
    print "start of call backing"
    yield thread_pool.submit(anysleep, 10)
    print "end of call backing"


call_backing()



