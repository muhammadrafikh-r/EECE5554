; Auto-generated. Do not edit!


(cl:in-package imu_driver-srv)


;//! \htmlinclude EulerToQuaternion-request.msg.html

(cl:defclass <EulerToQuaternion-request> (roslisp-msg-protocol:ros-message)
  ((euler_angles
    :reader euler_angles
    :initarg :euler_angles
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass EulerToQuaternion-request (<EulerToQuaternion-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EulerToQuaternion-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EulerToQuaternion-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imu_driver-srv:<EulerToQuaternion-request> is deprecated: use imu_driver-srv:EulerToQuaternion-request instead.")))

(cl:ensure-generic-function 'euler_angles-val :lambda-list '(m))
(cl:defmethod euler_angles-val ((m <EulerToQuaternion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_driver-srv:euler_angles-val is deprecated.  Use imu_driver-srv:euler_angles instead.")
  (euler_angles m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EulerToQuaternion-request>) ostream)
  "Serializes a message object of type '<EulerToQuaternion-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'euler_angles) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EulerToQuaternion-request>) istream)
  "Deserializes a message object of type '<EulerToQuaternion-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'euler_angles) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EulerToQuaternion-request>)))
  "Returns string type for a service object of type '<EulerToQuaternion-request>"
  "imu_driver/EulerToQuaternionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EulerToQuaternion-request)))
  "Returns string type for a service object of type 'EulerToQuaternion-request"
  "imu_driver/EulerToQuaternionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EulerToQuaternion-request>)))
  "Returns md5sum for a message object of type '<EulerToQuaternion-request>"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EulerToQuaternion-request)))
  "Returns md5sum for a message object of type 'EulerToQuaternion-request"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EulerToQuaternion-request>)))
  "Returns full string definition for message of type '<EulerToQuaternion-request>"
  (cl:format cl:nil "geometry_msgs/Vector3 euler_angles~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EulerToQuaternion-request)))
  "Returns full string definition for message of type 'EulerToQuaternion-request"
  (cl:format cl:nil "geometry_msgs/Vector3 euler_angles~%~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EulerToQuaternion-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'euler_angles))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EulerToQuaternion-request>))
  "Converts a ROS message object to a list"
  (cl:list 'EulerToQuaternion-request
    (cl:cons ':euler_angles (euler_angles msg))
))
;//! \htmlinclude EulerToQuaternion-response.msg.html

(cl:defclass <EulerToQuaternion-response> (roslisp-msg-protocol:ros-message)
  ((quaternion
    :reader quaternion
    :initarg :quaternion
    :type geometry_msgs-msg:Quaternion
    :initform (cl:make-instance 'geometry_msgs-msg:Quaternion)))
)

(cl:defclass EulerToQuaternion-response (<EulerToQuaternion-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EulerToQuaternion-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EulerToQuaternion-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imu_driver-srv:<EulerToQuaternion-response> is deprecated: use imu_driver-srv:EulerToQuaternion-response instead.")))

(cl:ensure-generic-function 'quaternion-val :lambda-list '(m))
(cl:defmethod quaternion-val ((m <EulerToQuaternion-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_driver-srv:quaternion-val is deprecated.  Use imu_driver-srv:quaternion instead.")
  (quaternion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EulerToQuaternion-response>) ostream)
  "Serializes a message object of type '<EulerToQuaternion-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'quaternion) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EulerToQuaternion-response>) istream)
  "Deserializes a message object of type '<EulerToQuaternion-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'quaternion) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EulerToQuaternion-response>)))
  "Returns string type for a service object of type '<EulerToQuaternion-response>"
  "imu_driver/EulerToQuaternionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EulerToQuaternion-response)))
  "Returns string type for a service object of type 'EulerToQuaternion-response"
  "imu_driver/EulerToQuaternionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EulerToQuaternion-response>)))
  "Returns md5sum for a message object of type '<EulerToQuaternion-response>"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EulerToQuaternion-response)))
  "Returns md5sum for a message object of type 'EulerToQuaternion-response"
  "48653d5a466e82f3531a42dc323eefb0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EulerToQuaternion-response>)))
  "Returns full string definition for message of type '<EulerToQuaternion-response>"
  (cl:format cl:nil "~%geometry_msgs/Quaternion quaternion~%~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EulerToQuaternion-response)))
  "Returns full string definition for message of type 'EulerToQuaternion-response"
  (cl:format cl:nil "~%geometry_msgs/Quaternion quaternion~%~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EulerToQuaternion-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'quaternion))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EulerToQuaternion-response>))
  "Converts a ROS message object to a list"
  (cl:list 'EulerToQuaternion-response
    (cl:cons ':quaternion (quaternion msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'EulerToQuaternion)))
  'EulerToQuaternion-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'EulerToQuaternion)))
  'EulerToQuaternion-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EulerToQuaternion)))
  "Returns string type for a service object of type '<EulerToQuaternion>"
  "imu_driver/EulerToQuaternion")