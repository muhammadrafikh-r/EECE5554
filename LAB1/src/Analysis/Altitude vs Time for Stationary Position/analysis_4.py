import rosbag
import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Specify the path to your bag file
bag_file = '/home/rayyan/catkin_ws/src/Data/stationary.bag'

# Output CSV file name
csv_file = 'converted_utc_altitude_values.csv'

# Function to convert raw UTC timestamp to hours, minutes, and seconds
def convert_to_hours_minutes_seconds(raw_utc_timestamp):
    utc_datetime = datetime.utcfromtimestamp(raw_utc_timestamp)
    hours = utc_datetime.hour
    minutes = utc_datetime.minute
    seconds = utc_datetime.second
    return hours, minutes, seconds

# Lists to store converted UTC timestamps and Altitude data
converted_utc_values = []
altitude_values = []

# Open the bag file
with rosbag.Bag(bag_file, 'r') as bag:
    for topic, msg, t in bag.read_messages():
        if topic == '/gps':  # Replace with the actual topic name for UTC timestamps
            # Assuming the UTC value is a Unix timestamp in seconds (adjust as needed)
            raw_utc_timestamp = msg.UTC
            hours, minutes, seconds = convert_to_hours_minutes_seconds(raw_utc_timestamp)
            converted_utc_values.append((hours, minutes, seconds))
            altitude_values.append(msg.Altitude)

# Write the converted UTC timestamps and Altitude data to a CSV file
with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Hours', 'Minutes', 'Seconds', 'Altitude'])  # Write CSV headers

    for (hours, minutes, seconds), altitude in zip(converted_utc_values, altitude_values):
        csv_writer.writerow([hours, minutes, seconds, altitude])

print(f'Converted UTC timestamps and Altitude data saved to {csv_file}')

# Lists to store the converted UTC timestamps and Altitude data
timestamps = []
altitude_values = []

# Read data from the CSV file
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        hours = int(row['Hours'])
        minutes = int(row['Minutes'])
        seconds = int(row['Seconds'])
        timestamp = hours * 3600 + minutes * 60 + seconds
        altitude = float(row['Altitude'])
        timestamps.append(timestamp)
        altitude_values.append(altitude)

# Create a plot of Altitude vs Time
plt.figure(figsize=(10, 6))
plt.plot(timestamps, altitude_values, marker='o', linestyle='-', label='Altitude vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude (meters)')
plt.title('Altitude vs Time For Stationary Position')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
