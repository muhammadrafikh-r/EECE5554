import rosbag
import matplotlib.pyplot as plt
import numpy as np

# Specify the paths to your bag files
bag_file = '/home/rayyan/catkin_ws/src/Data/walking.bag'

# Function to create a scatterplot with a line of best fit and error calculation
def create_scatterplot_with_best_fit_and_error(bag_file, title):
    UTM_northing = []
    UTM_easting = []

    with rosbag.Bag(bag_file, 'r') as bag:
        first_point = None
        for topic, msg, t in bag.read_messages(topics=['/gps']):
            UTM_northing.append(msg.UTM_northing)
            UTM_easting.append(msg.UTM_easting)
            if first_point is None:
                first_point = (msg.UTM_easting, msg.UTM_northing)

    UTM_easting = [e - first_point[0] for e in UTM_easting]
    UTM_northing = [n - first_point[1] for n in UTM_northing]

    # Perform linear regression to find the line of best fit
    x = np.array(UTM_easting)
    y = np.array(UTM_northing)
    m, b = np.polyfit(x, y, 1)  # Fit a linear regression line (y = mx + b)

    # Calculate the line of best fit
    line_of_best_fit = m * x + b

    # Calculate errors (vertical distances) from data points to the line of best fit
    errors = y - line_of_best_fit

    plt.figure(figsize=(8, 6))
    plt.scatter(UTM_easting, UTM_northing, label='UTM Data', s=5)
    plt.plot(x, m*x + b, color='red', label=f'Line of Best Fit')
    plt.xlabel('Scaled UTM Easting')
    plt.ylabel('Scaled UTM Northing')
    plt.title(title)
    plt.grid(True)
    plt.legend()

    # Display error information
    mean_error = np.mean(errors)
    max_error = np.max(np.abs(errors))
    plt.text(0.1, 0.9, f'Mean Error: {mean_error:.2f}', transform=plt.gca().transAxes, fontsize=12)
    plt.text(0.1, 0.85, f'Max Error: {max_error:.2f}', transform=plt.gca().transAxes, fontsize=12)

    plt.show()

# Create scatterplot with a line of best fit and error calculation for the bag file
create_scatterplot_with_best_fit_and_error(bag_file, 'Scaled UTM Northing vs Scaled UTM Easting for Walking')
