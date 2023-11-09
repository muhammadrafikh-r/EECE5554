#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import serial
from imu_driver.msg import imu_msg
from imu_driver.srv import EulerToQuaternion, EulerToQuaternionRequest, EulerToQuaternionResponse
import numpy as np

def toquat(r,p,y):
	qx = np.sin(r/2) * np.cos(p/2) * np.cos(y/2) - np.cos(r/2) * np.sin(p/2) * np.sin(y/2)
	qy = np.cos(r/2) * np.sin(p/2) * np.cos(y/2) + np.sin(r/2) * np.cos(p/2) * np.sin(y/2)
	qz = np.cos(r/2) * np.cos(p/2) * np.sin(y/2) - np.sin(r/2) * np.sin(p/2) * np.cos(y/2)
	qw = np.cos(r/2) * np.cos(p/2) * np.cos(y/2) + np.sin(r/2) * np.sin(p/2) * np.sin(y/2)
	return (qx,qy,qz,qw)

def convert_to_quaternion(r,p,y):
    qx, qy, qz, qw = toquat(r, p, y)
    return EulerToQuaternionResponse(qx, qy, qz, qw)

def convert_to_quaternion_server():
    #rospy.init_node('convert_to_quaternion_server')
    s = rospy.Service('convert_to_quaternion', EulerToQuaternion, convert_to_quaternion)
    #print("Ready to add two ints.")
    #rospy.spin()

if __name__ == '__main__':

    # prtv=rospy.get_param('imu_driver/port', '/dev/ttyUSB0')
    rospy.init_node('imu_driver') 
   
    pub = rospy.Publisher('imu', imu_msg, queue_size=5)    
    rospy.loginfo("Publishing IMU and MagField Data")

    #Initializing the conversion server
    convert_to_quaternion_server() 
    # rospy.wait_for_service('convert_to_quaternion')
    # eulertoquat = rospy.ServiceProxy('convert_to_quaternion', EulerToQuaternion)

    if len(sys.argv) > 0:
        rospy.loginfo(sys.argv[0])
        port_param = rospy.get_param('imu_driver/port', sys.argv[1])
    else:
        port_param = rospy.get_param('imu_driver/port', '/dev/ttyUSB0')

    # port_param = rospy.get_param('imu_driver/port', '/dev/ttyUSB0')
    port = serial.Serial(port_param, 115200, timeout=3.)
    port.write(b"VNWRG,07,40*XX")
    
    imu_parsed = imu_msg()
    imu_parsed.Header.frame_id="IMU1_FRAME"
    imu_parsed.Header.seq=0
    imu_parsed.IMU.header.frame_id="IMU1_FRAME"
    imu_parsed.MagField.header.frame_id="IMU1_FRAME"
    
    
    sleep_time = 0.25;
   
    try:
        while not rospy.is_shutdown():
            line = port.readline().decode().strip()

            if line.split(',')[0] == "$VNYMR":                
                try: 
                    yprmag = line.split(',')
                    imu_parsed.Header.stamp=rospy.Time.now()
                    imu_parsed.IMU.header.stamp=rospy.Time.now()
                    imu_parsed.MagField.header.stamp=rospy.Time.now()
                    imu_parsed.IMU.header.seq=imu_parsed.Header.seq
                    imu_parsed.MagField.header.seq=imu_parsed.Header.seq

                    # rospy.wait_for_service('convert_to_quaternion')
                    # quaternions = rospy.ServiceProxy('convert_to_quaternion', AddTwoInts)

                    req = EulerToQuaternionRequest()
                    req.roll = float(yprmag[3])
                    req.pitch = float(yprmag[2])
                    req.yaw = float(yprmag[1])

                    response = convert_to_quaternion(req)
                    # (qqx,qqy,qqz,qqw)=convert_to_quaternion(float(yprmag[3]),float(yprmag[2]),float(yprmag[1]))
                    imu_parsed.IMU.orientation.x=response.x
                    imu_parsed.IMU.orientation.y=response.y
                    imu_parsed.IMU.orientation.z=response.z
                    imu_parsed.IMU.orientation.w=response.w

                    imu_parsed.IMU.linear_acceleration.x=float(yprmag[7])
                    imu_parsed.IMU.linear_acceleration.y=float(yprmag[8])
                    imu_parsed.IMU.linear_acceleration.z=float(yprmag[9])

                    imu_parsed.IMU.angular_velocity.x=float(yprmag[10])
                    imu_parsed.IMU.angular_velocity.y=float(yprmag[11])
                    imu_parsed.IMU.angular_velocity.z=float(yprmag[12][0:-3])

                    imu_parsed.MagField.magnetic_field.x=float(yprmag[4])
                    imu_parsed.MagField.magnetic_field.y=float(yprmag[5])
                    imu_parsed.MagField.magnetic_field.z=float(yprmag[6])

                    imu_parsed.raw=line

                except: 
                    rospy.logwarn("Data exception: "+line)
                    continue
            pub.publish(imu_parsed)
        rospy.sleep(sleep_time)
            
    except rospy.ROSInterruptException:
        port.close()
    
    except serial.serialutil.SerialException:
        rospy.loginfo("Shutting down imu driver node...")