
from socket import *
from time import ctime

host = ''
port = 12345
buffsize = 2048
ADDR = (host,port)

tctime = socket(AF_INET,SOCK_STREAM) #ipv4 tcp
tctime.bind(ADDR) # #绑定需要监听的Ip和端口号
tctime.listen(3)

while True:
    print('Wait for connection ...')
    tctimeClient,addr = tctime.accept()
    print("Connection from :",addr) #输出client端的地址

    while True:
        data = tctimeClient.recv(buffsize).decode()  #收到client的字符串
        if not data:
            break
        tctimeClient.send(('[%s] %s' % (ctime(),data)).encode())  #传给client端时间和收到client的字符串
        print("ByeBye")  #做一个标记证明已执行完传回语句
    tctimeClient.close()
tctimeClient.close()
