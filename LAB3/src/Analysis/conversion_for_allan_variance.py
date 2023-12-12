import pandas as pd
import rosbag

bag_file = "/home/rayyan/catkin_ws/EECE5554/lab_3/src/Data/LocationC.bag"
output_csv_file = "imu.csv"

bag = rosbag.Bag(bag_file, "r")

angular_velocities_x = [] #GyroX
angular_velocities_y = [] #GyroY
angular_velocities_z = [] #GyroZ
accelerations_x = [] 
accelerations_y = []
accelerations_z = []

for topic, msg, t in bag.read_messages(topics=['/vectornav']):
    imu_data_strings = msg.data.split('\n')

    for imu_data_string in imu_data_strings:
        if imu_data_string.startswith("$VNYMR"):
            parts = imu_data_string.split(',')
            if len(parts) >= 10:
                try:
                    # print(parts)
                    angular_velocity_x = float(parts[10])  # Clean the string
                    angular_velocity_y = float(parts[11])
                    angular_velocity_z = float(parts[12][0:-5])
                    accel_x = float(parts[7])
                    accel_y = float(parts[8])
                    accel_z = float(parts[9])
                    angular_velocities_x.append(angular_velocity_x)
                    angular_velocities_y.append(angular_velocity_y)
                    angular_velocities_z.append(angular_velocity_z)
                    accelerations_x.append(accel_x)
                    accelerations_y.append(accel_y)
                    accelerations_z.append(accel_z)

                except ValueError:
                    print(f"Skipping invalid IMU data: {imu_data_string}")
                    continue

imu_data = pd.DataFrame({'Gyro X': angular_velocities_x , 'Gyro Y': angular_velocities_y , 'Gyro Z': angular_velocities_z, 'Accel X': accelerations_x , 'Accel Y': accelerations_y , 'Accel Z': accelerations_z})

imu_data.to_csv(output_csv_file, index=False)

bag.close()

print(f"Data has been saved to {output_csv_file}")
