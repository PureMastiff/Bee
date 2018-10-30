# coding = utf-8

import os
import time
from os.path import realpath, dirname
from bee._common import execute
from bee.sort import sort_name
from bee.view import show


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

    def get_cwd(self):
        ROOT_DIR = dirname(realpath(__file__))
        return ROOT_DIR

    def filelist(self):
        #filelist = [{'1.py': [name='', size='',date='']}, {'2.py': [name='', size='',date='']}]
        cmd = "ls /Users/guogx/Downloads"
        ret = execute(cmd)
        ret = ret.strip().split('\n')
        return ret


if __name__ == '__main__':
    t = TidyUpDownload()
    #print t.s_time()
    flist = t.filelist()
    #print(flist)
    show(sort_name(flist))
