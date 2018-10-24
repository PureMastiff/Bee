# coding: utf-8

import os
import platform


def os_what():
    return platform.platform()


def excute():
    pass


def main():
    name = os_what()
    print name


if __name__ == '__main__':
    main()