cmake_minimum_required(VERSION 3.8)
project(two_wheel_robot)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  urdf
  config
  worlds
  launch
  DESTINATION share/${PROJECT_NAME}/
)

install(PROGRAMS
  src/waypoint_follower_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
