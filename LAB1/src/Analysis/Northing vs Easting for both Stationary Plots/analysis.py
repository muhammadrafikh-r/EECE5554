import rosbag
import matplotlib.pyplot as plt

# Specify the paths to your bag files
bag_file_1 = '/home/rayyan/catkin_ws/src/Data/stationary.bag'
bag_file_2 = '/home/rayyan/catkin_ws/src/Data/stationary_occluded.bag'

# Function to create a scatterplot from a bag file
def create_scatterplot(bag_file, title):
    utm_northing = []
    utm_easting = []

    with rosbag.Bag(bag_file, 'r') as bag:
        first_point = None
        for topic, msg, t in bag.read_messages(topics=['/gps']):
            utm_northing.append(msg.UTM_northing)
            utm_easting.append(msg.UTM_easting)
            if first_point is None:
                first_point = (msg.UTM_easting, msg.UTM_northing)

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

# Create scatterplots for both bag files
create_scatterplot(bag_file_1, 'Scaled UTM Northing vs Scaled UTM Easting for Stationary Position')
create_scatterplot(bag_file_2, 'Scaled UTM Northing vs Scaled UTM Easting for Occluded Stationary Position')
