import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from visualization_msgs.msg import Marker

import math


import socket
import time

print('hi')

UDP_PARENT_IP = "192.168.0.107"
UDP_PARENT_PORT = 50000

UDP_CHILD_IP = "192.168.0.35"
UDP_CHILD_PORT = 1112

child_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

parent_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
parent_sock.bind((UDP_PARENT_IP, UDP_PARENT_PORT))



class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Marker, "visualization_marker1", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0
        self.id = 0

    def timer_callback(self, x, y):
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.header.stamp = self.get_clock().now().to_msg()

        # set shape, Arrow:child_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

parent_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
parent_sock.bind((UDP_PARENT_IP, UDP_PARENT_PORT)) 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
        marker.type = 3
        marker.id = self.id

        # Set the scale of the marker
        marker.scale.x = 0.15
        marker.scale.y = 0.15
        marker.scale.z = 0.01

        # Set the color
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
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
    
    minimal_publisher.timer_callback(0.0, 0.0)

    #rclpy.spin(minimal_publisher)
    
    print('listening for position')
    
    while True:
        data, addr = parent_sock.recvfrom(1024) # buffer size is 1024 bytes
        print(data.decode())
        orig_str = data.decode()
        numbers_str = orig_str.split('[')[1].split(']')[0]
        numbers_list = numbers_str.split(',')
        numbers = [float(num) for num in numbers_list]
        
        minimal_publisher.timer_callback(numbers[1]*1.5+0.2,numbers[0]*1.5)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
