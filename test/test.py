# coding=utf-8

import types

'''=运行的过程中给类绑定(添加)方法='''


class Person(object):

    num = 0;

    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    def eat(self):
        print "eat food"


#定义一个实例方法
def run(self, speed):
    print("%s在移动， 速度是 %d km/h"%(self.name, speed))


#定义一个类方法
@classmethod
def testClass(cls):
    cls.num = 100


#定义个静态方法
@staticmethod
def testStatic():
    print("--------static method------")


if __name__ == '__main__':
    #创建一个实例对象
    P = Person("Linda", 24)
    #调用在class中的方法
    P.eat()

    #给这个对象添加实例方法
    P.run = types.MethodType(run, P)
    #调用实例方法
    P.run(300)

    #给Person类绑定类方法
    Person.testClass = testClass
    #调用类方法
    print (Person.num)
    Person.testClass()
    print (Person.num)

    #给Person类绑定静态方法
    Person.testStatic = testStatic
    #调用静态方法
    Person.testStatic()