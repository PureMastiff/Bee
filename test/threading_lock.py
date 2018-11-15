# coding=utf-8

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num, sleeptime):
        threading.Thread.__init__(self)
        self.num = num
        self.sleepTime = sleeptime

    def run(self):
        self.num += 1
        time.sleep(self.sleepTime)
        print('线程{}, num={}'.format(self.name, self.num))


def test(sleepTime):
    num =1
    time.sleep(sleepTime)
    num += 1
    print('---({})--num={}'.format(threading.current_thread(), num))


def func1():
    t1 = threading.Thread(target=test, args=(5,))
    t2 = threading.Thread(target=test, args=(1,))

    t1.start()
    t2.start()


if __name__ == '__main__':
    #mutex = threading.Lock()
    t1 = MyThread(100, 1)
    t1.start()
    t2 = MyThread(200, 1)
    t2.start()

    func1()
