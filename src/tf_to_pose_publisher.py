#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class TfToPosePublisher(Node):
    def __init__(self):
        super().__init__('tf_to_pose_publisher')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        self.publisher = self.create_publisher(PoseStamped, '/robot_pose', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('tf_to_pose_publisher started')
        
    def timer_callback(self):
        try:
            # Look up transform from map to base_footprint
            t = self.tf_buffer.lookup_transform(
                'map',
                'base_footprint',
                rclpy.time.Time()
            )
            
            msg = PoseStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'map'
            msg.pose.position.x = t.transform.translation.x
            msg.pose.position.y = t.transform.translation.y
            msg.pose.position.z = t.transform.translation.z
            msg.pose.orientation = t.transform.rotation
            
            self.publisher.publish(msg)
            
        except TransformException as ex:
            # Throttle logging to avoid cluttering output
            self.get_logger().info(
                f'Waiting for map to base_footprint transform: {ex}',
                throttle_duration_sec=5.0
            )

def main(args=None):
    rclpy.init(args=args)
    node = TfToPosePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
