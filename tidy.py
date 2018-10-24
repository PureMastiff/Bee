# coding = utf-8

import os
import time
from bee._common import execute


SMALL = "<5M"
MIDDLE = "5M<= x <= 50M"
BIG = ">50M"
filessize = {SMALL: [], MIDDLE: [], BIG: []}


class TidyUpDownload():
    def __init__(self):
        self.time = None

    def s_time(self):
        s_time = time.localtime(time.time())
        return time.asctime(s_time)

    def filelist(self):
        cmd = "ls -h"
        print "1111"
        r = execute(cmd)
        return r

if __name__ == '__main__':
    t = TidyUpDownload()
    print t.s_time()
    t.filelist()


