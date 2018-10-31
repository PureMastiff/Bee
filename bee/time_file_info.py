# coding=utf-8

import time
import os
import _common


def timestamp_to_time(timestamp):
    '''把时间戳转化为时间  2018-10-25 17:26:22 '''
    timestruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timestruct)


def get_file_access_time(file_path):
    '''Access访问时间, 获取文件的最近访问时间'''
    file_path = unicode(file_path, 'utf8')
    a_time = os.path.getatime(file_path)
    return timestamp_to_time(a_time)


def get_file_modify_time(file_path):
    '''Modify修改时间, 获取文件的最近修改时间'''
    file_path = unicode(file_path, 'utf8')
    m_time = os.path.getmtime(file_path)
    return timestamp_to_time(m_time)


def get_file_change_time(file_path):
    '''Change状态改动时间, 获取文件的最近状态改变时间'''
    file_path = unicode(file_path, 'utf8')
    c_time = os.path.getctime(file_path)
    return timestamp_to_time(c_time)


def get_file_size(name):
    cmd_fs = 'ls -lh | grep {}'.format(name)
    ret = _common.execute(cmd_fs).rstrip()
    if not ret:
        return 0
    ret = ret.split()
    return ret[4]


def main():
    r = get_file_access_time("view.py")
    print r

if __name__ == '__main__':
    main()
