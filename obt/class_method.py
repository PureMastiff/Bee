# coding=utf-8


class A(object):
    _g = 1

    def foo(self, x):
        print('executing foo {} {}'.format(self,x))

    @classmethod
    def class_foo(cls, x):
        print('executing class_foo {} {}'.format(cls._g, x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo {}'.format(x))


a = A()
a.foo(1)
a.class_foo(1)
A.class_foo(1)
a.static_foo(1)
A.static_foo('hi')

print a.foo
print a.class_foo
print a.static_foo
print A.class_foo
print A.static_foo
print A.foo