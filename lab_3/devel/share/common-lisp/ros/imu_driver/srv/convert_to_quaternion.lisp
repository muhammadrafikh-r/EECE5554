; Auto-generated. Do not edit!


(cl:in-package imu_driver-srv)


;//! \htmlinclude convert_to_quaternion-request.msg.html

(cl:defclass <convert_to_quaternion-request> (roslisp-msg-protocol:ros-message)
  ((euler_angles
    :reader euler_angles
    :initarg :euler_angles
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass convert_to_quaternion-request (<convert_to_quaternion-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <convert_to_quaternion-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'convert_to_quaternion-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imu_driver-srv:<convert_to_quaternion-request> is deprecated: use imu_driver-srv:convert_to_quaternion-request instead.")))

(cl:ensure-generic-function 'euler_angles-val :lambda-list '(m))
(cl:defmethod euler_angles-val ((m <convert_to_quaternion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_driver-srv:euler_angles-val is deprecated.  Use imu_driver-srv:euler_angles instead.")
  (euler_angles m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <convert_to_quaternion-request>) ostream)
  "Serializes a message object of type '<convert_to_quaternion-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'euler_angles) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <convert_to_quaternion-request>) istream)
  "Deserializes a message object of type '<convert_to_quaternion-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'euler_angles) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<convert_to_quaternion-request>)))
  "Returns string type for a service object of type '<convert_to_quaternion-request>"
  "imu_driver/convert_to_quaternionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'convert_to_quaternion-request)))
  "Returns string type for a service object of type 'convert_to_quaternion-request"
  "imu_driver/convert_to_quaternionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<convert_to_quaternion-request>)))
  "Returns md5sum for a message object of type '<convert_to_quaternion-request>"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'convert_to_quaternion-request)))
  "Returns md5sum for a message object of type 'convert_to_quaternion-request"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<convert_to_quaternion-request>)))
  "Returns full string definition for message of type '<convert_to_quaternion-request>"
  (cl:format cl:nil "geometry_msgs/Vector3 euler_angles~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'convert_to_quaternion-request)))
  "Returns full string definition for message of type 'convert_to_quaternion-request"
  (cl:format cl:nil "geometry_msgs/Vector3 euler_angles~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <convert_to_quaternion-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'euler_angles))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <convert_to_quaternion-request>))
  "Converts a ROS message object to a list"
  (cl:list 'convert_to_quaternion-request
    (cl:cons ':euler_angles (euler_angles msg))
))
;//! \htmlinclude convert_to_quaternion-response.msg.html

(cl:defclass <convert_to_quaternion-response> (roslisp-msg-protocol:ros-message)
  ((quaternion
    :reader quaternion
    :initarg :quaternion
    :type geometry_msgs-msg:Quaternion
    :initform (cl:make-instance 'geometry_msgs-msg:Quaternion)))
)

(cl:defclass convert_to_quaternion-response (<convert_to_quaternion-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <convert_to_quaternion-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'convert_to_quaternion-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imu_driver-srv:<convert_to_quaternion-response> is deprecated: use imu_driver-srv:convert_to_quaternion-response instead.")))

(cl:ensure-generic-function 'quaternion-val :lambda-list '(m))
(cl:defmethod quaternion-val ((m <convert_to_quaternion-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_driver-srv:quaternion-val is deprecated.  Use imu_driver-srv:quaternion instead.")
  (quaternion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <convert_to_quaternion-response>) ostream)
  "Serializes a message object of type '<convert_to_quaternion-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'quaternion) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <convert_to_quaternion-response>) istream)
  "Deserializes a message object of type '<convert_to_quaternion-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'quaternion) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<convert_to_quaternion-response>)))
  "Returns string type for a service object of type '<convert_to_quaternion-response>"
  "imu_driver/convert_to_quaternionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'convert_to_quaternion-response)))
  "Returns string type for a service object of type 'convert_to_quaternion-response"
  "imu_driver/convert_to_quaternionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<convert_to_quaternion-response>)))
  "Returns md5sum for a message object of type '<convert_to_quaternion-response>"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'convert_to_quaternion-response)))
  "Returns md5sum for a message object of type 'convert_to_quaternion-response"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<convert_to_quaternion-response>)))
  "Returns full string definition for message of type '<convert_to_quaternion-response>"
  (cl:format cl:nil "~%geometry_msgs/Quaternion quaternion~%~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'convert_to_quaternion-response)))
  "Returns full string definition for message of type 'convert_to_quaternion-response"
  (cl:format cl:nil "~%geometry_msgs/Quaternion quaternion~%~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <convert_to_quaternion-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'quaternion))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <convert_to_quaternion-response>))
  "Converts a ROS message object to a list"
  (cl:list 'convert_to_quaternion-response
    (cl:cons ':quaternion (quaternion msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'convert_to_quaternion)))
  'convert_to_quaternion-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'convert_to_quaternion)))
  'convert_to_quaternion-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'convert_to_quaternion)))
  "Returns string type for a service object of type '<convert_to_quaternion>"
  "imu_driver/convert_to_quaternion")