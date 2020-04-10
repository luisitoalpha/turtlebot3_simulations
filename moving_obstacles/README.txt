1: Delete the build folder that is located here "catkin_ws/src/turtlebot3_simulations/moving_obstacles/worlds/"
2: cd catkin_ws/src/turtlebot3_simulations/moving_obstacles/worlds/
3: mkdir build
4: cd build
5: cmake ..
6: make
7: echo 'export GAZEBO_PLUGIN_PATH=~/catkin_ws/src/turtlebot3_simulations/moving_obstacles/worlds/build:${GAZEBO_PLUGIN_PATH}' >> ~/.bashrc
8: source ~/.bashrc
9:roslaunch turtlebot3_gazebo turtlebot3_world.launch
