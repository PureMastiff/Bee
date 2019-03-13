# coding=utf-8

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!!!!!!")


def make_app():
    return tornado.web.Application([('/', MainHandler)])


def main():
    app = make_app()
    app.listen('8888')
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()