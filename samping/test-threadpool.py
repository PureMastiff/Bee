# coding=utf-8

# import time
# import threadpool
# def sayhello(str):
#     print "Hello ",str
#     time.sleep(2)
#
# name_list =['xiaozi','aa','bb','cc']
# start_time = time.time()
# pool = threadpool.ThreadPool(10)
# requests = threadpool.makeRequests(sayhello, name_list)
# [pool.putRequest(req) for req in requests]
# pool.wait()
# print '%d second'% (time.time()-start_time)


# import threading
# import time
#
# def fun(argv):
#     print 'in', argv
#     time.sleep(2)
#
#
# threads = []    #用于保存线程
# for i in range(5):  #开5个线程
#     t = threading.Thread(target = fun, args = str(i))
#     threads.append(t)
#
# if __name__ == '__main__':
#     #开始所有的线程
#     for i in threads:
#         i.start()
#         print i
#     #保证线程执行完
#     for i in threads:
#         i.join()
#     print 'all over'
import threadpool

class A:
    member = "this is test"
    def __init__(self):
        pass

    @classmethod
    def Print1(cls):
        print "print 1:", cls.member

    def Print2(self):
        print "print 2:", self.member

    @classmethod
    def Print3(paraTest):
        print "print 3:", paraTest.member

    @staticmethod
    def print4():
        return "hello"


a = A()
A.Print1()
a.Print1()

#A.Print2()
a.Print2()

A.Print3()
a.Print3()

#A.print4()
#a.print4()


b = A.print4()
print b