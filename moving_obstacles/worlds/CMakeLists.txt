cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

add_library(ActorCollisionsPlugin SHARED ActorCollisionsPlugin.cc)
add_library(AttachModelPlugin SHARED AttachModelPlugin.cc)
add_library(TrajectoryActorPlugin SHARED TrajectoryActorPlugin.cc)
target_link_libraries(ActorCollisionsPlugin ${GAZEBO_LIBRARIES})
target_link_libraries(AttachModelPlugin ${GAZEBO_LIBRARIES})
target_link_libraries(TrajectoryActorPlugin ${GAZEBO_LIBRARIES})
