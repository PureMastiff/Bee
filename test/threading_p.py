# coding=utf-8
import time
import threading


def saySorry():
    print('亲爱的，我错啦， 我能吃饭了吗？')
    time.sleep(1)


def func1():
    for i in range(5):
        saySorry()


def func2():
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()


def sing():
    for i in range(3):
        print('正在唱歌...{}'.format(i))
        time.sleep(1)


def dance():
    for i in range(3):
        print('正在跳舞...{}'.format(i))
        time.sleep(1)


def func3():
    print('---开始---：{}'.format(time.ctime()))

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为：{}'.format(length))
        if length <= 1:
            break
        time.sleep(0.5)

    print('---结束---：{}'.format(time.ctime()))


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name+' @'+str(i)
            print msg


def func4():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    func4()