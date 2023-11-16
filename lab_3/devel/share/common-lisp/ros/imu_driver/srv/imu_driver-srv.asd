
(cl:in-package :asdf)

(defsystem "imu_driver-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "EulerToQuaternion" :depends-on ("_package_EulerToQuaternion"))
    (:file "_package_EulerToQuaternion" :depends-on ("_package"))
  ))