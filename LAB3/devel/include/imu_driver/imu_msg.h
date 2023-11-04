// Generated by gencpp from file imu_driver/imu_msg.msg
// DO NOT EDIT!


#ifndef IMU_DRIVER_MESSAGE_IMU_MSG_H
#define IMU_DRIVER_MESSAGE_IMU_MSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <sensor_msgs/Imu.h>
#include <sensor_msgs/MagneticField.h>

namespace imu_driver
{
template <class ContainerAllocator>
struct imu_msg_
{
  typedef imu_msg_<ContainerAllocator> Type;

  imu_msg_()
    : Header()
    , IMU()
    , MagField()
    , raw()  {
    }
  imu_msg_(const ContainerAllocator& _alloc)
    : Header(_alloc)
    , IMU(_alloc)
    , MagField(_alloc)
    , raw(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _Header_type;
  _Header_type Header;

   typedef  ::sensor_msgs::Imu_<ContainerAllocator>  _IMU_type;
  _IMU_type IMU;

   typedef  ::sensor_msgs::MagneticField_<ContainerAllocator>  _MagField_type;
  _MagField_type MagField;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _raw_type;
  _raw_type raw;





  typedef boost::shared_ptr< ::imu_driver::imu_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::imu_driver::imu_msg_<ContainerAllocator> const> ConstPtr;

}; // struct imu_msg_

typedef ::imu_driver::imu_msg_<std::allocator<void> > imu_msg;

typedef boost::shared_ptr< ::imu_driver::imu_msg > imu_msgPtr;
typedef boost::shared_ptr< ::imu_driver::imu_msg const> imu_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::imu_driver::imu_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::imu_driver::imu_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::imu_driver::imu_msg_<ContainerAllocator1> & lhs, const ::imu_driver::imu_msg_<ContainerAllocator2> & rhs)
{
  return lhs.Header == rhs.Header &&
    lhs.IMU == rhs.IMU &&
    lhs.MagField == rhs.MagField &&
    lhs.raw == rhs.raw;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::imu_driver::imu_msg_<ContainerAllocator1> & lhs, const ::imu_driver::imu_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace imu_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::imu_driver::imu_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::imu_driver::imu_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::imu_driver::imu_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::imu_driver::imu_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::imu_driver::imu_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::imu_driver::imu_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::imu_driver::imu_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "adf4a68813b79eebfd5a91db0f9b4d2c";
  }

  static const char* value(const ::imu_driver::imu_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xadf4a68813b79eebULL;
  static const uint64_t static_value2 = 0xfd5a91db0f9b4d2cULL;
};

template<class ContainerAllocator>
struct DataType< ::imu_driver::imu_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "imu_driver/imu_msg";
  }

  static const char* value(const ::imu_driver::imu_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::imu_driver::imu_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header Header\n"
"sensor_msgs/Imu IMU\n"
"sensor_msgs/MagneticField MagField\n"
"string raw\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/Imu\n"
"# This is a message to hold data from an IMU (Inertial Measurement Unit)\n"
"#\n"
"# Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec\n"
"#\n"
"# If the covariance of the measurement is known, it should be filled in (if all you know is the \n"
"# variance of each measurement, e.g. from the datasheet, just put those along the diagonal)\n"
"# A covariance matrix of all zeros will be interpreted as \"covariance unknown\", and to use the\n"
"# data a covariance will have to be assumed or gotten from some other source\n"
"#\n"
"# If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an orientation \n"
"# estimate), please set element 0 of the associated covariance matrix to -1\n"
"# If you are interpreting this message, please check for a value of -1 in the first element of each \n"
"# covariance matrix, and disregard the associated estimate.\n"
"\n"
"Header header\n"
"\n"
"geometry_msgs/Quaternion orientation\n"
"float64[9] orientation_covariance # Row major about x, y, z axes\n"
"\n"
"geometry_msgs/Vector3 angular_velocity\n"
"float64[9] angular_velocity_covariance # Row major about x, y, z axes\n"
"\n"
"geometry_msgs/Vector3 linear_acceleration\n"
"float64[9] linear_acceleration_covariance # Row major x, y z \n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"================================================================================\n"
"MSG: sensor_msgs/MagneticField\n"
" # Measurement of the Magnetic Field vector at a specific location.\n"
"\n"
" # If the covariance of the measurement is known, it should be filled in\n"
" # (if all you know is the variance of each measurement, e.g. from the datasheet,\n"
" #just put those along the diagonal)\n"
" # A covariance matrix of all zeros will be interpreted as \"covariance unknown\",\n"
" # and to use the data a covariance will have to be assumed or gotten from some\n"
" # other source\n"
"\n"
"\n"
" Header header                        # timestamp is the time the\n"
"                                      # field was measured\n"
"                                      # frame_id is the location and orientation\n"
"                                      # of the field measurement\n"
"\n"
" geometry_msgs/Vector3 magnetic_field # x, y, and z components of the\n"
"                                      # field vector in Tesla\n"
"                                      # If your sensor does not output 3 axes,\n"
"                                      # put NaNs in the components not reported.\n"
"\n"
" float64[9] magnetic_field_covariance # Row major about x, y, z axes\n"
"                                      # 0 is interpreted as variance unknown\n"
;
  }

  static const char* value(const ::imu_driver::imu_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::imu_driver::imu_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Header);
      stream.next(m.IMU);
      stream.next(m.MagField);
      stream.next(m.raw);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct imu_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::imu_driver::imu_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::imu_driver::imu_msg_<ContainerAllocator>& v)
  {
    s << indent << "Header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.Header);
    s << indent << "IMU: ";
    s << std::endl;
    Printer< ::sensor_msgs::Imu_<ContainerAllocator> >::stream(s, indent + "  ", v.IMU);
    s << indent << "MagField: ";
    s << std::endl;
    Printer< ::sensor_msgs::MagneticField_<ContainerAllocator> >::stream(s, indent + "  ", v.MagField);
    s << indent << "raw: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.raw);
  }
};

} // namespace message_operations
} // namespace ros

#endif // IMU_DRIVER_MESSAGE_IMU_MSG_H
