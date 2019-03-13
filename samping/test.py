# coding=utf-8
import heapq
from hello import Hello
from world import World
import time
import Queue
import threading

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priorprity):
        heapq.heappush(self._queue, (-priorprity, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)

    def get(self, heappop=heapq.heappush):
        return heappop(self._queue)


# 任务入优先级队列
taskq = PriorityQueue()
hello = Hello()
world = World()
timestamp = time.time()
hello = [hello, timestamp]
world = [world, timestamp+15]
taskq.push(hello, 8)
taskq.push(world, 9)
taskq.push(world, -1)
taskq.push(world, -5)
#taskq.push(network, 10)
taskq.push(hello, 11)
taskq.push(hello, 15)


# 执行任务入先入先出队列
qnum = Queue.LifoQueue()
while taskq.qsize():
    a = taskq.pop()
    if a[1] < time.time():
        qnum.put(a[0])

def perform(task):
    return task.check()

while qnum.qsize():
    q = qnum.get()
    print perform(q)


class Threadnum(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            num = self.queue.get()

            self.queue.task_done()




def main():
    #产生一个threads pool 并把消息传递给thread函数处理
    for i in range(5):
        t = Threadnum(q)
        t.setDaemon(True)
        t.start()

    #往队列中添加

#创建线程池


