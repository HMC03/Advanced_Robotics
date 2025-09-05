#!/bin/bash
# TurtleBot3 environment setup script

# Source ROS Jazzy installation
source /opt/ros/jazzy/setup.bash

# Source your TurtleBot3 workspace
source ./install/setup.bash

# Set the ROS domain ID (helps avoid network collisions)
export ROS_DOMAIN_ID=30 #TURTLEBOT3

export TURTLEBOT3_MODEL=waffle_pi