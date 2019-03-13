# coding=utf-8

import re
import time
import uptime

try:
    import psutil
except ImportError:
    psutil = None

B2MB = float(1048576)
KB2MB = B2KB = float(1024)


class Memory():
    def __init__(self):
        self.collect_time = int(time.time())

    def check(self):
        total = 0
        free = 0
        mem = psutil.virtual_memory()
        total_visible_memory_size = mem.total / B2KB
        free_physical_memory = mem.available / B2KB
        if total_visible_memory_size is not None and free_physical_memory is not None:
            total = int(total_visible_memory_size) / KB2MB
            free = int(free_physical_memory) / KB2MB
        cache_bytes = 0
        committed_bytes = 0
        pool_paged_bytes = 0
        pool_non_paged_bytes = 0

        usable = free + cache_bytes
        if total > 0:
            pct_usable = float(usable) / total
            pct_usage = (1 - pct_usable) * 100

        pdh_check = [
            ['system.mem.free', int(time.time()), free, {}],
            ['system.mem.used',  int(time.time()), total - free, {}],
            ['system.mem.total',  int(time.time()), total, {}],
            ['system.mem.cached', int(time.time()), cache_bytes, {}],
            ['system.mem.committed',  int(time.time()), committed_bytes, {}],
            ['system.mem.paged',  int(time.time()), pool_paged_bytes, {}],
            ['system.mem.nonpaged', int(time.time()), pool_non_paged_bytes, {}],
            ['system.mem.usable',  int(time.time()), usable, {}],
            ['system.mem.pct_usage',  int(time.time()), pct_usage, {}],
        ]
        return pdh_check


class Cpu():
    def __init__(self):
        pass
        # print('system.cpu.user')
        # print('system.cpu.idle')
        # print('system.cpu.interrupt')
        # print('system.cpu.system')
        # print('system.cpu.pct_usage')

    def _check(self):
        cpu_percent = psutil.cpu_times_percent()
        #print cpu_percent
        cpu_check = [
            ['system.cpu.user', int(time.time()), cpu_percent.user, {}],
            ['system.cpu.idle', int(time.time()), cpu_percent.idle, {}],
            ['system.cpu.system', int(time.time()), cpu_percent.system, {}],
            ['system.cpu.pct_usage', int(time.time()), cpu_percent.system + cpu_percent.user, {}],
            ['system.cpu.interrupt', int(time.time()), cpu_percent.interrupt, {}]
        ]
        return cpu_check

    def check(self):
        try:
            return self._check()
        except Exception:
            print(
                '[windows system check] collect cpu info failed')
            return []


class Network():
    def __init__(self):
        # print('system.net.bytes_rcvd')
        # print('system.net.bytes_sent')
        pass

    def _check(self):
        tot_before = psutil.net_io_counters()
        time.sleep(1)
        tot_after = psutil.net_io_counters()
        bytes_received_per_sec = tot_after.bytes_recv - tot_before.bytes_recv
        bytes_sent_per_sec = tot_after.bytes_sent - tot_before.bytes_sent
        net_check = [
            ['system.net.bytes_sent', int(time.time()), bytes_sent_per_sec, {}],
            ['system.net.bytes_rcvd', int(time.time()), bytes_received_per_sec, {}]
        ]
        return net_check
    def check(self):
        try:
            return self._check()
        except Exception:
            print('[windows system check] collect network info failed')
            return []


class IO():
    def __init__(self):
        pass
    def check(self):
        io_check = [
            ['system.io.wkb_s', int(time.time()), 0, {}],
            ['system.io.w_s', int(time.time()), 0, {}],
            ['system.io.rkb_s', int(time.time()), 0, {}],
            ['system.io.r_s', int(time.time()), 0, {}],
            ['system.io.avg_q_sz', int(time.time()), 0, {}],
        ]
        return io_check


class System():
    def __init__(self):
        #print('system.uptime')
        pass

    def _check(self):
        sys_check = [
            ['system.uptime', int(time.time()), uptime.uptime(), {}]
        ]
        return sys_check

    def check(self):
        try:
            return self._check()
        except Exception:
            print(
                '[windows system check] collect system info failed')
            return []

if __name__ == '__main__':
    mem = Memory()
    print mem.check()

    cpu = Cpu()
    print cpu.check()

    net = Network()
    print net.check()

    io = IO()
    print io.check()

    system = System()
    print system.check()

