# coding=utf-8

import os
from tornado.httpclient import HTTPClient


def syn_visit():
    http_client = HTTPClient()
    response = http_client.fetch("http://www.baidu.com")
    print response.body


###

from tornado.httpclient import AsyncHTTPClient


def handle_response(response):
    #print response.body
    with open("/Users/guogx/git/Bee/bee/tornado_program/test.txt", 'w') as fp:
        fp.write(response.body)


def asyn_visit():
    http_client = AsyncHTTPClient()
    http_client.fetch("http://www.baidu.com", callback=handle_response)


if __name__ == '__main__':
    #syn_visit()
    asyn_visit()




