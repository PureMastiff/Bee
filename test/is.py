# coding=utf-8
import copy
import time
from tornado import gen
from tornado.httpclient import HTTPClient, AsyncHTTPClient

def cpoy():
#深copy 浅copy
    a = [11, 22, 33]
    b = a

    print(a==b)
    #True
    print(a is b)
    #True

    c = copy.deepcopy(a)

    print(a==b)
    #True
    print(a is b)
    #False


def ssync_visit():
    http_client = HTTPClient()
    response = http_client.fetch('http://www.baidu.com')# 阻塞，直到网站请求完成
    print(response.body)


def hendle_response(response):
    print '33333'
    print(response.body)


def async_visit():
    http_client = AsyncHTTPClient()
    print '11111'
    response = http_client.fetch('http://www.baidu.com',callback=hendle_response) # 非阻塞
    time.sleep(10)
    print '22222'


@gen.coroutine
def corout_visit():
    http_client = AsyncHTTPClient()
    print '11111'
    response = yield http_client.fetch("http://www.lanou3g.com")
    print '222222'
    print response.body


@gen.coroutine
def syn_visit():
    http_client = HTTPClient()
    print '访问中...'
    response = yield http_client.fetch("http://www.baidu.com")  # 阻塞,直到访问完成
    print response.body


@gen.coroutine
def syn_visits():
    print '访问前'
    yield syn_visit()
    print '访问后'



if __name__=='__main__':
    syn_visits()