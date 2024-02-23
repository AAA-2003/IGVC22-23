
**All code is designed to run on ROS Noetic on Ubuntu 20.04**


*LIDAR / Navigation* Usage:

BUILD:
1. Must have sick_scan_XD installed to work with LIDAR; follow instruction for "Build on Linux ROS1 here" https://github.com/SICKAG/sick_scan_xd/blob/master/INSTALL-ROS1.md#build-on-linux-ros1
2. Install Hector SLAM: sudo apt-get install ros-kinetic-hector-slam
3. Clone this 'catkin_ws' and build with 'catkin_make'

PACKAGE INFO:
- ranger_2dnav:  This package contains all the path-planning contents & the combined all–in-one
launch file called ranger_start.launch. It contains the ROS move_base launch, all required (and tunable) nav parameters, starts Hector SLAM, and the pyserial interface to connect an Arduino

- ranger_actionlib: This package starts the Action Server to send/receive feedback from the navigation path planner. It sends waypoints goals (capable of sending in a GPS coordinate frame as well -- NOT FULLY IMPLEMENTED) and can convert GPS frame coordinates to the local map frame.

- sabertooth_rospy: This package (specifically the CmdVelToMotors node) subscribes to the /cmd_vel topic and converts the velocity commands to differential wheel velocity inputs (based on robot geometry) and publishes this information in a special string format, which is received by a ROS subscriber on an Arduino.


*Camera - IN PROGRESS*

Running the code
(must have camera connected. This is for ROS Noetic)

```roscore
cd catkin_ws
source devel/setup.bash
rosloaunch pointcloud_to_lasercan ranger.launch```
```

*IMU PhidgetSpatial Precision 3/3/3* Usage:

BUILD:
1. Bind PhidgetUSB module with WSL: https://learn.microsoft.com/en-us/windows/wsl/connect-usb
2.Follow: https://github.com/ros-drivers/phidgets_drivers to get phidgets_drivers package installed
      Note: make sure to finish Udev Rules setup process
3. Reinstall package from ROS package index to fix nodelet error: 'sudo apt install ros-noetic-phidgets-spatial'
4. build wih 'catkin_make'

Usage:
- 'roslaunch phidgets_spatial/launch/spatial.launch' launches spatial node which publishes /imu/data (containing Imu message in ENU form)


