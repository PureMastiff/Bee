# coding=utf-8


def A():
    print 1
    print 2
    print 3


def B():
    print "x"
    print "y"
    print 'z'


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming {}...'.format(n))
        r = '200 ok'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print ('[PRODUCER] Producering {}...'.format(n))
        r = c.send(n)
        print ('[PRODUCER] Consumer return: {}'.format(r))
    c.close()





if __name__ == "__main__":
    c = consumer()
    produce(c)
