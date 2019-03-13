# coding=utf-8


class Foo(object):
    def f1(self):
        print('origin f1')

    def f2(self):
        print('origin f2')


class Foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print ('decorated f1')
        self._decoratee.f1()

    def __getattr__(self, item):
        return getattr(self._decoratee, item)


u = Foo()
v = Foo_decorator(u)
v.f1()
v.f2()
