# coding = utf-8

import os
import time
from os.path import realpath, dirname
from bee._common import execute
from bee.sort import sort_name, sort_size, sort_date
from bee.view import show


class TidyUpDownload():
    def __init__(self):
        self.time = None

    def s_time(self):
        s_time = time.localtime(time.time())
        return time.asctime(s_time)

    def get_cwd(self):
        ROOT_DIR = dirname(realpath(__file__))
        return ROOT_DIR

    def filelist(self, dir):
        cmd = 'ls {}'.format(dir)
        #filelist = [{'1.py': [name='', size='',date='']}, {'2.py': [name='', size='',date='']}]
        ret = execute(cmd)
        ret = ret.strip().split('\n')
        return ret


if __name__ == '__main__':
    t = TidyUpDownload()
    PATH = "/Users/guogx/downloads"
    flist = t.filelist(PATH)
    tree_info = sort_date(flist, PATH)
    show(tree_info)
