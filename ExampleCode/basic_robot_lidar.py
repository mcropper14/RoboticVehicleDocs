import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# Start Lidar with: ros2 launch sllidar_Ros2 sllidar_s2_launch.py
# Will depend on the model of the robot 

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist = Twist()
        self.lidar_subscriber = self.create_subscription(LaserScan, 'scan', self.lidar_callback, 10)
        self.object_detected = False

    def lidar_callback(self, msg):
        min_distance = min(msg.ranges)
        print(min_distance)
        if min_distance < 0.23:  # You can adjust the values
            self.object_detected = True
            self.stop_robot()
        else:
            self.object_detected = False
            self.move_robot_forward()

    def move_robot_forward(self):
        # Command to move the robot forward
        #Simple, not great movement just for testing
        #basic_robot_movement.py has better movement
        self.twist.linear.x = 0.07  
        self.publisher.publish(self.twist)
        print("Published forward command")

    def stop_robot(self):
        # Command to stop the robot
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self.publisher.publish(self.twist)
        print("Published stop command")

def main(args=None):
    rclpy.init(args=args)
    move_robot = MoveRobot()
    rclpy.spin(move_robot)
    move_robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
