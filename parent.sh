#!/bin/bash

source /opt/ros/humble/setup.bash;
source ~/Desktop/mineswarm-parent/ros2_ws/install/setup.bash;
sudo chmod 777 /dev/ttyUSB0;
ros2 launch sllidar_ros2 sllidar_a1_launch.py & (source /opt/ros/humble/setup.bash; source ~/Desktop/mineswarm-parent/ros2_ws/install/setup.bash; ros2 launch ugv02_cartographer cartographer.launch.py) & ros2 run communication_module ugv02_control
