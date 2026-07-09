#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class WaypointFollower(Node):
    def __init__(self):
        super().__init__('waypoint_follower_node')
        self.get_logger().info('waypoint_follower_node placeholder — logic not yet implemented')

def main(args=None):
    rclpy.init(args=args)
    node = WaypointFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
