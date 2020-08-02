#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
PI = 3.1415926535897


def move(speed,distance,isForward,vel_msg):
    #rospy.init_node('move', anonymous=True)
    rate = rospy.Rate(10)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
   # pose_subscriber = rospy.Subscriber('turtle1/cmd_vel', Pose , update_pose)

    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        rate.sleep()

def rotate(speed,angle,clockwise, vel_msg):
    #rospy.init_node('rotate', anonymous=True)
    rate = rospy.Rate(10)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #pose_subscriber = rospy.Subscriber('turtle1/cmd_vel', Pose , update_pose)
    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
  #  rospy.spin()
    rate.sleep()

def run():
    # Testing our function
    vel_msg = Twist()
    rotate(30,60,0)
    #   time.sleep(1)
    move(1,2,1)
    #   time.sleep(1)
    rotate(30,120,1)
    #  time.sleep(1)
    move(1,2,1)
    # time.sleep(1)
    move(1,1,0)
    #time.sleep(1)
    rotate(30,120,1)
    #time.sleep(1)
    move(1,1,1)

def run_final():
    rospy.init_node('letter',anonymous = True)
    rospy.Service('move',Move, run)
    rospy.spin()


if __name__ == '__main__':
    try:
        run_final()
    except rospy.ROSInterruptException:
        pass