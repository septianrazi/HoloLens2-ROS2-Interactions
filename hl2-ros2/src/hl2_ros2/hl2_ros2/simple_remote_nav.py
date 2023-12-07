import time
from flask import Flask, request
import threading
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

app = Flask(__name__)

class MoveTurtlebot(Node):

    def __init__(self):
        super().__init__('move_turtlebot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.stopped = False

    def move_forward(self):
        msg = Twist()
        msg.linear.x = 0.5
        
        while not self.stopped:
            self.publisher_.publish(msg)
            time.sleep(0.1)
        
        msg.linear.x = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Moving Turtlebot4 forward')

    def move_backward(self):
        msg = Twist()
        msg.linear.x = -0.5
        self.publisher_.publish(msg)
        self.get_logger().info('Moving Turtlebot4 backward')

    def turn_left(self):
        msg = Twist()
        msg.angular.z = 0.5
        while not self.stopped:
            self.publisher_.publish(msg)
            time.sleep(0.1)
        
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Moving Turtlebot4 forward')

    def turn_right(self):
        msg = Twist()
        msg.angular.z = -0.5
        while not self.stopped:
            self.publisher_.publish(msg)
            time.sleep(0.1)
        
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Moving Turtlebot4 forward')
        
    def stop_movement(self):
        self.stopped = True
        time.sleep(0.3)
        self.stopped = False
    

@app.route('/move_forward', methods=['POST', 'GET'])
def move_forward():
    node.move_forward()
    return 'Success', 200

@app.route('/move_backward', methods=['POST', 'GET'])
def move_backward():
    node.move_backward()
    return 'Success', 200

@app.route('/turn_left', methods=['POST', 'GET'])
def turn_left():
    node.turn_left()
    return 'Success', 200

@app.route('/turn_right', methods=['POST', 'GET'])
def turn_right():
    node.turn_right()
    return 'Success', 200

@app.route('/stop', methods=['POST', 'GET'])
def stop():
    node.stop_movement()
    return 'Success', 200

def flask_thread():
    app.run(host='0.0.0.0', port=5000)


def main(args=None):
    global node
    rclpy.init(args=args)

    node = MoveTurtlebot()

    thread = threading.Thread(target=flask_thread)
    thread.start()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
