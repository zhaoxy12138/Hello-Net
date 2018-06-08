#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from socket import *

#HOST ='172.24.56.210'
HOST ='192.168.186.136'

PORT = 12345

BUFFSIZE=2048

ADDR = (HOST,PORT)

tctimeClient = socket(AF_INET,SOCK_STREAM)

tctimeClient.connect(ADDR)

while True:
    data = input(">")
    if not data:
        break
    tctimeClient.send(data.encode())
    data = tctimeClient.recv(BUFFSIZE).decode()
    if not data:
        break
    print(data)
tctimeClient.close()
