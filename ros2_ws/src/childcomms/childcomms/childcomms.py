import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from visualization_msgs.msg import Marker

import math

import socket
import time

X_SCALE = 5.0
Y_SCALE = 5.0

UDP_PARENT_IP = "192.168.0.107"
UDP_PARENT_PORT = 50000

parent_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
parent_sock.bind((UDP_PARENT_IP, UDP_PARENT_PORT))

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Marker, "visualization_marker", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0
        self.id = 0

    def timer_callback(self, x, y, threat):
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.header.stamp = self.get_clock().now().to_msg()

        # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
        marker.type = 3
        marker.id = self.id

        # Set the scale of the marker
        marker.scale.x = 0.15
        marker.scale.y = 0.15
        marker.scale.z = 0.01

        # Set the color
        marker.color.b = 0.0
        
        if threat:
        	marker.color.r = 1.0
        	marker.color.g = 0.0
        	marker.color.a = 0.5
        else:
        	marker.color.r = 0.0
        	marker.color.g = 1.0
        	marker.color.a = 0.2        	

        # Set the pose of the marker
        marker.pose.position.x = x
        marker.pose.position.y = y
        marker.pose.position.z = 0.0
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0
        self.publisher_.publish(marker)
        self.get_logger().info('Publishing')
        self.i += 1
        self.id += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    #minimal_publisher.timer_callback(0.0, 0.0, False)
    
    print('Listening to Child Platforms')
    
    
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
	    	minimal_publisher.timer_callback(float(message_components[1])*X_SCALE,float(message_components[2])*Y_SCALE, bool(int(message_components[3])))
	    else:
	    	print("====== Received Message from a Child Platform ======")
	    	print(message)
	    	print("====================================================\n")

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
