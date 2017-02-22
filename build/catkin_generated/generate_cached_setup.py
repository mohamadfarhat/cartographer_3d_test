# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in "/home/mohamad/catkin1_ws/devel_isolated/rtabmap_ros;/home/mohamad/catkin1_ws/devel_isolated/timestamp_tools;/home/mohamad/catkin1_ws/devel_isolated/hector_sensors_gazebo;/home/mohamad/catkin1_ws/devel_isolated/hector_gazebo_worlds;/home/mohamad/catkin1_ws/devel_isolated/hector_gazebo_thermal_camera;/home/mohamad/catkin1_ws/devel_isolated/hector_gazebo_plugins;/home/mohamad/catkin1_ws/devel_isolated/hector_gazebo;/home/mohamad/catkin1_ws/devel_isolated/gazebo_ros_pkgs;/home/mohamad/catkin1_ws/devel_isolated/gazebo_ros_control;/home/mohamad/catkin1_ws/devel_isolated/gazebo_ros;/home/mohamad/catkin1_ws/devel_isolated/gazebo_plugins;/home/mohamad/catkin1_ws/devel_isolated/gazebo_msgs;/home/mohamad/catkin1_ws/devel_isolated/freenect_stack;/home/mohamad/catkin1_ws/devel_isolated/freenect_launch;/home/mohamad/catkin1_ws/devel_isolated/freenect_camera;/home/mohamad/catkin1_ws/devel_isolated/driver_common;/home/mohamad/catkin1_ws/devel_isolated/driver_base;/home/mohamad/catkin1_ws/devel_isolated/depthimage_to_laserscan;/home/mohamad/catkin1_ws/devel;/home/mohamad/catkin_ws/install_isolated;/home/mohamad/mybot_ws/devel;/opt/ros/kinetic".split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/mohamad/Dokumente/catkin_ws/devel/env.sh')

output_filename = '/home/mohamad/Dokumente/catkin_ws/build/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
