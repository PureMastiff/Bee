# coding=utf-8

from socket import *
from time import ctime


def udp_server():
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    bindAddr = ('', 7788)
    udpSocket.bind(bindAddr)

    while True:
        recvData = udpSocket.recvfrom(1024)

        print('[{}] {}:{}'.format(ctime(), recvData[1][0], recvData[0]))
        if recvData[0] == "5d":
            print "ddddd"
        print('recvData:{}'.format(recvData))

    udpSocket.close()


def tcp_server():
    pass