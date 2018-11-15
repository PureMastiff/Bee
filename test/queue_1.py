# coding=utf-8

import threading
import time
from Queue import Queue


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize():
                pass
