;; Auto-generated. Do not edit!


(when (boundp 'imu_driver::EulerToQuaternion)
  (if (not (find-package "IMU_DRIVER"))
    (make-package "IMU_DRIVER"))
  (shadow 'EulerToQuaternion (find-package "IMU_DRIVER")))
(unless (find-package "IMU_DRIVER::EULERTOQUATERNION")
  (make-package "IMU_DRIVER::EULERTOQUATERNION"))
(unless (find-package "IMU_DRIVER::EULERTOQUATERNIONREQUEST")
  (make-package "IMU_DRIVER::EULERTOQUATERNIONREQUEST"))
(unless (find-package "IMU_DRIVER::EULERTOQUATERNIONRESPONSE")
  (make-package "IMU_DRIVER::EULERTOQUATERNIONRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass imu_driver::EulerToQuaternionRequest
  :super ros::object
  :slots (_euler_angles ))

(defmethod imu_driver::EulerToQuaternionRequest
  (:init
   (&key
    ((:euler_angles __euler_angles) (instance geometry_msgs::Vector3 :init))
    )
   (send-super :init)
   (setq _euler_angles __euler_angles)
   self)
  (:euler_angles
   (&rest __euler_angles)
   (if (keywordp (car __euler_angles))
       (send* _euler_angles __euler_angles)
     (progn
       (if __euler_angles (setq _euler_angles (car __euler_angles)))
       _euler_angles)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Vector3 _euler_angles
    (send _euler_angles :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Vector3 _euler_angles
       (send _euler_angles :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Vector3 _euler_angles
     (send _euler_angles :deserialize buf ptr-) (incf ptr- (send _euler_angles :serialization-length))
   ;;
   self)
  )

(defclass imu_driver::EulerToQuaternionResponse
  :super ros::object
  :slots (_quaternion ))

(defmethod imu_driver::EulerToQuaternionResponse
  (:init
   (&key
    ((:quaternion __quaternion) (instance geometry_msgs::Quaternion :init))
    )
   (send-super :init)
   (setq _quaternion __quaternion)
   self)
  (:quaternion
   (&rest __quaternion)
   (if (keywordp (car __quaternion))
       (send* _quaternion __quaternion)
     (progn
       (if __quaternion (setq _quaternion (car __quaternion)))
       _quaternion)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Quaternion _quaternion
    (send _quaternion :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Quaternion _quaternion
       (send _quaternion :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Quaternion _quaternion
     (send _quaternion :deserialize buf ptr-) (incf ptr- (send _quaternion :serialization-length))
   ;;
   self)
  )

(defclass imu_driver::EulerToQuaternion
  :super ros::object
  :slots ())

(setf (get imu_driver::EulerToQuaternion :md5sum-) "48653d5a466e82f3531a42dc323eefb0")
(setf (get imu_driver::EulerToQuaternion :datatype-) "imu_driver/EulerToQuaternion")
(setf (get imu_driver::EulerToQuaternion :request) imu_driver::EulerToQuaternionRequest)
(setf (get imu_driver::EulerToQuaternion :response) imu_driver::EulerToQuaternionResponse)

(defmethod imu_driver::EulerToQuaternionRequest
  (:response () (instance imu_driver::EulerToQuaternionResponse :init)))

(setf (get imu_driver::EulerToQuaternionRequest :md5sum-) "48653d5a466e82f3531a42dc323eefb0")
(setf (get imu_driver::EulerToQuaternionRequest :datatype-) "imu_driver/EulerToQuaternionRequest")
(setf (get imu_driver::EulerToQuaternionRequest :definition-)
      "geometry_msgs/Vector3 euler_angles


================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
---

geometry_msgs/Quaternion quaternion


================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")

(setf (get imu_driver::EulerToQuaternionResponse :md5sum-) "48653d5a466e82f3531a42dc323eefb0")
(setf (get imu_driver::EulerToQuaternionResponse :datatype-) "imu_driver/EulerToQuaternionResponse")
(setf (get imu_driver::EulerToQuaternionResponse :definition-)
      "geometry_msgs/Vector3 euler_angles


================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
---

geometry_msgs/Quaternion quaternion


================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")



(provide :imu_driver/EulerToQuaternion "48653d5a466e82f3531a42dc323eefb0")


