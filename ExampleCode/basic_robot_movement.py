"""
MOTOR1: Left Front Motor
MOTOR2: Left Rear Motor
MOTOR3: Right Front Motor
MOTOR4: Right Rear Motor

"""

#Start motor movement on robot with: ros2 run yahboomcar_bringup Mcnamu_driver_X3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
from rclpy.duration import Duration

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist = Twist()

    def move_robot_forward(self, duration_seconds, speed=0.07):
        self.twist.linear.x = speed
        self.twist.angular.z = 0.0

        end_time = self.get_clock().now() + Duration(seconds=duration_seconds)

        while self.get_clock().now() < end_time:
            self.publisher.publish(self.twist)
            rclpy.spin_once(self, timeout_sec=0.1)

        self.stop_robot_movement()

    #Timer helps make smooth turns 
    def robot_turn_90(self, angular_speed=0.5, clockwise=True):
        radians_to_turn = math.pi / 2
        duration_seconds = radians_to_turn / angular_speed

        self.twist.linear.x = 0.0
        self.twist.angular.z = -angular_speed if clockwise else angular_speed

        end_time = self.get_clock().now() + Duration(seconds=duration_seconds)

        while self.get_clock().now() < end_time:
            self.publisher.publish(self.twist)
            rclpy.spin_once(self, timeout_sec=0.1)

        self.stop_robot_movement()
        print("Turned 90 degrees")


    def stop_robot_movement(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self.publisher.publish(self.twist)
        print("Published stop command")

def main(args=None):
    rclpy.init(args=args)
    move_robot = MoveRobot()

    try:

        # For example - move the robot forward for 2 seconds 
        move_robot.move_robot_forward(2.0)
        

    except KeyboardInterrupt:
        move_robot.stop_robot_movement()
    finally:
        move_robot.stop_robot_movement()
        move_robot.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
