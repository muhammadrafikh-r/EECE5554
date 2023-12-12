// Auto-generated. Do not edit!

// (in-package imu_driver.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class convert_to_quaternionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.euler_angles = null;
    }
    else {
      if (initObj.hasOwnProperty('euler_angles')) {
        this.euler_angles = initObj.euler_angles
      }
      else {
        this.euler_angles = new geometry_msgs.msg.Vector3();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type convert_to_quaternionRequest
    // Serialize message field [euler_angles]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.euler_angles, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type convert_to_quaternionRequest
    let len;
    let data = new convert_to_quaternionRequest(null);
    // Deserialize message field [euler_angles]
    data.euler_angles = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'imu_driver/convert_to_quaternionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '01954336000a228e12c0ea86ec76073a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Vector3 euler_angles
    
    
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
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new convert_to_quaternionRequest(null);
    if (msg.euler_angles !== undefined) {
      resolved.euler_angles = geometry_msgs.msg.Vector3.Resolve(msg.euler_angles)
    }
    else {
      resolved.euler_angles = new geometry_msgs.msg.Vector3()
    }

    return resolved;
    }
};

class convert_to_quaternionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.quaternion = null;
    }
    else {
      if (initObj.hasOwnProperty('quaternion')) {
        this.quaternion = initObj.quaternion
      }
      else {
        this.quaternion = new geometry_msgs.msg.Quaternion();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type convert_to_quaternionResponse
    // Serialize message field [quaternion]
    bufferOffset = geometry_msgs.msg.Quaternion.serialize(obj.quaternion, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type convert_to_quaternionResponse
    let len;
    let data = new convert_to_quaternionResponse(null);
    // Deserialize message field [quaternion]
    data.quaternion = geometry_msgs.msg.Quaternion.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a service object
    return 'imu_driver/convert_to_quaternionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c3d2506862045c1ddfbe5c9ef23688f4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    geometry_msgs/Quaternion quaternion
    
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new convert_to_quaternionResponse(null);
    if (msg.quaternion !== undefined) {
      resolved.quaternion = geometry_msgs.msg.Quaternion.Resolve(msg.quaternion)
    }
    else {
      resolved.quaternion = new geometry_msgs.msg.Quaternion()
    }

    return resolved;
    }
};

module.exports = {
  Request: convert_to_quaternionRequest,
  Response: convert_to_quaternionResponse,
  md5sum() { return '48653d5a466e82f3531a42dc323eefb0'; },
  datatype() { return 'imu_driver/convert_to_quaternion'; }
};
