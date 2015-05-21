from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSocket=socket(AF_INET,SOCK_DGRAM)
udpSerSocket.bind(ADDR)

while True:
    print 'waiting for message...'
    data,addr=udpSerSocket.recvfrom(BUFSIZ)
    udpSerSocket.sendto('[%s]%s'%(ctime(),data),addr)
    print '...receive from and return to:',addr

udpSerSocket.close()