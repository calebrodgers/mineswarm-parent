import socket

UDP_PARENT_IP = "192.168.0.107"
UDP_PARENT_PORT = 50000

parent_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
parent_sock.bind((UDP_PARENT_IP, UDP_PARENT_PORT))

while True:
    data, addr = parent_sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data)
