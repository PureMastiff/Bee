# coding=utf-8

import time
import unix as u
import win32 as w
import os
import sysutil
import sys
import socket
from pf import get_platform
import uptime
import uuid
from p_platform import Platform
from network import Network
from support_data import MYSQL_DATA, DISK_LINUX, DISK_WIN


class Data(object):
    def __init__(self):
        self.unix_system_data = {
            'io': u.IO(),
            'load': u.Load(),
            'memory': u.Memory(),
            'processes': u.Processes(),
            'cpu': u.Cpu(),
            'system': u.System()
        }

        self.win32_system_checks = {
            'io': w.IO(),
            'proc': '',
            'memory': w.Memory(),
            'network': w.Network(),
            'cpu': w.Cpu(),
            'system': w.System()
        }

        self.data = {
            "agentVersion": "3.0.1",
            "apiKey": "e10adc3949ba59abbe56e057f2gg88dd",
            "collection_timestamp": time.time(),
            "machine_type": self.get_machine_type(),
            "python": sys.version,
            "os": get_platform().dist,
            "system.uptime": uptime.uptime(),
            "uuid": ''.join(str(uuid.uuid1()).split('-')),
            "metrics": None,
            "events": {},
            "resources": {},
            "internalHostname": socket.gethostname(),
            "ip": self.get_ip(),
            "service_checks":[
                {"status": 0, "tags": ["check:ntp"], "timestamp": time.time(), "check": "datamonitor.agent.check_status", "host_name": "Hunz", "message": '', "id": 10},
                {"status": 0, "tags": ["check:disk"], "timestamp": time.time(), "check": "datamonitor.agent.check_status", "host_name": "Hunz", "message": '', "id": 11},
                {"status": 0, "tags": ["check:network"], "timestamp":time.time(), "check": "datamonitor.agent.check_status", "host_name": "Hunz", "message": '', "id": 12},
                {"status": 0, "tags": None, "timestamp": time.time(), "check": "datamonitor.agent.up", "host_name": "Hunz", "message": '', "id": 13}
            ],
        }

    def get_machine_type(self):
        return os.environ.get('ANT_NODE_TYPE') or sysutil.node_type()

    def get_ip(self):
        hostname = socket.gethostname()
        try:
            ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            ip = "10.1.100.31"
        return ip

    def run(self):
        metrics = []
        if Platform.is_windows():
            for key in ['memory', 'cpu', 'network', 'io', 'system']:
                try:
                    metrics.extend(self.win32_system_checks[key].check())
                except Exception:
                    print('Unable to fetch Windows system metrics.')
        else:
            for key in ['load', 'system', 'io', 'cpu']:
                try:
                    key_data = self.unix_system_data[key].check()
                    if key_data:
                        self.data.update(key_data)
                except Exception:
                    print('Unable to fetch Windows system metrics.')

            #processes = self.unix_system_data['processes'].check()
            # print processes
            # self.data.update(processes)

            memory = self.unix_system_data['memory'].check()
            if memory:
                memstats = {
                    'memPhysUsed': memory.get('physUsed'),
                    'memPhysPctUsage': memory.get('physPctUsage'),
                    'memPhysFree': memory.get('physFree'),
                    'memPhysTotal': memory.get('physTotal'),
                    'memPhysUsable': memory.get('physUsable'),
                    'memSwapUsed': memory.get('swapUsed'),
                    'memSwapFree': memory.get('swapFree'),
                    'memSwapPctFree': memory.get('swapPctFree'),
                    'memSwapTotal': memory.get('swapTotal'),
                    'memSwapPctUsage': memory.get('swapPctUsage'),
                    'memCached': memory.get('physCached'),
                    'memBuffers': memory.get('physBuffers'),
                    'memShared': memory.get('physShared'),
                    'memSlab': memory.get('physSlab'),
                    'memPageTables': memory.get('physPageTables'),
                    'memSwapCached': memory.get('swapCached')
                }
                self.data.update(memstats)
            metrics = DISK_DATA + MYSQL_DATA + Network().check()

        self.data["metrics"] = metrics
        return self.data


if __name__ == '__main__':
    d = Data()
    data = d.run()
    print data

