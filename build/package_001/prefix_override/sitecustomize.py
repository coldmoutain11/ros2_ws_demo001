import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/martine/ROS2_study/ros2_ws_demo001/install/package_001'
