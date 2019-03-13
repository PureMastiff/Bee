# coding=utf-8


from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch("http://www.baidu.com")
    print response.headers

@gen.coroutine
def call():
    print "start call anothrer coroutine"
    yield coroutine_visit()
    print "end of call_coroutine"


def func_normal():
    print "start to call a coroutine"
    #IOLoop.current().run_sync(lambda: coroutine_visit())
    IOLoop.current().spawn_callback(coroutine_visit)
    print 'end of call a coroutine'


if __name__ == '__main__':
    func_normal()