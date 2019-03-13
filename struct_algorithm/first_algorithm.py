# coding=utf-8

import time


def fun1():
    start_time = time.time()

    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    print a, b, c

    end_time = time.time()
    print "elapsed: {}".format( end_time - start_time)


def fun2():
    start_time = time.time()

    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a -b
            if a ** 2 + b ** 2 == c ** 2:
                print a, b, c

    end_time = time.time()
    print "elapsed: {}".format( end_time - start_time)


def fun3():
    #l = list(range(1000))
    #l = [i for i in range(1000)]
    l = []
    for i in range(1000):
        l.append(i)
    print l


if __name__ == "__main__":
    # fun1()   elapsed: -194.673608065
    # fun2()   elapsed: 0.185308933258
    start_time = time.time()
    fun3()
    end_time = time.time()
    print "elapsed: {}".format( end_time - start_time)
