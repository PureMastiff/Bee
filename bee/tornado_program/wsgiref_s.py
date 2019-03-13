# coding=utf-8


from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 ok', [('content-Type', 'text/html')])
    return '<b>hello, world! </b>'


server = make_server('127.0.0.1', 8080, application)

server.serve_forever()