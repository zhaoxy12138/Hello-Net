# -*- coding: cp936 -*-

from socket import *

import struct

ADDR = ('',8000)

BUFSIZE = 1024

FILEINFO_SIZE=struct.calcsize('128sI') #初始化文件信息大小

recvSock = socket(AF_INET,SOCK_STREAM)#创建套接字

recvSock.bind(ADDR) #绑定ip与端口 

recvSock.listen(1) #开始监听
#参数指定tcpsever可以同时接受多少个客服端的连接申请，当超过此数时server将拒绝客户端的连接申请，给出socket.error: [Errno 10061]错误。
print "Waiting for connection..."

conn,addr = recvSock.accept()#接受TCP连接，并返回新的套接字与IP地址

print "connection finished",addr #输出地址

fhead = conn.recv(FILEINFO_SIZE)#收到从client端传来的文件名 和文件大小

filename,filesize=struct.unpack('128sI',fhead)#解包

print filename,len(filename),type(filename)  #输出

print filesize

filename = filename.strip('\00') #使用strip()删除打包时附加的多余空字符

fp = open(filename,'wb')#打开文件 如果不存在则创建

restsize = filesize #设置变量剩余大小 用于传输完成时跳出循环

print "Receiving files... ",

while 1:

    if restsize > BUFSIZE:  #每次接受bufsize个字节

        filedata = conn.recv(BUFSIZE) #接收bufsize个

    else:                   #剩下的

        filedata = conn.recv(restsize) #接收剩余的

    if not filedata: break

    fp.write(filedata)     #写进文件

    restsize = restsize-len(filedata) 

    if restsize == 0: #如果写完了 跳出循环

     break

print "Receiving Finished..."

fp.close()

conn.close()

recvSock.close()

print "Connection closed..."
