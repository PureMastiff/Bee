# coding=utf-8

import time
import logging
import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write('hello, world')
        self.finish()


class NoBlockingHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(10)
        self.write('Blocking Request')


class BlockingHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(10)
        self.write('Blocking Request')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/block", BlockingHandler),
        (r"/noblock", NoBlockingHandler),
    ], autoreload=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
