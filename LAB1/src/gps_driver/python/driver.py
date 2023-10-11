#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from std_msgs.msg import Header
from gps_driver.msg import gps_msg
import utm
import serial
import sys
import rospy

#Conversion of latitude and longitude from DDMM.SSS to DD format 
def conversion(latitude, longitude):

    str_longitude = str(longitude)
    str_latitude = str(latitude)
    
    if '.' in str_longitude or '.' in str_latitude :

        lat_int, lat_deci = str_latitude.split('.')
        long_int, long_deci = str_longitude.split('.')
 
        long_first_three_digits = long_int[:3]
        long_remaining_digits = long_int[3:] + '.' + long_deci

        lat_first_two_digits = lat_int[:2]
        lat_remaining_digits = lat_int[2:] + '.' + lat_deci

        latitude_res = float(lat_first_two_digits) + float(lat_remaining_digits) / 60
        longitude_res = float(long_first_three_digits) + float(long_remaining_digits) / 60

    return latitude_res, longitude_res

def parse(line):

    # Splitting the $GPGGA line into split_data
    split_data = line.split(',')

    # Check if the line has enough split_data and starts with $GPGGA
    if split_data[0] == "b'$GPGGA":

        try:
            ts = split_data[1]
            ts = float(ts)

            if split_data[5] == 'E':
                longitude = float(split_data[4])
            else:
                longitude = -float(split_data[4]) 

            if split_data[3] == 'N':
                latitude = float(split_data[2])
            else:
                latitude = -float(split_data[2])  

            utc = float(split_data[1])  
            hdop = float(split_data[8])   
            altitude = float(split_data[9])
            
            latitude, longitude = conversion(latitude, longitude)

            utm_coordinates = utm.from_latlon(latitude, longitude)
            utm_easting = utm_coordinates[0]   
            utm_northing = utm_coordinates[1]
            zone = utm_coordinates[2]
            letter = utm_coordinates[3]
        
            return ts, latitude, longitude, altitude, utm_easting, utm_northing, zone, letter, utc, hdop
        
        except ValueError as e:

            print(f"Error: parsing: {e}")
            return None

def puckDriver():
    
    rospy.init_node('puckDriver')

    gps_publisher = rospy.Publisher('/gps', gps_msg, queue_size=10)
    
    if len(sys.argv) > 0:
        rospy.loginfo(sys.argv[0])
        serial_port = rospy.get_param('~port', sys.argv[1])
    else:
        serial_port = rospy.get_param('~port', '/dev/ttyUSB0')

    serial_reception = rospy.get_param('~baudrate', 4800)
    port = serial.Serial(rospy.get_param('~port', '/dev/ttyUSB0'), serial_reception, timeout=3.)
    rospy.logdebug("GNSS Port Number" + rospy.get_param('~port', '/dev/ttyUSB0') + " at " + str(serial_reception))
  
    
    raw_gps_data = gps_msg()
    raw_gps_data.Header.frame_id = "GPS1_Frame"
    try:
        while not rospy.is_shutdown():

            line = str(port.readline().strip())


            if line.startswith("b'$GPGGA"):

                parsedD = parse(line)

                if parsedD:

                    raw_gps_data.Latitude = float(parsedD[1])
                    raw_gps_data.Longitude = float(parsedD[2])
                    raw_gps_data.Altitude = float(parsedD[3])
                    raw_gps_data.UTM_easting = float(parsedD[4])
                    raw_gps_data.UTM_northing = float(parsedD[5])
                    raw_gps_data.Zone = int(parsedD[6])
                    raw_gps_data.Letter = str(parsedD[7])
                    raw_gps_data.UTC = float(parsedD[8])
                    raw_gps_data.HDOP = float(parsedD[9])

                    utc_time = str(parsedD[0])
                    ros_time = float(utc_time[2:4])*60+float(utc_time[4:])+ float(utc_time[:2])*3600
                    raw_gps_data.Header.stamp = rospy.Time.from_sec(ros_time)
                    gps_publisher.publish(raw_gps_data)
                    
                    print(raw_gps_data)

    except rospy.ROSInterruptException:
        port.close()
    
    except serial.serialutil.SerialException:
        rospy.loginfo("Shutting down GNSS driver node...")

if __name__ == '__main__':

    try:
        puckDriver()

    except rospy.ROSInterruptException:
        pass