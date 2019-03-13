# coding: utf-8
import os
import re
import sys
import platform
from configer import Configer

from collections import namedtuple
from semver import Spec, Version
from subprocess import check_output, CalledProcessError


__version__ = '0.4.4'


Platform = namedtuple('Platform',
                      ['system', 'dist', 'version', 'cpu', 'kernel'])


class NotMatchError(Exception):
    pass


_platform = None
PLATFORM_SEP = '@'
LINUX_DIST_MAP = {
    'centos': 'CentOS',
    'ubuntu': 'Ubuntu',
    'debian': 'Debian',
    'fedora': 'Fedora',
    'redhat': 'RedHat',
    'oracle': 'Oracle',
    'redflag': 'RedFlag'
}
OS_RELEASE = '/etc/os-release'
REDHAT_RELEASE = '/etc/redhat-release'
NEOKYLIN_RELEASE = '/etc/neokylin-release'
NEOSHINE_RELEASE = '/etc/neoshine-release'
REDFLAG_RELEASE = '/etc/redflag-release'


def get_platform():
    """
    获取平台信息，返回命名元组，包含如下信息：
        system: 系统大类，如 Windows, Linux, UNIX等
        dist: 发行版，如 Windows, CentOS, Ubuntu, Debian, Fedora, RedHat, SUSE, FreeBSD, Oracle, Amazon等
        version: 具体的版本号, Windows如2003、2008、2012、2016， CentOS如7.2.1511
        cpu: 处理器架构，32或者64
        kernel: 内核版本号，Windows下如10.0.14393， CentOS下如3.10.0
    """
    global _platform
    if _platform is not None:
        return _platform

    version = kernel = ''
    uname = platform.uname()
    system = uname[0]
    cpu = get_bits()

    if system == 'Windows':
        dist = 'Windows'
        kernel = uname[3]
        found_versions = re.findall('(\d+)', uname[2])
        if found_versions:
            version = found_versions[0]

    elif system == 'Linux':
        version = platform.linux_distribution()[1]
        platform_str = platform.platform().strip().lower()
        kernel = platform_str.split('-')[1]
        found_dists = re.findall(
            'with-(centos|ubuntu|debian|fedora|redhat|oracle)-', platform_str)

        if found_dists:
            lower_dist = found_dists[0]
            dist = LINUX_DIST_MAP[lower_dist]

            # 针对中标麒麟
            if os.path.exists(NEOKYLIN_RELEASE):
                dist = 'NeoKylin'
                version = _neokylin_version()
            # 针对中标普华
            elif os.path.exists(NEOSHINE_RELEASE):
                dist = 'NeoShine'
                version = _neoshine_version()
            # 针对 RedHat 和 CentOS 发行版
            elif lower_dist == 'redhat' and os.path.exists(REDHAT_RELEASE):
                with open(REDHAT_RELEASE) as f:
                    if 'centos' in f.read().lower():
                        dist = LINUX_DIST_MAP['centos']
            # 针对 Ubuntu 发行版
            elif lower_dist in ('ubuntu', 'debian') and os.path.exists(OS_RELEASE):
                configer = Configer(OS_RELEASE, content_format=Configer.EQUAL)
                found_versions = re.findall('(\d+\.*\d*\.*\d*)',
                                            configer.get('VERSION'))
                if found_versions:
                    version = found_versions[0]

                dist_id = configer.get('ID', 'debian').lower()
                dist = 'Ubuntu' if 'ubuntu' in dist_id else 'Debian'
        else:
            # 针对 openSUSE 和 SUSE 发行版
            dist = platform.linux_distribution()[0]
            if 'opensuse' in dist.lower():
                dist = 'openSUSE'
            elif 'suse' in dist.lower():
                dist = 'SUSE'
            # 针对 Amazon 发行版
            elif 'amzn' in platform_str:
                dist = 'Amazon'
                if os.path.exists(OS_RELEASE):
                    configer = Configer(OS_RELEASE,
                                        content_format=Configer.EQUAL)
                    version = configer.get('VERSION')
            # 针对 NeoKylin（中标麒麟）
            elif os.path.exists(NEOKYLIN_RELEASE):
                dist = 'NeoKylin'
                version = _neokylin_version(platform_str)
            # 针对中标普华
            elif os.path.exists(NEOSHINE_RELEASE):
                dist = 'NeoShine'
                version = _neoshine_version()
            # 针对RedFlag（红旗）
            elif os.path.exists(REDFLAG_RELEASE):
                dist = 'RedFlag'
                with open(REDFLAG_RELEASE) as f:
                    content = f.read()
                    found_versions = re.findall('(\d+\.*\d*\.*\d*)', content)
                    if found_versions:
                        version = found_versions[0]

    elif system in ('FreeBSD', 'Darwin'):
        dist = system
        system = 'UNIX'
        version = platform.platform().strip().split('-')[1]

    elif system == 'AIX':
        dist = system
        system = 'UNIX'
        version = '.'.join(platform.uname()[3:1:-1])

    else:
        dist = system
        system = 'Linux'
        version = platform.version()

    version = to_semantic_version(version)
    kernel = to_semantic_version(kernel)

    return Platform(system, dist, version, cpu, kernel)


def _neokylin_version(platform_str=None):
    return _neo_version(platform_str, NEOKYLIN_RELEASE)


def _neoshine_version():
    return _neo_version(None, NEOSHINE_RELEASE)


def _neo_version(platform_str, release):
    if platform_str:
        version = platform_str.split('-')[-2]
        if version and not version[0].isdigit():
            version = ''
    else:
        version = ''

    if not version:
        with open(release) as f:
            content = f.read()
            found_versions = re.findall('(\d+\.*\d*\.*\d*)', content)
            if found_versions:
                version = found_versions[0]
    return version


def get_bits():
    if os.name == 'nt':
        try:
            from win32com.client import GetObject
            wmi = GetObject('winmgmts:/root/cimv2')
            raw_bits = wmi.execquery('select * from Win32_ComputerSystem')[0].SystemType
        except ImportError:
            raw_bits = check_output('echo %PROCESSOR_ARCHITECTURE%', shell=True)
        if 'x86' in raw_bits.lower():
            bits = 32
        else:
            bits = 64
    elif sys.platform.startswith("aix"):
        bits = check_output('bootinfo -K', shell=True)
    else:
        bits = check_output('getconf LONG_BIT', shell=True)
    try:
        bits = int(bits)
    except ValueError:
        bits = 64
    return bits


def to_semantic_version(version):
    version = version.strip('.') or '0'
    nums = version.split('.')
    nums_length = len(nums)
    if nums_length < 3:
        version += '.0' * (3 - nums_length)
    else:
        version = '.'.join(nums[:3])
    return version


def get_matched_platform_cpu(platforms=None):
    """
    给定的多个平台名称中，是否匹配当前平台
    platform_names是一个由如下形式组成的列表：
        Windows, Windows_10.0.14393, Windows_^10.0, Linux, CentOS_~6, AIX_^6.1
    """
    if not platforms:
        return '', ''

    cur_platform = get_platform()
    cur_version = Version(cur_platform.version)
    cur_kernel = Version(cur_platform.kernel)

    for platform_name, cpus in platforms.iteritems():
        if isinstance(cpus, (str, int)):
            cpus = [int(cpus)] if cpus.strip() else None
        cpus = cpus or [32, 64]

        # Check cpu
        if cur_platform.cpu not in cpus:
            continue

        # Check system
        system, version = split_platform(platform_name)
        if system in (cur_platform.system, cur_platform.dist):
            if not version:
                return platform_name, cur_platform.cpu
            elif (system == 'Windows' and Spec(version).match(cur_kernel)) or \
                    Spec(version).match(cur_version):
                return platform_name, cur_platform.cpu
    raise NotMatchError("Current {!r} doesn't match platform require: {!r}"
                        .format(cur_platform, platforms))


def split_platform(platform_name, sep=PLATFORM_SEP):
    version = None
    platform_name_split = platform_name.split(sep, 1)
    if len(platform_name_split) == 2:
        system, version = platform_name_split
    else:
        system = platform_name_split[0]
    return system, version
