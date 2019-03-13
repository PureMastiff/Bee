# coding=utf-8

import time
import Queue as Q
import heapq
from network import Network
from hello import Hello
from world import World

'''每15s执行一次  注意写配置文件  不同的instance 有不同的执行间隔'''
INTERVAL = 15
"""记得数据类型校验"""

hello = Hello()
world = World()

schedules = [
    hello ,
    world
]


class Schedule(object):
    def __init__(self, priority, description, timestamp):
        self.priority = priority
        self.description = description
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return '(' + str(self.priority) + ', \'' + self.description + '\'' + \
               ', ' + str(self.timestamp) + ')'


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priorprity, timestamp):
        heapq.heappush(self._queue, (-priorprity, self._index, item, timestamp))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)

    def get(self, heappop=heapq.heappush):
        return heappop(self._queue)


def sendSchedule():
    for schedule in schedules:
        print(schedule)


def PriorityQueue_heapq():
    q = PriorityQueue()
    network = Network()
    hello = Hello()
    world = World()

    #q.push(network, 9)
    q.push(hello, 4, time.time())
    q.push(world, -1, time.time())

    while q.qsize():
        a = q.pop()
        print a.check()


def PriorityQueue_class():
    que = Q.PriorityQueue()
    que.put(Schedule(7, Network(), time.time()))
    que.put(Schedule(6, "mysql", time.time()))
    que.put(Schedule(1, 'disk', time.time()))
    que.put(Schedule(5, 'network', time.time()))
    print 'end'
    while not que.empty():
        q = que.get()
        print q
        print q.priority
        if q.description == "Network":
            network =  q.description+'()'
            network.check()
        print q.timestamp


if __name__ == '__main__':
    #PriorityQueue_class()
    #PriorityQueue_heapq()
    sendSchedule()