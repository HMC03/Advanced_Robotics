import rclpy
import math

from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class DrawN(Node):

    def __init__(self):
        super().__init__('DrawN')

        # CMD_VEL Publisher Setup
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.drawN)

        # Pose Subscriber Setup
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose_sub  # prevent unused variable warning

        # Initialize Current Pose Value
        self.current_pose = None

        # Define Waypoints making up the 'N'
        self.waypoints = [(5.0, 5.0), (5.0, 8.0), (6.0, 8.0), (8.0, 6.0), (8.0, 8.0), (9.0, 8.0), (9.0, 5.0), (8.0, 5.0), (6.0, 7.0), (6.0, 5.0), (5.0, 5.0)]
        self.current_wp_index = 0

    def pose_callback(self, msg: Pose):
        self.current_pose = msg
        # self.get_logger().info(
        #     f"Pose -> x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}"
        # )

    def drawN(self):
        if self.current_pose is None:
            return  # wait until we have pose

        # Distance Calculations
        target_x, target_y = self.waypoints[self.current_wp_index]
        dx = target_x - self.current_pose.x
        dy = target_y - self.current_pose.y
        distance = math.sqrt(dx*dx + dy*dy)

        # Reached waypoint Bypass
        if(distance < 0.1):
            self.get_logger().info(f"Reached waypoint {self.current_wp_index+1}")
            self.current_wp_index = (self.current_wp_index + 1) % len(self.waypoints)
            return
        
        # Angle Calculations
        target_theta = math.atan2(dy, dx)
        angle_diff = target_theta - self.current_pose.theta
        angle_diff = math.atan2(math.sin(angle_diff), math.cos(angle_diff))
        direction = 1 if angle_diff >= 0 else -1

        # Set Twist Command
        twist = Twist()
        if abs(angle_diff) > 0.1:
            # Rotate towards target
            twist.angular.z = 1.0 * direction
        else:
            # Move forward
            twist.linear.x = 1.0

        self.cmd_vel_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)

    draw_n = DrawN()
    
    rclpy.spin(draw_n)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    draw_n.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()