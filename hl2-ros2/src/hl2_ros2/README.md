First time init:
source /opt/ros/humble/setup.bash
cd ~/hl2_ros2/src
ros2 pkg create --build-type ament_python --node-name simple_remote_nav hl2_ros2


setup with:
ping 192.168.100.7
ros2 run hl2_ros2 simple_remote_nav
cd ~/hl2-ros2/src
source /opt/ros/humble/setup.bash
cd ..
colcon build --symlink-install --packages-select hl2_ros2
source install/local_setup.bash
ros2 run hl2_ros2 simple_remote_nav
