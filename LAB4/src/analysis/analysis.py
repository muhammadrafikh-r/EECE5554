import bagpy
from bagpy import bagreader
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy import signal, integrate
from scipy.signal import butter, filtfilt
import scipy.integrate as integrated_yaw_z
from geopy.distance import geodesic

sns.set(style="whitegrid")


#MAGNETOMETER CALIBRATION

calibration_bag = bagreader('/home/rayyan/catkin_ws/EECE5554/LAB4/src/data/data_going_in_circles.bag')
gps_data = calibration_bag.message_by_topic('/gps')
imu_data = calibration_bag.message_by_topic('/imu')

gps_readings = pd.read_csv(gps_data)	
imu_readings = pd.read_csv(imu_data)

time_secs = imu_readings['Header.stamp.secs'].values
time_nsecs = np.double(imu_readings['Header.stamp.nsecs'])
time_nsecs /= 1000000000
time_imu = np.double(time_secs + time_nsecs)
time_imu -= time_imu.min()

x_values = imu_readings['MagField.magnetic_field.x'].values
y_values = imu_readings['MagField.magnetic_field.y'].values
z_values = imu_readings['MagField.magnetic_field.z'].values
x_values -= x_values.min()
y_values -= y_values.min()
z_values -= z_values.min()

x_values = x_values*10000
y_values = y_values*10000
z_values = z_values*10000

#Hard Iron Error Calculation 
x_mean = np.mean(x_values)
y_mean = np.mean(y_values)

#Hard-Iron Correction
x_values_corrected = x_values - x_mean
y_values_corrected = y_values - y_mean

imu_data = np.array([x_values, y_values, z_values])

#PLOT OF RAW MAGNETOMETER DATA (ONLY CORRECTED FOR ZERO BIAS)
plt.grid(color='grey', linestyle='--', linewidth=1)
plt.scatter(x_values, y_values, marker='x', label = 'Raw Magnetometer Data', color='palevioletred')
plt.title('Raw Magnetic Field')
plt.xlabel('X (Gauss)')
plt.ylabel('Y (Gauss)')
plt.legend()
plt.show()

#PLOT OF HARD-IRON CALIBRATED MAGNETOMETER DATA
plt.grid(color='grey', linestyle='--', linewidth=1)
plt.scatter(x_values_corrected, y_values_corrected, marker='x', label = 'Hard-Iron Calibrated', color='palevioletred')
doughnut = plt.Circle((0.0, 0.0), 0.10, fill=False, color='black')
plt.gca().add_patch(doughnut)
plt.gca().set_aspect("equal")
plt.title('Hard_Iron_Calibration Of Magnetic Field')
plt.xlabel('Hard_Iron_X (Gauss)')
plt.ylabel('Hard_Iron_Y (Gauss)')
plt.legend()
plt.show()

# SOFT-IRON ERROR CALCULATION
X_major = float(x_values_corrected[2000])
Y_major = float(y_values_corrected[2000])
radius = math.sqrt((X_major**2) + (Y_major**2))
theta = np.arcsin((Y_major/radius))

R = [[np.cos(theta), np.sin(theta)], [np.sin(-theta), np.cos(theta)]]
v = [x_values_corrected, y_values_corrected]

matrix = np.matmul(R, v)

#PLOT OF SOFT-IRON CALIBRATED MAGNETOMETER DATA
plt.grid(color='grey', linestyle='--', linewidth=1)
plt.scatter(matrix[0], matrix[1], marker='x', label = 'Soft-Iron Calibrated', color='palevioletred')
doughnut = plt.Circle((0.0, 0.0), 0.10, fill=False, color='black')
plt.gca().add_patch(doughnut)
plt.gca().set_aspect("equal")
plt.title('Soft_Iron_Calibration of Magnetic Field')
plt.xlabel('Soft_Iron_X (Gauss)')
plt.ylabel('Soft_Iron_Y (Gauss)')
plt.legend()
plt.show()

#these values are observed by seeing the circle that fits the data. r is the radius in y direction, and q is the radius in the x direction.
r = 0.10
q = 0.10
sigma = q/r

#HARD-IRON & SOFT-IRONCORRECTION OF MAGNETOMETER DATA
matrix2 = [[1, 0], [0, sigma]]
rotate = np.matmul(matrix2, matrix)
theta = -theta
R1 = [[np.cos(theta), np.sin(theta)], [np.sin(-theta), np.cos(theta)]]
v1 = np.matmul(R1, rotate)

#PLOT OF HARD-IRON & SOFT-IRON CALIBRATED MAGNETIC FIELD
plt.grid(color='grey', linestyle='--', linewidth=1)
plt.scatter(v1[0], v1[1], marker='x', label='Hard and Soft Iron Calibrated Data', color='indianred')
doughnut = plt.Circle((0.0, 0.0), 0.10, fill=False, color='black')
plt.gca().add_patch(doughnut)
plt.gca().set_aspect("equal")
plt.title('Final Calibrated Plot Of Magnetic Field X vs Y')
plt.xlabel('Mx (Gauss)')
plt.ylabel('My (Gauss)')
plt.rcParams.update({'font.size': 22})
plt.legend()
plt.show()


###################################SENSOR FUSION######################################################

calibration_bag = bagreader('/home/rayyan/catkin_ws/EECE5554/LAB4/src/data/data_driving.bag')
gps_data = calibration_bag.message_by_topic('/gps')
imu_data = calibration_bag.message_by_topic('/imu')

gps_readings = pd.read_csv(gps_data)	
imu_readings = pd.read_csv(imu_data)

time_secs = imu_readings['Header.stamp.secs'].values
time_nsecs = np.double(imu_readings['Header.stamp.nsecs'].values)
time_nsecs /= 1000000000
time_imu = np.double(time_secs + time_nsecs)
time_imu -= time_imu.min()

x_values = imu_readings['MagField.magnetic_field.x'].values
y_values = imu_readings['MagField.magnetic_field.y'].values
z_values = imu_readings['MagField.magnetic_field.z'].values
x_values -= x_values.min()
y_values -= y_values.min()
z_values -= z_values.min()

x_values = x_values*10000
y_values = y_values*10000
z_values = z_values*10000

#Hard Iron Error Calculation 
x_mean = np.mean(x_values)
y_mean = np.mean(y_values)

#Hard-Iron Correction
x_values_corrected = x_values - x_mean
y_values_corrected = y_values - y_mean

# SOFT-IRON ERROR CALCULATION
X_major = float(x_values_corrected[2000])
Y_major = float(y_values_corrected[2000])
radius = math.sqrt((X_major**2) + (Y_major**2))
theta = np.arcsin((Y_major/radius))

R = [[np.cos(theta), np.sin(theta)], [np.sin(-theta), np.cos(theta)]]
v = [x_values_corrected, y_values_corrected]

matrix = np.matmul(R, v)

r = 0.10
q = 0.10
sigma = q/r

#HARD-IRON & SOFT-IRON CORRECTION OF MAGNETOMETER DATA
matrix2 = [[1, 0], [0, sigma]]
rotate = np.matmul(matrix2, matrix)
theta = -theta
R1 = [[np.cos(theta), np.sin(theta)], [np.sin(-theta), np.cos(theta)]]
v1 = np.matmul(R1, rotate)

plt.plot(time_imu, x_values, label="Raw X Axis Magnetometer Data")
plt.plot(time_imu, v[0], label = "Corrected X Axis Magnetometer Data")
plt.xlabel("Time (seconds)")
plt.ylabel("Mx (Gauss)")
plt.title("Magnetic Field (X-Axis) vs Time")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(time_imu, y_values, label="Raw Y Axis Magnetometer Data")
plt.plot(time_imu, v[1], label = "Corrected Y Axis Magnetometer Data")
plt.xlabel("Time (seconds)")
plt.ylabel("My (Gauss)")
plt.title("Magnetic Field (Y-Axis) vs Time")
plt.legend()
plt.grid(True)
plt.show()

#CALCULATION OF UNCORRECTED YAW ANGLE IN RADIANS FROM RAW MAGNETOMETER DATA (ONLY CORRECTED FOR BIAS AND SCALED (NORMALIZED))
yaw_radians_uncorrected_wrapped = np.arctan2(y_values, x_values)

#CALCULATE YAW ANGLE IN RADIANS FROM CORRECTED (FOR SOFT AND HARD IRON) MAGNETOMETER DATA. WRAPPPED MEANS THE DATA GOES FROM O TO 2*pi and then comes back to 0.
yaw_radians_corrected_wrapped = np.arctan2(v1[1], v1[0])

#UNWRAP THE UNCORRECTED YAW RADIANS ANGLE DATA TO GET UNWRAPPED YAW ANGLES IN RADIANS. UNWRAPPED MEANS THAT THE DATA GOES FROM 0 TO INFINITY, THAT IS 0 TO 28Pi, and then 2*pi to 4*pi and so on.
yaw_radians_uncorrected_unwrapped = np.unwrap(yaw_radians_uncorrected_wrapped)

#UNWRAP THE CORRECTED YAW RADIANS ANGLE DATA TO GET UNWRAPPED YAW ANGLES IN RADIANS.
yaw_radians_corrected_unwrapped = np.unwrap(yaw_radians_corrected_wrapped)

#CONVERSION OF WRAPPED UNCORRECTED AND CORRECTED YAW ANGLES FROM RADIANS TO DEGREES.
yaw_angle_uncorrected_from_wrapped = np.degrees(yaw_radians_uncorrected_wrapped)
yaw_angle_corrected_from_wrapped = np.degrees(yaw_radians_corrected_wrapped)

#PLOT OF UNCORRECTED WRAPPED RADIANS VS TIME WITH CORRECTED UNWRAPPED RADIANS VS TIME
plt.figure(figsize=(10, 5))
plt.plot(time_imu, yaw_radians_corrected_wrapped, label="Corrected Yaw (Radians)")
plt.plot(time_imu, yaw_radians_uncorrected_wrapped, label = "Uncorrected Yaw (Radians)")
plt.xlabel("Time (seconds)")
plt.ylabel("Yaw Angle (Radians)")
plt.title("Yaw Angle vs Time")
plt.legend()
plt.grid(True)

#PLOT OF UNCORRECTED UNWRAPPED RADIANS VS TIME WITH CORRECTED UNWRAPPED RADIANS VS TIME
plt.figure(figsize=(10, 5))
plt.plot(time_imu, yaw_radians_corrected_unwrapped, label="Corrected Unwrapped Yaw (Radians)")
plt.plot(time_imu, yaw_radians_uncorrected_unwrapped, label = "Uncorrected UnwrappedYaw (Radians)")
plt.xlabel("Time (seconds)")
plt.ylabel("Yaw Angle (Radians)")
plt.title("Yaw Angle over Time")
plt.legend()
plt.grid(True)

#PLOT OF UNCORRECTED WRAPPED YAW ANGLE VS TIME WITH CORRECTED WRAPPED YAW ANGLE VS TIME 
plt.figure(figsize=(10, 5))
plt.plot(time_imu, yaw_angle_uncorrected_from_wrapped, label="Uncorrected Yaw (Angle)")
plt.plot(time_imu, yaw_angle_corrected_from_wrapped, label = "Corrected Yaw (Angle)")
plt.xlabel("Time (seconds)")
plt.ylabel("Yaw Angle (Degrees)")
plt.title("Yaw Angle over Time")
plt.legend()
plt.grid(True)

plt.show()

def quaternion_to_euler(w,x,y,z):

    w = w.values
    x = x.values
    y = y.values
    z = z.values
    # Calculate yaw (Z-axis rotation)
    
    yaw = np.arctan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))

    # Calculate pitch (Y-axis rotation)
    sin_p = 2 * (w * y - z * x)
    if (abs(sin_p) >= 1).all():
    # Handle the case where the condition is true for all elements
    	pitch = np.copysign(np.pi / 2, sin_p)
    else:
    # Handle the case where the condition is not true for all elements
    	pitch = np.arcsin(sin_p)

    # Calculate roll (X-axis rotation)
    roll = np.arctan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))

    # Return Euler angles in radians
    return yaw, pitch, roll

############## DRIVING DATA ANALYSIS ##############

driving_bag = bagreader("/home/rayyan/catkin_ws/EECE5554/LAB4/src/data/data_driving.bag")
imu_data_driving = driving_bag.message_by_topic('/imu')
gps_data_driving = driving_bag.message_by_topic('/gps')

gps_readings_driving = pd.read_csv(gps_data_driving)
imu_readings_driving = pd.read_csv(imu_data_driving)

time_secs_d = imu_readings_driving['Header.stamp.secs'].values
time_nsecs_d = np.double(imu_readings_driving['Header.stamp.nsecs'].values)
time_nsecs_d /= 1000000000
time_imu_d = np.double(time_secs_d + time_nsecs_d)
time_imu_d -= time_imu_d.min()

w_d = imu_readings_driving['IMU.orientation.w']
x_d = imu_readings_driving['IMU.orientation.x']
y_d = imu_readings_driving['IMU.orientation.y']
z_d = imu_readings_driving['IMU.orientation.z']
orientation_z_d, orientation_y_d, orientation_x_d = quaternion_to_euler(w_d,x_d,y_d,z_d)

gyro_z = imu_readings_driving['IMU.angular_velocity.z'].values 
integrated_yaw_z = integrate.cumtrapz(gyro_z, time_imu_d, initial=0)

# Define your filter parameters and data
plt.figure(figsize=(10,5))
plt.plot(time_imu_d, yaw_radians_corrected_wrapped, label="Magnetometer Yaw")
plt.plot(time_imu_d, -integrated_yaw_z, label="Gyroscope Yaw")
plt.plot(time_imu_d, orientation_z_d, label="IMU Yaw(Orientation)")
plt.xlabel("Time (seconds)")
plt.ylabel("Yaw (radians)")
plt.legend()
plt.title("Yaw from Magnetometer, Gyroscope & IMU")

plt.show()

b, a = butter(3, 0.1, "lowpass", fs=40, analog=False)
lpf = filtfilt(b, a, yaw_radians_corrected_unwrapped)
b, a = butter(3, 0.0001, 'highpass', fs=40, analog=False)
hpf = filtfilt(b, a, integrated_yaw_z)
alpha = 0.75

# Initialize yaw_filtered as an empty list
yaw_filtered = [0]

for i in range(len(hpf) - 1):
    j = i + 1
    if j < len(hpf) and j < len(lpf):
        filtered_value = alpha * (yaw_filtered[i] + hpf[j] * 0.05) + ((1 - alpha) * lpf[j])
        yaw_filtered.append(filtered_value)

plt.figure(figsize=(10,5))
plt.plot(time_imu_d, lpf, label="LPF (Magnetometer Yaw)")
plt.plot(time_imu_d, -hpf, label="HPF (Gyroscope Yaw)")
plt.plot(time_imu_d, yaw_filtered, label="Complementary filter")
plt.xlabel("Time (seconds)")
plt.ylabel("Yaw (radians)")
plt.legend()
plt.title("Filters implementation")

plt.show()

plt.figure(figsize=(10,5))
plt.plot(time_imu_d,-integrated_yaw_z, label='using Angular velocity from Gyroscope')
plt.plot(time_imu_d, orientation_z_d, label="using Yaw from Orientation data")
plt.plot(time_imu_d, yaw_radians_corrected_wrapped, label='using Corrected Magnetometer')
plt.plot(time_imu_d, yaw_filtered, label="Complementary filter")

plt.xlabel('Time (seconds)')
plt.ylabel('Yaw angle (radians)')
plt.title('Yaw angle vs Time')
plt.legend()
plt.grid(True)
plt.show()

############################################
############## VELOCITY ####################
############################################

dx = gps_readings_driving['UTM_easting'].values
dy = gps_readings_driving['UTM_northing'].values
dt_complete = gps_readings_driving['Time'].values
dt_up_without_decimal = [int(number) for number in dt_complete]
dt_up = dt_up_without_decimal
dt_up = np.array(dt_up)
gps_lon = gps_readings_driving['Longitude'].values
gps_lat = gps_readings_driving['Latitude'].values

time_secs_gps_d = gps_readings_driving['Header.stamp.secs'].values
time_nsecs_gps_d = np.double(gps_readings_driving['Header.stamp.nsecs'].values)
time_nsecs_gps_d /= 1000000000
time_gps_d = np.double(time_secs_gps_d + time_nsecs_gps_d)

velocity_linear_x_array = imu_readings_driving['IMU.linear_acceleration.x'].values
velocity_linear_x_array = velocity_linear_x_array - np.mean(velocity_linear_x_array)

velocity_linear_x = integrate.cumtrapz(imu_readings_driving['IMU.linear_acceleration.x'], time_imu_d , initial=0)
velocity_linear_x_mean = integrate.cumtrapz(velocity_linear_x_array, time_imu_d , initial=0)

gps_readings_driving_np = pd.DataFrame.to_numpy(gps_readings_driving)

############################removing redundant data from GPS data

ds_list_new = np.empty((0))
dt_list_new = np.empty((0))
for i in range(dt_up.shape[0]-1):
    ds_new = np.sqrt(np.square(dx[i+1] - dx[i] ) + np.square(dy[i+1] - dy[i]))
    dt_new =dt_up[i+1] - dt_up[i]
    ds_list_new = np.append(ds_list_new, ds_new)
    dt_list_new = np.append(dt_list_new, dt_new)

dv_new = ds_list_new/dt_list_new
dt_complete-=dt_complete.min()
plt.plot(dt_complete[:-1], dv_new)
plt.xlabel("Time (seconds)")
plt.ylabel("Linear Velocity (m/s)")
plt.title("GPS Velocity")
plt.legend()
plt.show()

test_time_list = np.array(time_secs_d)
unique_velocity_linear_x = []
for timestamp in dt_up:
    indices = np.where(test_time_list == timestamp)
    unique_velocity_linear_x.append(velocity_linear_x[indices[0][0]])

unique_velocity_linear_x = np.array(unique_velocity_linear_x)
dt_up_copy = np.copy(dt_up)
dt_up -= dt_up.min()

m,b = np.polyfit(dt_up,unique_velocity_linear_x,1)
dist_lobf = np.absolute(dt_up[:]*m - unique_velocity_linear_x[:] + b)/(np.sqrt(m**2+1))
# plt.close()

plt.plot(dt_complete,m*dt_up+b, "black", label="Line of best fit for IMU Vecloity with bias")
plt.plot(dt_complete, unique_velocity_linear_x, "r", label="IMU Velocity with bias")
plt.plot(dt_complete, dist_lobf, "g", label="IMU Velocity without bias")
# plt.plot(dt_complete[:-1], dv_new, "b",label="GPS Velocity")
plt.xlabel("Time (seconds)")
plt.ylabel("Linear Velocity (m/s)")
plt.title("Velocity estimation using acceleration from IMU")
plt.legend()
plt.show()

###########Dead Reckoning######################################################################

#Comparison of Displacements
#Calculation of Displacement from Forward (X) Velocity estimated using the Forward (X) acceleration of IMU
print('*************************************************************************')
displacement_linear_x = integrate.cumtrapz(unique_velocity_linear_x, dt_complete, initial=0)

#Calculation of Displacement from Forward (X) Velocity estimated using the Forward (X) acceleration of IMU
print('*************************************************************************')
displacement_GPS_linear_x = integrate.cumtrapz(ds_list_new, dt_complete[:-1], initial=0)

plt.plot(dt_complete[:-1], displacement_linear_x[:-1], "black", label="IMU")
plt.plot(dt_complete[:-1], displacement_GPS_linear_x, "r", label="GPS")
plt.xlabel("Time (in seconds)")
plt.ylabel("Distance (m)")
plt.title("Comparison of Displacement")
plt.legend()
plt.show()

dx = gps_readings_driving['UTM_easting'].values
dy = gps_readings_driving['UTM_northing'].values
dx -= (dx.min()+93)
dy -= dy.min()
plt.figure(figsize=(8, 6))
plt.scatter(dx, dy, label='UTM Data - (Bias + 93)', s=5)

unique_comp_yaw = []
unique_driving_orientation_z = []

for timestamp in dt_up_copy:
    indices = np.where(test_time_list == timestamp)
    unique_comp_yaw.append(yaw_filtered[indices[0][0]])

unique_comp_yaw = np.array(unique_comp_yaw)

velocity_easting = np.cos(unique_comp_yaw + 90*(np.pi/180)) * dist_lobf
velocity_northing = np.sin(unique_comp_yaw + 90*(np.pi/180)) * dist_lobf

easting_distance = integrate.cumtrapz(velocity_easting, dt_complete, initial=0) * 1.75
northing_distance = integrate.cumtrapz(velocity_northing, dt_complete, initial=0) * 1.75

plt.plot(easting_distance, northing_distance, "r", label = "IMU (Complementay FIlter) Trajectory x 1.75")
plt.legend()
plt.title("GPS Trajectory & IMU Trajectory")
plt.show()