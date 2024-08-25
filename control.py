from gpiozero import AngularServo
import sys
import serial
import json
import time
import math
import socket
from adafruit_servokit import ServoKit

ser = serial.Serial('/dev/ttyS0',115200,timeout=1)

CHILD1_UP_ANGLE = 110
CHILD1_DOWN_ANGLE = 170
CHILD2_UP_ANGLE = 170
CHILD2_DOWN_ANGLE = 110
CHILD3_UP_ANGLE = 170
CHILD3_DOWN_ANGLE = 110
CHILD4_UP_ANGLE = 110
CHILD4_DOWN_ANGLE = 170

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

#kit = ServoKit(channels=16)
    
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
    	kit.servo[0].angle = CHILD1_DOWN_ANGLE
    	time.sleep(1)
    	#child1_sock.sendto(f"{x},{y}".encode('utf-8'), (UDP_CHILD1_IP, UDP_CHILD1_PORT))
    if childRobotID == 2:
    	kit.servo[1].angle = CHILD2_DOWN_ANGLE
    	time.sleep(1)
    	#child2_sock.sendto(f"{x},{y}".encode('utf-8'), (UDP_CHILD2_IP, UDP_CHILD2_PORT))
    if childRobotID == 3:
    	kit.servo[2].angle = CHILD2_DOWN_ANGLE
    	time.sleep(1)
    	#child3_sock.sendto(f"{x},{y}".encode('utf-8'), (UDP_CHILD3_IP, UDP_CHILD3_PORT))
    if childRobotID == 4:
    	kit.servo[4].angle = CHILD2_DOWN_ANGLE
    	time.sleep(1)
    	#child4_sock.sendto(f"{x},{y}".encode('utf-8'), (UDP_CHILD4_IP, UDP_CHILD4_PORT))

# Define a function to drive the main robot
def driveMainRobot(x, y):
	angle_time = abs(float(y)) / 50
	if float(sys.argv[1]) > 0:
	    data = {"T":1,"L":-0.1,"R":0.1}
	else:
	    data = {"T":1,"L":0.1,"R":-0.1}
	stop_data = {"T":1,"L":0.0,"R":0.0}
	json_data = json.dumps(data).encode("utf-8")
	json_stop_data = json.dumps(stop_data).encode("utf-8")
	print("turning")
	ser.write(json_data+ b'\n')
	print(angle_time)
	ser.write(json_data+ b'\n')
	time.sleep(angle_time)
	ser.write(json_stop_data+ b'\n')

	dist_time = float(x)

	print("driving")
	data = {"T":1,"L":-0.1,"R":-0.1}
	json_data = json.dumps(data).encode("utf-8")
	for i in range(math.floor(dist_time)):
	    ser.write(json_data+ b'\n')
	    time.sleep(1)
	time.sleep(dist_time-math.floor(dist_time))

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

deployChild(1, 0.4, 0.6)
#deployChild(2, 0.4, 0.4)
#deployChild(3, 0.4, 0.4)
#deployChild(4, 0.4, 0.4)
