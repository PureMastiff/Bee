# coding=utf-8

import sys
sys.path.append('../')

import time
from hello import Hello, World, China, Zhejiang, Hangzhou
import Queue
import threading
import heapq
import os
import yaml
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

    @classmethod
    def run(self):
        global taskq, scheq
        print "执行队列的size:{}\n".format(taskq.qsize())
        while True:
            print "执行队列的大小：{}\n".format(taskq.qsize())
            task = taskq.get()
            print "{}消费了{}".format(self.name, task().name)
            print "-----执行任务{}-----开始\n".format(task().name)
            self.start_time = time.time()
            self.task = task
            TaskCheck.run(task)

            print "-----执行任务{}完成----\n".format(task().name)
            timestamp = time.time()+ task().interval
            scheq.push(Schedule(task, timestamp), timestamp)


class ThreadPool(object):
    threads = []
    number_threads = 0
    limit_thread_num = 0

    @classmethod
    def start_execute_threads(cls, number_threads):
        cls.number_threads = number_threads
        cls.limit_thread_num = number_threads/2.0
        # 创建几个执行队列线程
        for i in range(number_threads):
            cls.threads.append(PerformTask())

        for i in cls.threads:
            i.setDaemon(True)
            i.start()

    @classmethod
    def clean_threads(cls):
        cls.threads = []


class MonitorThreadPool(ThreadPool):
    dump_filepath = '/tmp/pending_tasks.yaml'
    continue_run = True
    pengding_tasks = set([])
    timeout_tasks = set([])
    check_pending_interval =5

    @classmethod
    def stop_loop(cls):
        cls.continue_run = False

    @classmethod
    def reset_flag(cls):
        cls.continue_run = True

    @classmethod
    def start_check_pending_task(cls):
        while cls.continue_run:
            try:
                now = time.time()
                pending_task = set([i.task for i in cls.threads if
                                    i.start_time and (now - i.start_time) > i.task.interval])
                to_timeout = set([])
                if pending_task != cls.pengding_tasks:
                    to_timeout = cls.pengding_tasks - pending_task
                cls.pengding_tasks = pending_task
                cls.timeout_tasks = to_timeout | cls.timeout_tasks

                if len(cls.pengding_tasks | cls.timeout_tasks) >= cls.limit_thread_num:

                    cls.record()
                    cls.send_event_to_forwarder()
            except Exception:
                print "check pending task failed"
            finally:
                time.sleep(cls.check_pending_interval)

    @classmethod
    def record(cls):
        source_data = {}
        if os.path.exists(cls.dump_filepath):
            with open(cls.dump_filepath, 'r') as outfile:
                source_data = yaml.load(outfile)
        if not source_data:
            source_data = {}

        for task in cls.pengding_tasks:
            if task.name not in source_data:
                source_data[task.name] = cls.init_data(task.name)
            source_data[task.name]['pending_time'] += 1
        for task in cls.timeout_tasks:
            if task.name not in source_data:
                source_data[task.name] = cls.init_data(task.name)
            source_data[task.name]['timeout_time'] += 1

        with open(cls.dump_filepath, 'w') as outfile:
            yaml.dump(source_data, outfile, default_flow_style=False)

    @classmethod
    def send_event_to_forwarder(cls):
        pass

    @classmethod
    def init_data(cls, name):
        return {
            'name': name,
            'pending_time': 0,
            'timeout_time': 0,
        }


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

    # for i in range(2):
    #     performtask = PerformTask()
    #     performtask.start()
    # threadnum = threading.active_count()
    # print "threadnum:{}".format(threadnum)

    ThreadPool.start_execute_threads(2)
    #PerformTask.start()

