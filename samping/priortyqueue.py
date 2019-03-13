# coding=utf-8

import sys
sys.path.append('../')

import heapq
from hello import Hello
from world import World

from monitorpkg.network import Network


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priorprity):
        heapq.heappush(self._queue, (priorprity, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push([Hello, 0], 0)
    q.push([Hello, 5], 5)

    print q.qsize()
    print q.pop()
    print q.pop()

    p = Network()
    p.check()