# coding=utf-8

from socket import *
serSocket = socket(AF_INET, SOCK_DGRAM)


serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

localAddr = ('127.0.0.1', 7788)
serSocket.bind(localAddr)
serSocket.listen(5)

while True:
    print('----主进程，等待新客户端的到来----')
    newSocket, destAddr = serSocket.accept()
    print('----主进程，接下来负责数据处理[{}]----'.format(destAddr))

    try:
        while True:
            recvData = newSocket.recv(1024)
            if len(recvData)>0:
                print('recv[{}]:{}'.format(destAddr, recvData))
            else:
                print("[{}]客户端已经关闭".format(destAddr))
                break
    finally:
        newSocket.close()
serSocket.close()