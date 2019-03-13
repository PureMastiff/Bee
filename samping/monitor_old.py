# coding=utf-8

import sys
sys.path.append('../')

import time
from hello import Hello, World, China, Zhejiang, Hangzhou
import Queue
import threading
import heapq
from monitorpkg.network import Network


#初始化任务列表
SCHEDULES_LIST = [
    Hello,
    World,
    China,
    Zhejiang,
    Hangzhou,
    Network
]


#优先级队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)


class Schedule(object):
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item


#添加任务
class DistributeTask(object):
    def __init__(self):
        pass

    @staticmethod
    def distribute_task(q, tasks, timestamp_priority=0):
        for task in tasks:
            q.push(Schedule(task, timestamp_priority), timestamp_priority)


# a = Schedule(0, Hello)
# hello = a.item
# print hello().check()
# print a.priority


#检查任务队列放入执行队列
class CheckSchedule(threading.Thread):
    def run(self):
        global scheq, taskq
        while True:
            print "-----每秒检查一次任务队列-----\n"
            print "任务队列长度：{}\n".format(scheq.qsize())
            while scheq.qsize():
                print "-----检查任务队列的每个元素\n"
                task = scheq.pop()
                print "task.pritity:{}\n".format(task.priority)
                if task.priority < time.time():
                    taskq.put(task.item)
                else:
                    scheq.push(task, task.priority)
                    break
            time.sleep(1)


class TaskCheck(object):
    def __init__(self):
        print "-----执行任务-----开始\n"
        self.start_time = None

    @classmethod
    def run(self, qtask):
        self.start_time = time.time()
        print self.start_time
        print qtask().check()


# 执行任务
class PerformTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start_time = 0
        self.task = None

    def run(self):
        global taskq, scheq
        print "执行队列的size:{}\n".format(taskq.qsize())
        while True:
            print "执行队列的大小：{}\n".format(taskq.qsize())
            q = taskq.get()
            print "{}消费了{}".format(self.name, q().name)
            print "-----执行任务{}-----开始\n".format(q().name)

            TaskCheck.run(q)
            sch_threads = []

            print "-----执行任务{}完成----\n".format(q().name)
            timestamp = time.time()+ q().interval
            scheq.push(Schedule(q, timestamp), timestamp)


class MonitorThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.threadEvent = event

    def run(self):
        pass


class ThreadPool(object):
    threads = []
    number_threads = 0
    limit_thread_num = 0

    def start_execute_threads(self, number_threads):
        self.number_threads = number_threads
        self.limit_thread_num = number_threads/2.0
        for i in range(number_threads):
            self.threads.append(PerformTask(name=str(i)))



class Forwarder(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


if __name__ == "__main__":
    # 任务队列：scheq  执行队列：taskq
    # 创建优先级队列 以"时间戳为优先级

    scheq = PriorityQueue()

    DistributeTask.distribute_task(scheq, SCHEDULES_LIST)

    # 执行队列
    taskq = Queue.Queue()

    for i in range(1):
        checksch = CheckSchedule()
        checksch.start()

    for i in range(2):
        performtask = PerformTask()
        performtask.start()
    threadnum = threading.active_count()
    print "threadnum:{}".format(threadnum)


