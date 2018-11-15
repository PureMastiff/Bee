# coding=utf-8


def fib(times):
    n = 0
    a,b = 0, 1
    while n<times:
        yield b
        a,b = b, a+b
        n+=1


def gen():
    i = 0
    while i<5:
        temp = yield i
        #print "dddd"
        #print(temp)
        i += 1


if __name__ == '__main__':
    L = [x*x for x in range(5)]
    print L

    G = (x*x for x in range(5))
    for x in G:
        print x

    for f in fib(1):
        print f

    print("=========")
    f1 = gen()
    for i in f1:
        print i
