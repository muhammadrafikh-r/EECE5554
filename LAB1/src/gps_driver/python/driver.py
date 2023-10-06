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

    float_longitude = str(longitude)
    float_latitude = str(latitude)
    
    #To check if the string consists of a decimal
    if '.' in float_longitude or '.' in float_latitude :

        #Split the string into integer and decimal parts
        long_integer_part, long_decimal_part = float_longitude.split('.')
        lat_integer_part, lat_decimal_part = float_latitude.split('.')
        
        #Extraction of first two digits and remaining digits
        lat_first_two_digits = lat_integer_part[:2]
        lat_remaining_digits = lat_integer_part[2:] + '.' + lat_decimal_part
        long_first_three_digits = long_integer_part[:3]
        long_remaining_digits = long_integer_part[3:] + '.' + long_decimal_part

        #Conversion of remaining digits to a float followed by division by 60
        long_remaining_float = float(long_remaining_digits) / 60
        lat_remaining_float = float(lat_remaining_digits) / 60

        #Summing up the divided value to the first two digits
        lat_result = float(lat_first_two_digits) + lat_remaining_float
        long_result = float(long_first_three_digits) + long_remaining_float

    return lat_result, long_result

def parse_gpgga(line):

    # Splitting the $GPGGA line into fields
    fields = line.split(',')

    # Check if the line has enough fields and starts with $GPGGA
    if fields[0] == "b'$GPGGA":

        try:
            time_stamp = float(fields[1])

            if fields[3] == 'N':
                latitude = float(fields[2])
            else:
                latitude = -float(fields[2])  

            if fields[5] == 'E':
                longitude = float(fields[4])
            else:
                longitude = -float(fields[4]) 

            utc = float(fields[1])  
            hdop = float(fields[8])   
            altitude = float(fields[9])
            
            latitude, longitude = conversion(latitude, longitude)

            #Conversion of latitude and longitude to UTM
            utm_coords = utm.from_latlon(latitude, longitude)
            utm_easting = utm_coords[0]   
            utm_northing = utm_coords[1]
            zone = utm_coords[2]
            letter = utm_coords[3]
        
            return time_stamp, latitude, longitude, altitude, utm_easting, utm_northing, zone, letter, utc, hdop
        
        except ValueError as e:

            print(f"Error parsing GPGGA data: {e}")
            return None

def my_gnss_puck_driver():

    rospy.init_node('my_gnss_puck_driver')

    my_serial_port = rospy.get_param('~port', '/dev/ttyUSB0')

    serial_baud = rospy.get_param('~baudrate', 4800)
    port = serial.Serial(my_serial_port, serial_baud, timeout=3.)
    rospy.logdebug("GNSS puck is on port " + my_serial_port + " at " + str(serial_baud))
    gps_pub = rospy.Publisher('/gps', gps_msg, queue_size=10)
    
    gps_data = gps_msg()
    gps_data.Header.frame_id = "GPS1_Frame"

    try:
        while not rospy.is_shutdown():

            line = port.readline().strip()
            line = str(line)

            if line.startswith("b'$GPGGA"):

                parsed_data = parse_gpgga(line)

                if parsed_data:

                    time_utc = str(parsed_data[0])
                    time_ros = float(time_utc[:2])*3600+float(time_utc[2:4])*60+float(time_utc[4:])
                    gps_data.Header.stamp = rospy.Time.from_sec(time_ros)
                    gps_data.Latitude = float(parsed_data[1])
                    gps_data.Longitude = float(parsed_data[2])
                    gps_data.Altitude = float(parsed_data[3])
                    gps_data.UTM_easting = float(parsed_data[4])
                    gps_data.UTM_northing = float(parsed_data[5])
                    gps_data.Zone = int(parsed_data[6])
                    gps_data.Letter = str(parsed_data[7])
                    gps_data.UTC = float(parsed_data[8])
                    gps_data.HDOP = float(parsed_data[9])
                    gps_pub.publish(gps_data)
                    print(gps_data)

    except rospy.ROSInterruptException:
        port.close()
    
    except serial.serialutil.SerialException:
        rospy.loginfo("Shutting down GNSS driver node...")

if __name__ == '__main__':

    try:
        my_gnss_puck_driver()

    except rospy.ROSInterruptException:
        pass