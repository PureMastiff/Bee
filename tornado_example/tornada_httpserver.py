# coding=utf-8

import time
from tornado import gen
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient

from tornado.ioloop import IOLoop

def handle_response(response):
    print response.body


@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch("http://www.baidu.com")
    print response.body


def asynchronous_visit():
    http_client = AsyncHTTPClient()
    http_client.fetch("http://www.baidu.com", callback=handle_response)


def synchronous_visit():
    http_client = HTTPClient()
    response = http_client.fetch("http://www.baidu.com")
    #print response.head
    print response.body

@gen.coroutine
def outer_coroutine():
    print "start call another coroutine"
    yield coroutine_visit()
    print "end of outer_coroutine"


def func_normal():
    print "start"
    #IOLoop.current().run_sync(lambda: coroutine_visit())
    IOLoop.current().spawn_callback(coroutine_visit)
    print "end"

if __name__ == '__main__':
    #synchronous_visit()
    #asynchronous_visit()
    func_normal()

