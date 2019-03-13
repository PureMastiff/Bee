# coding=utf-8

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

sendAddr = ('127.0.0.1', 7788)

#sendData = raw_input("请输入：")
sedData = '5d'

udpSocket.sendto(sedData, sendAddr)


#recvData = udpSocket.recvfrom(1024)
#print (recvData)

udpSocket.close()