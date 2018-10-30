# coding=utf-8
import os
import logging
from _common import execute

NAME_ADD = [".jpg", ".pdf", ".tgz", ".tar.gz", ".doc", ".egg" ]


def dir_or_file(path):
    if os.path.isdir(path):
        return True
    elif os.path.isfile(path):
        return False
    else:
        return -1


def getfilename(filename):
    '''获取文件的后缀名.doc .jpg .tgz'''
    ret = filename.split(".")
    if len(ret) > 1:
        return '.{}'.format(ret[len(ret) - 1])
    else:
        return "child-dir"


def sort_name(filelist):
    '''以类型进行排序输出
    filelist = ['1.py', '2.py', '3.doc', '4.pdf', '7.py']
    {'.doc': ['3.doc'], '.pdf': ['4.pdf'], '.py': ['1.py', '2.py', '7.py']}
    '''
    name_info = []
    s_nameinfo = {}
    for i in filelist:
        ret = getfilename(i)
        if ret in name_info:
            s_nameinfo[ret].append(i)
        else:
            name_info.append(ret)
            s_nameinfo[ret] = [i]
    return s_nameinfo


def getfilesize(filename):
    '''获取文件的大小'''
    pass


def sort_size(files):
    '''以文件大小进行排序输出'''
    pass


def getfiledate(filename):
    '''获取文件的创建日期'''
    pass


def sort_date(files):
    '''以日期不同进行排序出'''
    pass


if __name__ == '__main__':
    filelist = ['1.py', '2.py', '3.doc', '4.pdf', '7.py', '8', '9']
    sort_name(filelist)
