# coding=utf-8

'''=运行过程中限制实例的属性，运行过程中不能修改='''



class Person(object):
    __slots__ = ("name", "age")


class Test(Person):
    pass


if __name__ == '__main__':
    P = Person()
    P.name = 'linda'
    P.age = 20
    #P.score = 100

    t = Test()
    t.score = 110
    print t.score