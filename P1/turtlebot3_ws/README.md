1) To Build
* 
    ```
    colcon build
    ```

2) launch gazebo
* 
    ```
    ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
    ```

3) teleop control
* 
    ```
    ros2 run turtlebot3_teleop teleop_keyboard
    ```

4) run SLAM
* 
    ```
    ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
    ```

5) save map
* 
    ```
    ros2 run nav2_map_server map_saver_cli -f ./src/map
    ```

6) navigation
* 
    ```
    ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=./src/map.yaml
    ```
* estimate initial pose by clicking '2D Pose Estimate' button and clicking and dragging
