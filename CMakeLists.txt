cmake_minimum_required(VERSION 2.8.3)
project(arduino_msgs)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs dynamic_reconfigure)

add_message_files(
  DIRECTORY msg
  FILES
  commands.msg
  states.msg
)
generate_messages(DEPENDENCIES std_msgs)

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## Generate dynamic reconfigure parameters in the 'cfg' folder
generate_dynamic_reconfigure_options(
  cfg/li3ds_arduino_settings.cfg
)

catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs dynamic_reconfigure
)
