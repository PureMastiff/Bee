# coding=utf-8
import time

class Hello(object):
    def __init__(self):
        self.str = "hello world!"
        self.interval = 4
        self.name = "Hello"

    def check(self):
        return self.str


class World(object):
    def __init__(self):
        self.str = "world hello!"
        self.interval = 2
        self.name = "World"

    def check(self):
        return self.str


class China(object):
    def __init__(self):
        self.str = "hello China!"
        self.interval = 5
        self.name = "China"

    def check(self):
        return self.str


class Zhejiang(object):
    def __init__(self):
        self.str = "hello zhejiang!"
        self.interval = 0.5
        self.name = "Zhejiang"

    def check(self):
        return self.str


class Hangzhou(object):
    def __init__(self):
        self.str = "hello hangzhou!"
        self.interval = 10
        self.name = "Hangzhou"

    def check(self):
        time.sleep(20)
        return self.str