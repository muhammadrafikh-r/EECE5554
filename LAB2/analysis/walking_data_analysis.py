import rosbag
import matplotlib.pyplot as plt
import numpy as np
import bagpy
from bagpy import bagreader
import pandas as pd
import math

# Specify the paths to your bag files
bag_file_1 = '/home/rayyan/catkin_ws/EECE5554/lab2/data/2023-10-16-15-38-09.bag'
bag_file_2 = '/home/rayyan/catkin_ws/EECE5554/lab2/data/2023-10-16-15-13-36.bag'

# Function to create a scatterplot from a bag file
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

    utm_northing_list = []
    utm_easting_list = []

    with rosbag.Bag(bag_file, 'r') as bag:
        first_point = None
        for topic, msg, t in bag.read_messages(topics=['/gps']):
            utm_northing_list.append(msg.utm_northing)
            utm_easting_list.append(msg.utm_easting)
            if first_point is None:
                first_point = (msg.utm_easting, msg.utm_northing)

    utm_easting_list = [e - first_point[0] for e in utm_easting_list]
    utm_northing_list = [n - first_point[1] for n in utm_northing_list]
    x_min = min(utm_easting_list)
    x_max = max(utm_easting_list)
    y_min = min(utm_northing_list)
    y_max = max(utm_northing_list)

    x_min_index = utm_easting_list.index(x_min)
    y_at_x_min = utm_northing_list[x_min_index]
    corner_1 = [x_min, y_at_x_min]

    y_max_index = utm_northing_list.index(y_max)
    x_at_y_max = utm_easting_list[y_max_index]
    corner_2 = [x_at_y_max, y_max]

    x_max_index = utm_easting_list.index(x_max)
    y_at_x_max = utm_northing_list[x_max_index]
    corner_3 = [x_max, y_at_x_max]

    y_min_index = utm_northing_list.index(y_min)
    x_at_y_min = utm_easting_list[y_min_index]
    corner_4 = [x_at_y_min, y_min]

    corners = np.array([corner_1, corner_2, corner_3, corner_4])
    corners_modified = np.array([corner_1, corner_2, corner_3, corner_4, corner_1])

    edge_1_points = []
    edge_2_points = []
    edge_3_points = []
    edge_4_points = []

    minimum = min(x_min_index,y_max_index)
    maximum = max(x_min_index,y_max_index)
    for i in range(minimum, maximum+1):
        edge_1_points.append([utm_easting_list[i], utm_northing_list[i]])
    
    minimum = min(x_max_index,y_max_index)
    maximum = max(x_max_index,y_max_index)
    for i in range(minimum, maximum+1):
        edge_2_points.append([utm_easting_list[i], utm_northing_list[i]])
    
    minimum = min(x_max_index,y_min_index)
    maximum = max(x_max_index,y_min_index)
    for i in range(minimum, maximum+1):
        edge_3_points.append([utm_easting_list[i], utm_northing_list[i]])

    minimum = min(x_min_index,y_min_index)
    maximum = max(x_min_index,y_min_index)
    for i in range(minimum, maximum+1):
        edge_4_points.append([utm_easting_list[i], utm_northing_list[i]])
    
    edge_1_x = []
    edge_1_y = []
    for i in range(len(edge_1_points)):
        edge_1_x.append(edge_1_points[i][0])
        edge_1_y.append(edge_1_points[i][1])
    edge_1_x = np.array(edge_1_x)
    edge_1_y = np.array(edge_1_y)

    edge_2_x = []
    edge_2_y = []
    for i in range(len(edge_2_points)):
        edge_2_x.append(edge_2_points[i][0])
        edge_2_y.append(edge_2_points[i][1])
    edge_2_x = np.array(edge_2_x)
    edge_2_y = np.array(edge_2_y)

    edge_3_x = []
    edge_3_y = []
    for i in range(len(edge_3_points)):
        edge_3_x.append(edge_3_points[i][0])
        edge_3_y.append(edge_3_points[i][1])
    edge_3_x = np.array(edge_3_x)
    edge_3_y = np.array(edge_3_y)

    edge_4_x = []
    edge_4_y = []
    for i in range(len(edge_4_points)):
        edge_4_x.append(edge_4_points[i][0])
        edge_4_y.append(edge_4_points[i][1])
    edge_4_x = np.array(edge_4_x)
    edge_4_y = np.array(edge_4_y)


    m_1, b_1 = np.polyfit(edge_1_x, edge_1_y, 1)  # Fit a linear regression line (y = mx + b)
    line_of_best_fit_1 = np.empty(len(edge_1_x))
    line_of_best_fit_1 = m_1*edge_1_x + b_1
    errors_1 = np.empty(len(edge_1_y))
    for i in range(len(edge_1_y)):
        errors_1 = np.append(errors_1, math.dist([edge_1_x[i], edge_1_y[i]], [edge_1_x[i], line_of_best_fit_1[i]]))
    mean_error_1 = np.mean(errors_1)

    m_2, b_2 = np.polyfit(edge_2_x, edge_2_y, 1)  # Fit a linear regression line (y = mx + b)
    line_of_best_fit_2 = np.empty(len(edge_2_x))
    line_of_best_fit_2 = m_2*edge_2_x + b_2
    errors_2 = np.empty(len(edge_2_y))
    for i in range(len(edge_2_y)):
        errors_2 = np.append(errors_2, math.dist([edge_2_x[i], edge_2_y[i]], [edge_2_x[i], line_of_best_fit_2[i]]))
    mean_error_2 = np.mean(errors_2)

    m_3, b_3 = np.polyfit(edge_3_x, edge_3_y, 1)  # Fit a linear regression line (y = mx + b)
    line_of_best_fit_3 = np.empty(len(edge_3_x))
    line_of_best_fit_3 = m_3*edge_3_x + b_3
    errors_3 = np.empty(len(edge_3_y))
    for i in range(len(edge_3_y)):
        errors_3 = np.append(errors_3, math.dist([edge_3_x[i], edge_3_y[i]], [edge_3_x[i], line_of_best_fit_3[i]]))
    mean_error_3 = np.mean(errors_3)

    m_4, b_4 = np.polyfit(edge_4_x, edge_4_y, 1)  # Fit a linear regression line (y = mx + b)
    line_of_best_fit_4 = np.empty(len(edge_4_x))
    line_of_best_fit_4 = m_4*edge_4_x + b_4
    errors_4 = np.empty(len(edge_4_y))
    for i in range(len(edge_4_y)):
        errors_4 = np.append(errors_4, math.dist([edge_4_x[i], edge_4_y[i]], [edge_4_x[i], line_of_best_fit_4[i]]))
    mean_error_4 = np.mean(errors_4)

    total_error = (mean_error_1 + mean_error_2 + mean_error_3 + mean_error_4)/4
    print('Mean Error = ', total_error)

    plt.figure(figsize=(8, 6))
    plt.scatter(utm_easting, utm_northing, label='UTM Data', s=5)
    plt.plot(corners_modified[:, 0], corners_modified[:, 1], 'k-')
    # plt.plot(edge_1_x, m_1*edge_1_x + b_1, color='red', label=f'Line of Best Fit')
    # plt.plot(edge_2_x, m_2*edge_2_x + b_2, color='red')
    # plt.plot(edge_3_x, m_3*edge_3_x + b_3, color='red')
    #plt.plot(edge_4_x, m_4*edge_4_x + b_4, color='red')
    plt.xlabel('Scaled UTM Easting')
    plt.ylabel('Scaled UTM Northing')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

create_scatterplot(bag_file_1, 'UTM Northing vs UTM Easting for Walking with Best Fit Line')
create_scatterplot(bag_file_2, 'UTM Northing vs UTM Easting for Walking Occluded with Best Fit Line')

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


hist, x_edges, y_edges = np.histogram2d(stationary_readings['utm_easting'], stationary_readings['utm_northing'], bins=50)

# Create a 2D histogram plot
plt.figure(figsize=(6, 6))
plt.imshow(hist.T, origin='lower', extent=[x_edges.min(), x_edges.max(), y_edges.min(), y_edges.max()], cmap='viridis')
plt.colorbar(label='Frequency')
plt.xlabel('UTM Easting')
plt.ylabel('UTM Northing')
plt.title('2D Histogram of Stationary Data')
plt.tight_layout()
plt.show()

# Create a 2D histogram
hist, x_edges, y_edges = np.histogram2d(stationary_occluded_readings['utm_easting'], stationary_occluded_readings['utm_northing'], bins=50)

plt.figure(figsize=(6, 6))
plt.imshow(hist.T, origin='lower', extent=[x_edges.min(), x_edges.max(), y_edges.min(), y_edges.max()], cmap='viridis')
plt.colorbar(label='Frequency')
plt.xlabel('UTM Easting')
plt.ylabel('UTM Northing')
plt.title('2D Histogram of Stationary Occluded Data')
plt.tight_layout()
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