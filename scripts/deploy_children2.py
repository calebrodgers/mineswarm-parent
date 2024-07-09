import socket
import time
import sys

UDP_PARENT_IP = "192.168.0.107"
UDP_PARENT_PORT = 50000

UDP_CHILD1_IP = "192.168.0.15"
UDP_CHILD1_PORT = 1112

UDP_CHILD2_IP = "192.168.0.25"
UDP_CHILD2_PORT = 1112

UDP_CHILD3_IP = "192.168.0.35"
UDP_CHILD3_PORT = 1112

UDP_CHILD4_IP = "192.168.0.45"
UDP_CHILD4_PORT = 1112
    
child1_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

child2_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                     
child3_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                     
child4_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


parent_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
parent_sock.bind((UDP_PARENT_IP, UDP_PARENT_PORT))

if '1' in sys.argv:
    print('Deploying Child Platform 1')
if '2' in sys.argv:
    print('Deploying Child Platform 2')
if '3' in sys.argv:
    print('Deploying Child Platform 3')
if '4' in sys.argv:
    print('Deploying Child Platform 4')

if '1' in sys.argv:
    child1_sock.sendto(b"2", (UDP_CHILD1_IP, UDP_CHILD1_PORT))
if '2' in sys.argv:
    child2_sock.sendto(b"2", (UDP_CHILD2_IP, UDP_CHILD2_PORT))
if '3' in sys.argv:
    child3_sock.sendto(b"2", (UDP_CHILD3_IP, UDP_CHILD3_PORT))
if '4' in sys.argv:
    child4_sock.sendto(b"2", (UDP_CHILD4_IP, UDP_CHILD4_PORT))

time.sleep(1)

if '1' in sys.argv:
    child1_sock.sendto(b"0.4,0.6", (UDP_CHILD1_IP, UDP_CHILD1_PORT))
if '2' in sys.argv:
    child2_sock.sendto(b"-0.4,0.6", (UDP_CHILD2_IP, UDP_CHILD2_PORT))
if '3' in sys.argv:
    child3_sock.sendto(b"-0.4,0.6", (UDP_CHILD3_IP, UDP_CHILD3_PORT))
if '4' in sys.argv:
    child4_sock.sendto(b"0.4,0.6", (UDP_CHILD4_IP, UDP_CHILD4_PORT))

while True:
    data, addr = parent_sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data.decode())
