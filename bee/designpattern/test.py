# coding=utf-8


class A(object):
    def foo(self, x):
        print ("executing foo({},{})".format(self, x))
        print ('self:', self)

    @classmethod
    def class_foo(cls, x):
        print ("executing class_foo({},{})".format(cls, x))
        print ('cls:', cls)

    @staticmethod
    def static_foo(x):
        print ("executing static_foo({})".format(x))



class B(A):
    pass


a = A()

# print (a)
# print (a.foo)
# print (a.class_foo)
# print (a.static_foo)
#
# print A.foo
# print A.class_foo(1)
# print A.static_foo(1)


b = B()
print (b)
print b.foo
print b.class_foo
print b.static_foo


print B
# print B.foo(1)
print B.class_foo(1)
print B.static_foo(1)