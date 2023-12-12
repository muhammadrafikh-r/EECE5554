#!/usr/bin/python3

from imu_driver.srv import EulerToQuaternion, EulerToQuaternionResponse
from geometry_msgs.msg import Quaternion
import rospy
import math
import numpy as np

def conversion_function(euler_angles):
    
    print('77777777777777777777777')
    # quat = Quaternion()
    r = euler_angles.euler_angles.x
    p = euler_angles.euler_angles.y
    y = euler_angles.euler_angles.z
    print('88888888888888888888')
    quat = Quaternion()
    # quat.w = (math.cos(req.euler_angles.x/2) * math.cos(req.euler_angles.y/2) * math.cos(req.euler_angles.z/2)) + (math.sin(req.euler_angles.x/2) * math.sin(req.euler_angles.y/2) * math.sin(req.euler_angles.z/2))
    # quat.x = (math.sin(req.euler_angles.x/2) * math.cos(req.euler_angles.y/2) * math.cos(req.euler_angles.z/2)) - (math.cos(req.euler_angles.x/2) * math.sin(req.euler_angles.y/2) * math.sin(req.euler_angles.z/2))
    # quat.y = (math.cos(req.euler_angles.x/2) * math.sin(req.euler_angles.y/2) * math.cos(req.euler_angles.z/2)) + (math.sin(req.euler_angles.x/2) * math.cos(req.euler_angles.y/2) * math.sin(req.euler_angles.z/2))
    # quat.z = (math.cos(req.euler_angles.x/2) * math.cos(req.euler_angles.y/2) * math.sin(req.euler_angles.z/2)) - (math.sin(req.euler_angles.x/2) * math.sin(req.euler_angles.y/2) * math.cos(req.euler_angles.z/2))
    quat.x = (math.sin(r/2) * math.cos(p/2) * math.cos(y/2) - math.cos(r/2) * math.sin(p/2) * math.sin(y/2))
    quat.y = (math.cos(r/2) * math.sin(p/2) * math.cos(y/2) + math.sin(r/2) * math.cos(p/2) * math.sin(y/2))
    quat.z = (math.cos(r/2) * math.cos(p/2) * math.sin(y/2) - math.sin(r/2) * math.sin(p/2) * math.cos(y/2))
    quat.w = (math.cos(r/2) * math.cos(p/2) * math.cos(y/2) + math.sin(r/2) * math.sin(p/2) * math.sin(y/2))
    # quat = [qx, qy, qz, qw]
    return(EulerToQuaternionResponse(quat))

    # return(EulerToQuaternionResponse(quat))

def server_conversion():
    rospy.init_node("quaternion_conversion_server")
    s = rospy.Service("convert_to_quaternion", EulerToQuaternion, conversion_function)
    print("Service Initiated")
    rospy.spin()

if __name__ == '__main__':
    server_conversion()