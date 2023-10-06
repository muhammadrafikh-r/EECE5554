import rosbag
import matplotlib.pyplot as plt
import numpy as np

# Specify the path to your bag file
bag_file = '/home/rayyan/catkin_ws/src/Data/stationary_occluded.bag'

# Known stationary position (true latitude and longitude)
true_latitude = 42.3417256
true_longitude = -71.1002406

# Lists to store errors
latitude_errors = []
longitude_errors = []

# Open the bag file
with rosbag.Bag(bag_file, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=['/gps']):
        # Calculate error in latitude and longitude
        latitude_error = msg.Latitude - true_latitude
        longitude_error = msg.Longitude - true_longitude
        latitude_errors.append(latitude_error)
        longitude_errors.append(longitude_error)

# Calculate the magnitude of errors (Euclidean distance)
error_magnitudes = np.sqrt(np.square(latitude_errors) + np.square(longitude_errors))

# Error Metrics
mae = np.mean(np.abs(error_magnitudes))  # Mean Absolute Error (MAE)
rmse = np.sqrt(np.mean(np.square(error_magnitudes)))  # Root Mean Square Error (RMSE)
mem = np.mean(error_magnitudes)  # Mean Error Magnitude (MEM)

# Print the error metrics
print(f'Mean Absolute Error (MAE): {mae:.2f} meters')
print(f'Root Mean Square Error (RMSE): {rmse:.2f} meters')
print(f'Mean Error Magnitude (MEM): {mem:.2f} meters')

# Create a histogram of the error magnitudes
plt.figure(figsize=(8, 6))
plt.hist(error_magnitudes, bins=30, color='blue', alpha=0.7)
plt.xlabel('Error Magnitude')
plt.ylabel('Frequency')
plt.title('Error Histogram for Occluded Stationary Position')
plt.grid(True)
plt.show()
