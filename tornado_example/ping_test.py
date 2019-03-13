# coding=utf-8

import subprocess
import threading


def ping(host):
    result = subprocess.call('ping -c2 {} &> /dev/null'.format(host), shell=True)
    if result == 0:
        print host
    else:
        print '{} down\n'.format(host)


if __name__ == '__main__':
    ips = ['10.1.240.{}'.format(i) for i in range(1,255)]
    for ip in ips:
        t = threading.Thread(target=ping, args=(ip,))
        t.start()