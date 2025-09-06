# Advanced Robotics - Project 1 Deliverable 2
This workspace includes the well-known ROS package `turtlesim` along with a custom package that enables the turtle to trace the letter **'N'** in honor of NC State.

## Dependencies
* Ros2 Jazzy
* python3

## Setup

1) Source Ros
    ```
    source /opt/ros/jazzy/setup.bash
    ```

2) Build
    ```
    cd ./drawN_ws
    colcon build
    ```

## How to Run
1) Source Package
    ```
    source ./src/setup.bash
    ```

2) Run Turtle Sim
    ```
    ros2 run turtlesim turtlesim_node
    ```

3) Run Custom Package
    ```
    ```