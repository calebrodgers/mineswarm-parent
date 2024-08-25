import socket

UDP_PARENT_IP = "192.168.0.107"
UDP_PARENT_PORT = 50000

parent_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
parent_sock.bind((UDP_PARENT_IP, UDP_PARENT_PORT))

while True:
    data, addr = parent_sock.recvfrom(1024) # buffer size is 1024 bytes
    message = data.decode()
    if message[0].isdigit():
    	message_components = message.split(',')
    	print("== Received Mapping Message from a Child Platform ==")
    	print("Child Platform: {}".format(message_components[0]))
    	print("X Position: {}".format(float(message_components[1])))
    	print("Y Position: {}".format(float(message_components[2])))
    	print("Threat Detected: {}".format((bool(int(message_components[3])))))
    	print("====================================================\n")
    else:
    	print("====== Received Message from a Child Platform ======")
    	print(message)
    	print("====================================================\n")
