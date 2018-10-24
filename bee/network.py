# coding: utf-8
import psutil
from _common import s_networkinfo


def network_info():
    '''
    获取网卡的相关信息
    snic: subscriber network interface controller 用户网络接口控制器
    '''
    info = []

    ipv4s_infos = []
    ipv6s_infos = []

    for name, snics in psutil.net_if_addrs().items():
        name = name.lower()
        if 'loopback' in name or 'vmware' in name or 'virtual' in name or 'tunneling' in name:
            continue
        for snic in snics:
            if snic.family in (-1, 17, 18):
                mac = snic.address
            elif snic.family == 2:
                ipv4 = snic.address
                if ipv4 and ipv4.startswith(('169', '127.0.0.1')):
                    continue
                    ipv4s_infos.append((ipv4, snic.broadcast, snic.netmask))
            elif snic.family in (10, 23, 30):
                ipv6 = snic.address
                if ipv6 == '::1':
                    continue
                if ipv6 and '%' in ipv6:
                    ipv6 = ipv6.split('%')[0]
                ipv6s_infos.append((ipv6, snic.broadcast, snic.netmask))

        if not ipv4s_infos and not ipv6s_infos:
            continue

        if mac:
            mac = mac.upper()
        else:
            mac = ''

        for ipv4, netmask, broadcast in ipv4s_infos:
            #print ipv4, netmask, broadcast
            info.append(s_networkinfo(name=name, mac=mac, ip=ipv4, type='ipv4', broadcast=broadcast, netmask=netmask))
        #print ipv6s_infos
        for ipv6, netmask, broadcast in ipv6s_infos:
            info.append(s_networkinfo(name=name, mac=mac, ip=ipv6, type='ipv6', broadcast=broadcast, netmask=netmask))
    print info[1].name


def main():
    network_info()



if __name__ == '__main__':
    main()