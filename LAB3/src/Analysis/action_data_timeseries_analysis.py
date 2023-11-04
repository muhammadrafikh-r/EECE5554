import numpy as np
import bagpy
from bagpy import bagreader
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math

sns.set(style="whitegrid")

def quaternion_to_euler(x, y, z, w):
    euler_angles = []

    for i in range(len(x)):
        qx, qy, qz, qw = x[i], y[i], z[i], w[i]

        # Roll Calculation
        sinr_cosp = 2.0 * (qw * qx + qy * qz)
        cosr_cosp = 1.0 - 2.0 * (qx * qx + qy * qy)
        roll = math.degrees(math.atan2(sinr_cosp, cosr_cosp))

        # Pitch Calculation
        sinp = 2.0 * (qw * qy - qz * qx)
        if abs(sinp) >= 1:
            pitch = math.degrees(math.copysign(math.pi / 2, sinp))
        else:
            pitch = math.degrees(math.asin(sinp))

        # Yaw Calculation
        siny_cosp = 2.0 * (qw * qz + qx * qy)
        cosy_cosp = 1.0 - 2.0 * (qy * qy + qz * qz)
        yaw = math.degrees(math.atan2(siny_cosp, cosy_cosp))

        euler_angles.append([roll, pitch, yaw])

    euler_df = pd.DataFrame(euler_angles, columns=['IMU.euler_orientation.x', 'IMU.euler_orientation.y', 'IMU.euler_orientation.z'])
    return euler_df


def plot_error_histogram(columnx, columny, columnz, name, num_bins=20):

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel()

    sns.scatterplot(x=time_stamp, y=columnx, label="X Axis", ax=axes[0])
    sns.scatterplot(x=time_stamp, y=columny, label="Y Axis", ax=axes[0])
    sns.scatterplot(x=time_stamp, y=columnz, label="Z Axis", ax=axes[0])
    axes[0].set_xlabel("Time Stamp")
    axes[0].set_ylabel("Euler Angles")
    axes[0].set_title(name + " Readings")

    column_names = [columnx, columny, columnz]
    for i, column in enumerate(column_names):
        errors = column - column.mean()
        std_variation = column.std()
        mean = column.mean()
        median = column.median()
        print("Standard Deviaton: " + str(std_variation))
        print("Mean: " + str(mean))
        print("Median: " + str(median))
        axes[i+1].hist(errors, bins=num_bins, alpha=0.7, color='blue', edgecolor='black')
        axes[i+1].set_xlabel("Error")
        axes[i+1].set_ylabel("Frequency")
        column_xyz = str(column.name)
        axes[i+1].set_title(f"Error for {name} in " + column_xyz.split('.')[2].upper() + " axis")
        axes[i+1].grid(True)

    plt.tight_layout()
    plt.show()

stationary_bag = bagreader('/home/rayyan/catkin_ws/EECE5554/LAB3/src/Data/action_data.bag')
stationary_bag_data = stationary_bag.message_by_topic('/imu')
stationary_bag_readings = pd.read_csv(stationary_bag_data)

stationary_bag_readings['IMU.orientation.x'] -= stationary_bag_readings['IMU.orientation.x'].min()
stationary_bag_readings['IMU.orientation.y'] -= stationary_bag_readings['IMU.orientation.y'].min()
stationary_bag_readings['IMU.orientation.z'] -= stationary_bag_readings['IMU.orientation.z'].min()
stationary_bag_readings['IMU.orientation.w'] -= stationary_bag_readings['IMU.orientation.w'].min()

stationary_bag_readings['IMU.linear_acceleration.x'] -= stationary_bag_readings['IMU.linear_acceleration.x'].min()
stationary_bag_readings['IMU.linear_acceleration.y'] -= stationary_bag_readings['IMU.linear_acceleration.y'].min()
stationary_bag_readings['IMU.linear_acceleration.z'] -= stationary_bag_readings['IMU.linear_acceleration.z'].min()

stationary_bag_readings['IMU.angular_velocity.x'] -= stationary_bag_readings['IMU.angular_velocity.x'].min()
stationary_bag_readings['IMU.angular_velocity.y'] -= stationary_bag_readings['IMU.angular_velocity.y'].min()
stationary_bag_readings['IMU.angular_velocity.z'] -= stationary_bag_readings['IMU.angular_velocity.z'].min()

stationary_bag_readings['MagField.magnetic_field.x'] -= stationary_bag_readings['MagField.magnetic_field.x'].min()
stationary_bag_readings['MagField.magnetic_field.y'] -= stationary_bag_readings['MagField.magnetic_field.y'].min()
stationary_bag_readings['MagField.magnetic_field.z'] -= stationary_bag_readings['MagField.magnetic_field.z'].min()

time_stamp = stationary_bag_readings['Header.stamp.secs'] 

euler_angles = quaternion_to_euler(stationary_bag_readings['IMU.orientation.x'], stationary_bag_readings['IMU.orientation.y'], stationary_bag_readings['IMU.orientation.z'], stationary_bag_readings['IMU.orientation.w'])

plot_error_histogram(stationary_bag_readings['IMU.linear_acceleration.x'], stationary_bag_readings['IMU.linear_acceleration.y'], stationary_bag_readings['IMU.linear_acceleration.z'], "Linear Acceleration")
plot_error_histogram(stationary_bag_readings['IMU.angular_velocity.x'], stationary_bag_readings['IMU.angular_velocity.y'], stationary_bag_readings['IMU.angular_velocity.z'], "Angular Velocity")
plot_error_histogram(stationary_bag_readings['MagField.magnetic_field.x'], stationary_bag_readings['MagField.magnetic_field.y'], stationary_bag_readings['MagField.magnetic_field.z'], "Magnetic Field")
plot_error_histogram(euler_angles['IMU.euler_orientation.x'], euler_angles['IMU.euler_orientation.y'], euler_angles['IMU.euler_orientation.z'], "Orientation")
