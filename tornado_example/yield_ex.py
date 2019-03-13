# coding=utf-8


def demoItertor():
    print "First"
    yield 1


for i in demoItertor():
    print "--------"
    print i