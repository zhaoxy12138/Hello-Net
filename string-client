# -*- coding:utf-8 -*-
from socket import *

#HOST ='172.24.56.210'
HOST ='192.168.186.136' #虚拟机ip

PORT = 12345 #端口号

BUFFSIZE=2048 #传输的最大size

ADDR = (HOST,PORT) #地址

tctimeClient = socket(AF_INET,SOCK_STREAM) #AF_INET：ipv4
#SOCK_STERAM:type。Tcp连接，提供序列化的、可靠的、双向连接的字节流。

tctimeClient.connect(ADDR) #连接

while True:
    data = raw_input(">")
    if not data:
        break
    tctimeClient.send(data.encode())#向server发送数据
    data = tctimeClient.recv(BUFFSIZE).decode()  #server端接收的数据
    if not data:
        break
    print(data)
tctimeClient.close()
