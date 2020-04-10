1: Delete the build folder that is located here "catkin_ws/src/turtlebot3_simulations/moving_obstacles/worlds/"
2: cd catkin_ws/src/turtlebot3_simulations/moving_obstacles/worlds/
3: mkdir build
4: cd build
5: cmake ..
6: make
7:export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:~/catkin_ws/src/turtlebot3_simulations/moving_obstacles/worlds/build
8:roslaunch turtlebot3_gazebo turtlebot3_world.launch
