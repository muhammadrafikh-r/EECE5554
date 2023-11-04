import rosbag
import matplotlib.pyplot as plt
import numpy as np
import bagpy
from bagpy import bagreader
import pandas as pd

#PATH TO BAG FILES
bag_file_1 = '/home/rayyan/catkin_ws/EECE5554/lab2/data/2023-10-16-15-22-04.bag'
bag_file_2 = '/home/rayyan/catkin_ws/EECE5554/lab2/data/2023-10-16-15-00-42.bag'

#FUNCTION TO CREATE SCATTERPLOT OF NORTHING VS EASTING DATA FROM BAG FILES
def create_scatterplot(bag_file, title):

    utm_northing = []
    utm_easting = []

    with rosbag.Bag(bag_file, 'r') as bag:
        first_point = None
        for topic, msg, t in bag.read_messages(topics=['/gps']):
            utm_northing.append(msg.utm_northing)
            utm_easting.append(msg.utm_easting)
            if first_point is None:
                first_point = (msg.utm_easting, msg.utm_northing)

    utm_easting = [e - first_point[0] for e in utm_easting]
    utm_northing = [n - first_point[1] for n in utm_northing]

    plt.figure(figsize=(8, 6))
    plt.scatter(utm_easting, utm_northing, label='UTM Data', s=5)
    plt.xlabel('Scaled UTM Easting')
    plt.ylabel('Scaled UTM Northing')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

#FUNCTION CALL TO CREATE SCATTERPLOTS OF NORTHING VS EASTING DATA
create_scatterplot(bag_file_1, 'UTM Northing vs UTM Easting for Stationary Position')
create_scatterplot(bag_file_2, 'UTM Northing vs UTM Easting for Occluded Stationary Position')

#FUCNTION DEFINITION TO CALCULATE MEDIAN ABSOLUTE DEVIATION
def median_absolute_deviation(data):
 
    median = np.median(data)
    absolute_deviations = np.abs(data - median)
    median_absolute_deviation = np.median(absolute_deviations)
    return median_absolute_deviation

stationary_bag = bagreader(bag_file_1)
stationary_occluded_bag = bagreader(bag_file_2)

stationary_data = stationary_bag.message_by_topic("/gps")
stationary_occluded_data = stationary_occluded_bag.message_by_topic("/gps")

stationary_readings = pd.read_csv(stationary_data)
stationary_occluded_readings = pd.read_csv(stationary_occluded_data)

median_absolute_deviation__stationary_northing = median_absolute_deviation(stationary_readings['utm_northing'])
median_absolute_deviation__stationary_easting = median_absolute_deviation(stationary_readings['utm_easting'])
print("Median Absolute Deviation for Northing of Stationary Position: " + str(median_absolute_deviation__stationary_northing))
print("Median Absolute Deviation for Easting of Stationary Position: " + str(median_absolute_deviation__stationary_easting))

median_absolute_deviation__stationary_occluded_northing = median_absolute_deviation(stationary_occluded_readings['utm_northing'])
median_absolute_deviation__stationary_occluded_easting = median_absolute_deviation(stationary_occluded_readings['utm_easting'])
print("Median Absolute Deviation for Northing of Stationary Occluded Position: " + str(median_absolute_deviation__stationary_occluded_northing))
print("Median Absolute Deviation for Easting of Stationary Occluded Position: " + str(median_absolute_deviation__stationary_occluded_easting))

#Data Normalization
stationary_readings['utm_easting'] -= stationary_readings['utm_easting'].min()
stationary_readings['utm_northing'] -= stationary_readings['utm_northing'].min()

stationary_occluded_readings['utm_easting'] -= stationary_occluded_readings['utm_easting'].min()
stationary_occluded_readings['utm_northing'] -= stationary_occluded_readings['utm_northing'].min()


#2D HISTOGRAM OF STATIONARY POSITION

plt.rcParams["figure.figsize"] = [7.50, 7.50]
plt.rcParams["figure.autolayout"] = True
x = stationary_readings['utm_easting']
y = stationary_readings['utm_northing']

fig, ax = plt.subplots()
_ = ax.hist2d(x[::10], y[::10])

ax.set_xlabel('UTM Easting')
ax.set_ylabel('UTM Northing')
ax.set_title('2D Histogram of Stationary Data')

plt.show()

#2D HISTOGRAM OF STATIONARY OCCLUDED POSITION

plt.rcParams["figure.figsize"] = [7.50, 7.50]
plt.rcParams["figure.autolayout"] = True
x = stationary_occluded_readings['utm_easting']
y = stationary_occluded_readings['utm_northing']

fig, ax = plt.subplots()
_ = ax.hist2d(x[::10], y[::10])

ax.set_xlabel('UTM Easting')
ax.set_ylabel('UTM Northing')
ax.set_title('2D Histogram of Stationary Occluded Data')

plt.show()

# Create a figure with two subplots (one row, two columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot UTM Easting Histogram
ax1.hist(stationary_readings['utm_easting'], bins=20, color='blue', alpha=0.7, edgecolor='black')
ax1.set_title('UTM Easting (Stationary Data)')
ax1.set_xlabel('Easting Values')
ax1.set_ylabel('Frequency')

# Plot UTM Northing Histogram
ax2.hist(stationary_readings['utm_northing'], bins=20, color='green', alpha=0.7, edgecolor='black')
ax2.set_title('UTM Northing (Stationary Data)')
ax2.set_xlabel('Northing Values')
ax2.set_ylabel('Frequency')

plt.show()

# Create a figure with two subplots (one row, two columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot UTM Easting Histogram
ax1.hist(stationary_occluded_readings['utm_easting'], bins=20, color='blue', alpha=0.7, edgecolor='black')
ax1.set_title('UTM Easting (Stationary Occluded Data)')
ax1.set_xlabel('Easting Values')
ax1.set_ylabel('Frequency')

# Plot UTM Northing Histogram
ax2.hist(stationary_occluded_readings['utm_northing'], bins=20, color='green', alpha=0.7, edgecolor='black')
ax2.set_title('UTM Northing (Stationary Occluded Data)')
ax2.set_xlabel('Northing Values')
ax2.set_ylabel('Frequency')

plt.show()


# Known stationary position (true latitude and longitude)
true_latitude = 42.33879
true_longitude = -71.0883

# Lists to store errors
latitude_errors = []
longitude_errors = []

# Open the bag file
with rosbag.Bag(bag_file_1, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=['/gps']):
        # Calculate error in latitude and longitude
        latitude_error = msg.latitude - true_latitude
        longitude_error = msg.longitude - true_longitude
        latitude_errors.append(latitude_error)
        longitude_errors.append(longitude_error)

# Calculate the magnitude of errors (Euclidean distance)
error_magnitudes = np.sqrt(np.square(latitude_errors) + np.square(longitude_errors))

# Error Metrics
mae = np.mean(np.abs(error_magnitudes))  # Mean Absolute Error (MAE)
rmse = np.sqrt(np.mean(np.square(error_magnitudes)))  # Root Mean Square Error (RMSE)
mem = np.mean(error_magnitudes)  # Mean Error Magnitude (MEM)

# Print the error metrics
print(f'Mean Absolute Error (MAE)for Stationary Position: {mae} meters')
print(f'Root Mean Square Error (RMSE) for Stationary Position: {rmse} meters')
print(f'Mean Error Magnitude (MEM) for Stationary Position: {mem} meters')

# Create a histogram of the error magnitudes
plt.figure(figsize=(8, 6))
plt.hist(error_magnitudes, bins=30, color='blue', alpha=0.7)
plt.xlabel('Error Magnitude')
plt.ylabel('Frequency')
plt.title('Error Histogram for Stationary Position')
plt.grid(True)
plt.show()

# Known stationary occluded position (true latitude and longitude)
true_latitude = 42.33862
true_longitude = -71.08575

# Lists to store errors
latitude_errors = []
longitude_errors = []

# Open the bag file
with rosbag.Bag(bag_file_1, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=['/gps']):
        # Calculate error in latitude and longitude
        latitude_error = msg.latitude - true_latitude
        longitude_error = msg.longitude - true_longitude
        latitude_errors.append(latitude_error)
        longitude_errors.append(longitude_error)

# Calculate the magnitude of errors (Euclidean distance)
error_magnitudes = np.sqrt(np.square(latitude_errors) + np.square(longitude_errors))

# Error Metrics
mae = np.mean(np.abs(error_magnitudes))  # Mean Absolute Error (MAE)
rmse = np.sqrt(np.mean(np.square(error_magnitudes)))  # Root Mean Square Error (RMSE)
mem = np.mean(error_magnitudes)  # Mean Error Magnitude (MEM)

# Print the error metrics
print(f'Mean Absolute Error (MAE) for Stationary Occluded Position: {mae} meters')
print(f'Root Mean Square Error (RMSE) for Stationary Occluded Position: {rmse} meters')
print(f'Mean Error Magnitude (MEM) for Stationary Occluded Position: {mem} meters')

# Create a histogram of the error magnitudes
plt.figure(figsize=(8, 6))
plt.hist(error_magnitudes, bins=30, color='blue', alpha=0.7)
plt.xlabel('Error Magnitude')
plt.ylabel('Frequency')
plt.title('Error Histogram for Stationary Occluded Position')
plt.grid(True)
plt.show()