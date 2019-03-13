# coding=utf-8

"""
目的： 处理命令行参数，可以--help
两种方法；
1. sys.argv()
2.python的argparse 包

"""

import sys
import os
import argparse


# 使用sys.argv
def method1():
    word = sys.argv[1]
    if word == '--help' or word == '-h':
        print """
        --help or -h: display the help
        --where: find where is argvpy.py  
        --num: get file num
        """
    elif word == 'where':
        print os.getcwd()
    elif word == 'num':
        print 3


# 使用 argparse
def argparseMethod():
    parse = argparse.ArgumentParser()
    parse.add_argument('echo')
    parse.add_argument('--verbosity', '-v')
    args = parse.parse_args()
    if args.echo:
        print args.echo
    elif args.verbosity:
        print 'verbosity is ****'





if __name__ == "__main__":
    #method1()
    argparseMethod()