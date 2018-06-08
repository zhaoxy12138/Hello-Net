# -*- coding: cp936 -*-
from socket import *
import os
import struct
ADDR = ('192.168.186.136',8000)  #虚拟机ip
BUFSIZE = 1024   #以1024字节为传输单位
filename = raw_input('Please input file name...\r\n')
FILEINFO_SIZE=struct.calcsize('128sI') #初始化文件大小 128bytes Int
sendSock = socket(AF_INET,SOCK_STREAM)#定义套接字类型 ipv4 tcp
sendSock.connect(ADDR)  #连接
fhead=struct.pack('128sI',filename,os.stat(filename).st_size) #将值根据格式转化为字符串
#os.stat 用于在给定的路径上执行一个系统 stat 的调用 st_size:普通文件以字节为单位的大小
sendSock.send(fhead)  #发送文件信息
fp = open(filename,'rb') #打开文件
while 1:
    filedata = fp.read(BUFSIZE)  #每次读BUFSIZE个字节
    if not filedata: break
    sendSock.send(filedata) #发送数据
print "Sending successful..."
fp.close()  #关闭文件
sendSock.close() #关闭套接字
print "Connection closed..."
