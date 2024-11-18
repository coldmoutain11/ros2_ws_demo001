import rclpy
from rclpy.node import Node
 
def main(args=None):
    rclpy.init(args=args) # init rclpy
    my_node = Node("node_001")  # to create a Node object
    my_node.get_logger().info("hello，I am node_001")  # to print a message.
    rclpy.spin(my_node) # to keep Node running
    rclpy.shutdown() # to close Node
