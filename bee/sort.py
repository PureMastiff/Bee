# coding=utf-8
import os
import logging
from _common import execute
from time_file_info import get_file_modify_time


def getfilename(filename):
    '''获取文件的后缀名.doc .jpg .tgz'''
    ret = filename.split(".")
    if len(ret) > 1:
        return '.{}'.format(ret[len(ret) - 1])
    else:
        return "child-dir"


def sort_name(filelist, path=None):
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


def get_file_size(file_path):
    '''获取文件的大小, 以"K"为单位'''
    file_path = unicode(file_path, 'utf8')
    fsize = os.path.getsize(file_path)
    return fsize/float(1024)


def sort_size(filelist, path):
    '''以文件大小进行排序输出'''
    size_info = []
    s_sizeinfo = {}
    for i in filelist:
        filepath = '{}/{}'.format(path, i)
        if os.path.isfile(filepath):
            ret = get_file_size(filepath)
            if ret <= 1024:
                r = '{}k'.format(ret)
                if 'small_0-1M' in size_info:
                    s_sizeinfo['small_0-1M'].append('{} {}'.format(i, r))
                else:
                    size_info.append('small_0-1M')
                    s_sizeinfo['small_0-1M'] = ['{} {}'.format(i, r)]

            elif 1024*5 > ret > 1024:
                r = '{}M'.format(ret/1024)
                if 'mid_1-5M' in size_info:
                    s_sizeinfo['mid_1-5M'].append('{} {}'.format(i, r))
                else:
                    size_info.append('mid_1-5M')
                    s_sizeinfo['mid_1-5M'] = ['{} {}'.format(i, r)]

            elif 1024*5 <= ret <= 1024*50:
                r = '{}M'.format(ret/1024)
                if 'big_5-50M' in size_info:
                    s_sizeinfo['big_5-50M'].append('name:{} size:{}'.format(i, r))
                else:
                    size_info.append('big_5-50M')
                    s_sizeinfo['big_5-50M'] = ['{} {}'.format(i, r)]

            elif 1024*50 < ret:
                r = '{}M'.format(ret/1024)
                if 'too-big>50M' in size_info:
                    s_sizeinfo['too-big>50M'].append('name:{} size:{}'.format(i, r))
                else:
                    size_info.append('too-big>50M')
                    s_sizeinfo['too-big>50M'] = ['{} {}'.format(i, r)]

        elif os.path.isdir(filepath):
            if 'dir' in size_info:
                s_sizeinfo['dir'].append(i)
            else:
                size_info.append('dir')
                s_sizeinfo['dir'] = [i]
        else:
            raise ('error')
    return s_sizeinfo


def getfiledate(filename, path):
    '''获取文件的创建日期'''
    filepath = '{}/{}'.format(path, filename)
    m_time = get_file_modify_time(filepath)
    return m_time


def sort_date(filelist, path):
    '''以日期不同进行排序出'''
    date_info = []
    s_dateinfo = {}
    for file in filelist:
        ret = getfiledate(file, path)
        date = ret.split(' ')[0]
        if date in date_info:
            s_dateinfo[date].append(file)
        else:
            date_info.append(date)
            s_dateinfo[date] = [file]
    return s_dateinfo


if __name__ == '__main__':
    filelist = ['1.py', '2.py', '3.doc', '4.pdf', '7.py', '8', '9']
    sort_size(filelist)
