# coding=utf-8
from time import ctime, sleep
import functools

def foo():
    print('foo')

#表示是函数
foo

#表示执行foo函数
foo()


def foo1():
    print('foo1')


foo1 = lambda x,y: x+y
print foo1(1, 7)


def w1(func):
    def inner():
        print("yanzheng")
        func()
    return inner

@w1
def f1():
    print("f111111")

@w1
def f2():
    print('f2')

@w1
def f3():
    print('f3')

@w1
def f4():
    print('f4')


def timefun(func):
    def wrappedfunc():
        print('{} called at {}'.format(func.__name__, ctime()))
        return func()
    return wrappedfunc


@timefun
def noo():
    print("I am noo")


@timefun
def getInfo():
    return '---hahah---'


def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper


@note
def test():
    "test function"
    print('I am test')


if __name__ == '__main__':
    f1()
    f2()
    f3()
    f4()

    noo()
    sleep(2)
    noo()

    print(getInfo())


    print("-------------------")


    test()
    print(test.__doc__)