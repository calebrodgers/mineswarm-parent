from gpiozero import AngularServo
import sys
import serial
import json
import time
import math
import socket

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

# Define a function to deploy a child robot
def deployChild(childRobotID, x, y):
    print(f"Deploying child robot {childRobotID} to relative location ({x}, {y})")
    if childRobotID == 1:
    	#child1_sock.sendto(b"2", (UDP_CHILD1_IP, UDP_CHILD1_PORT))
    	#time.sleep(1)
    	child1_sock.sendto(b"0.4,0.6", (UDP_CHILD1_IP, UDP_CHILD1_PORT))
    if childRobotID == 2:
    	#child1_sock.sendto(b"2", (UDP_CHILD2_IP, UDP_CHILD2_PORT))
    	#time.sleep(1)
    	child1_sock.sendto(b"0.4,0.6", (UDP_CHILD2_IP, UDP_CHILD2_PORT))
    if childRobotID == 3:
    	#child1_sock.sendto(b"2", (UDP_CHILD3_IP, UDP_CHILD3_PORT))
    	#time.sleep(1)
    	child1_sock.sendto(b"0.4,0.6", (UDP_CHILD3_IP, UDP_CHILD3_PORT))
    if childRobotID == 4:
    	#child1_sock.sendto(b"2", (UDP_CHILD4_IP, UDP_CHILD4_PORT))
    	#time.sleep(1)
    	child1_sock.sendto(b"0.4,0.6", (UDP_CHILD4_IP, UDP_CHILD4_PORT))

# Define a function to drive the main robot
def driveMainRobot(x, y):
    print(f"Driving main robot to location ({x}, {y})")

# Divide the main area into smaller segments
def divide_area(main_area_x, main_area_y, num_child_robots):
    segment_width = main_area_x // 2
    segment_height = main_area_y // 2
    
    segments = []
    for i in range(2):
        for j in range(2):
            segment_x = i * segment_width
            segment_y = j * segment_height
            segments.append((segment_x, segment_y, segment_width, segment_height))
    
    return segments

# Main function to deploy child robots to cover the entire area
def deploy_child_robots_to_search_area(main_area_x, main_area_y, num_child_robots):
    segments = divide_area(main_area_x, main_area_y, num_child_robots)
    
    for i, (seg_x, seg_y, seg_width, seg_height) in enumerate(segments):
        # Drive main robot to the starting position of the segment
        driveMainRobot(seg_x, seg_y)
        
        # Deploy the child robot to cover this segment
        deployChild(i, seg_width, seg_height)

#deploy_child_robots_to_search_area(sys.argv[1], sys.argv[2], num_child_robots)

deployChild(1, 1, 1)