# coding: utf-8

import os
import sys
import platform
import subprocess
from collections import namedtuple
from itertools import izip

# =================================================================
# --- OS constants
# =================================================================

POSIX = os.name == "posix"
WINDOWS = os.name == "nt"
LINUX = sys.platform.startswith("linux")
AIX = sys.platform.startswith("aix")
DARWIN = sys.platform.startswith("darwin")


# =================================================================
# --- Info
# =================================================================

# networkinfo()
s_networkinfo = namedtuple('s_networkinfo',
                          ['name', 'mac', 'ip', 'type', 'broadcast', 'netmask'])
#info=[]
#info.append(s_networkinfo(
    # name=name, mac=mac, ipv4=ipv4, ipv6=ipv6s[0],netmask=netmask))


# =================================================================
# --- slots classes
# =================================================================
class SlotBase(object):
    def __init__(self, *args, **kwargs):
        setted = set()
        kwargs_ = dict(izip(self.__slots__, args))
        kwargs_.update(kwargs)
        for key, value in kwargs_.iteritems():
            setattr(self, key, value)
            setted.add(key)
        for key in set(self.__slots__) - setted:
            setattr(self, key, None)

    def __str__(self):
        attrs = ', '.join('{}={!r}'.format(name, getattr(self, name)) for name in self.__slots__)
        return '<{} {}>'.format(self.__class__.__name__, attrs)


class snetworkinfo():
    __slots__ = ('name', 'mac', 'ip', 'type', 'broadcast', 'netmask')


# =================================================================
# --- Exceptions
# =================================================================

class ExecuteError(Exception):
    def __init__(self, returncode, cmd, reason=''):
        self.returncode = returncode
        super(ExecuteError,
              self).__init__('\nWhen executing cmd: {} occurs an error!\n'
                             'Reason: {}'.format(cmd, reason))


# =================================================================
# --- utils
# =================================================================


def os_what():
    ''' 获取系统平台'''
    return platform.platform()


def execute(cmd, env=None):
    p = subprocess.Popen(
        cmd, shell=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    returncode = p.poll()
    if returncode == 0:
        return stdout
    else:
        raise ExecuteError(returncode, cmd, reason=stderr)


def main():
    name = os_what()
    print name
    cmd_str = 'ls -l'
    r = execute(cmd_str)
    print r


if __name__ == '__main__':
    main()




# coding: utf-8

import os
import sys
import platform
import subprocess
from collections import namedtuple
from itertools import izip
import ConfigParser
# =================================================================
# --- OS constants
# =================================================================

POSIX = os.name == "posix"
WINDOWS = os.name == "nt"
LINUX = sys.platform.startswith("linux")
AIX = sys.platform.startswith("aix")
DARWIN = sys.platform.startswith("darwin")


# =================================================================
# --- Info
# =================================================================

# networkinfo()
s_networkinfo = namedtuple('s_networkinfo',
                          ['name', 'mac', 'ip', 'type', 'broadcast', 'netmask'])
#info=[]
#info.append(s_networkinfo(
    # name=name, mac=mac, ipv4=ipv4, ipv6=ipv6s[0],netmask=netmask))


# =================================================================
# --- slots classes
# =================================================================
class SlotBase(object):
    def __init__(self, *args, **kwargs):
        setted = set()
        kwargs_ = dict(izip(self.__slots__, args))
        kwargs_.update(kwargs)
        for key, value in kwargs_.iteritems():
            setattr(self, key, value)
            setted.add(key)
        for key in set(self.__slots__) - setted:
            setattr(self, key, None)

    def __str__(self):
        attrs = ', '.join('{}={!r}'.format(name, getattr(self, name)) for name in self.__slots__)
        return '<{} {}>'.format(self.__class__.__name__, attrs)


class snetworkinfo():
    __slots__ = ('name', 'mac', 'ip', 'type', 'broadcast', 'netmask')


# =================================================================
# --- Exceptions
# =================================================================

class ExecuteError(Exception):
    def __init__(self, returncode, cmd, reason=''):
        self.returncode = returncode
        super(ExecuteError,
              self).__init__('\nWhen executing cmd: {} occurs an error!\n'
                             'Reason: {}'.format(cmd, reason))


# =================================================================
# --- utils
# =================================================================


def os_what():
    ''' 获取系统平台'''
    return platform.platform()


def execute(cmd, env=None):
    p = subprocess.Popen(
        cmd, shell=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    returncode = p.poll()
    if returncode == 0:
        return stdout
    else:
        raise ExecuteError(returncode, cmd, reason=stderr)


def main():
    name = os_what()
    print name
    cmd_str = 'ls -l'
    r = execute(cmd_str)
    print r


if __name__ == '__main__':
    main()