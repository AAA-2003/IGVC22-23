#/!/usr/bin/python3.8
'''
Package for transforming raw IMU data
1.subscribes to /imu/data
2.transforms data as setup in the transform(<>) function
3.republishes transformed IMU data as 'robot_imu' topic
'''
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu

global IMU_data #stores raw IMU data recieved from sensor
global publish_rate #rate at which IMU data has to be published


#Subscriber for raw imu data
#stores recieved data on IMU_data & calls transform
def rec(msg):
        #if(not msg.is_calibrated):
        #       rospy.loginfo("imu not calibrated!");
        #rospy.loginfo(msg.data_raw)
        #print(msg.linearAcceleration.x)
        #publish_msg(msg)
        rospy.loginfo(msg.header.frame_id)
        IMU_data.header.frame_id = msg.header.frame_id
        IMU_data.orientation.x = msg.orientation.x
        IMU_data.orientation.y = msg.orientation.y
        IMU_data.orientation.z = msg.orientation.z

        IMU_data.angular_velocity.x = msg.angular_velocity.x
        IMU_data.angular_velocity.y = msg.angular_velocity.y
        IMU_data.angular_velocity.z = msg.angular_velocity.z

        IMU_data.linear_acceleration.x = msg.linear_acceleration.x
        IMU_data.linear_acceleration.y = msg.linear_acceleration.y
        IMU_data.linear_acceleration.z = msg.linear_acceleration.z

        transform(IMU_data)

#used to transfrom Imu type data if needed
#TO BE UPDATED BASED ON FRAME OF REFERENCE FROM SENSOR
def transform(sensor_data):
        sensor_data.orientation.x += 0
        sensor_data.orientation.y += 0
        sensor_data.orientation.z += 0

        sensor_data.angular_velocity.x *= -1 #currently flips x axis (NOT NEEDED since IMU already in ENU form)
        sensor_data.angular_velocity.y += 0
        sensor_data.angular_velocity.z += 0

        sensor_data.linear_acceleration.x += 0
        sensor_data.linear_acceleration.y += 0
        sensor_data.linear_acceleration.z += 0

#publisher for transformed IMU message
#publishes at specified rate
def publish_msg():
        pub = rospy.Publisher('robot_imu', Imu, queue_size=30)
        rospy.loginfo("publisher setup- topic: /robot_imu  @"+str(publish_rate))
        rate = rospy.Rate(publish_rate)
        while not rospy.is_shutdown():
                #rospy.loginfo("published IMU data")
                pub.publish(IMU_data)
                rate.sleep()

if __name__ == '__main__':
        publish_rate = 10
        IMU_data = Imu()
        IMU_data.header.frame_id = "no init"
        rospy.init_node("robot_imu_publisher")
        rospy.Subscriber("imu/data_raw", Imu, rec)
        try:
                 publish_msg()
        except rospy.ROSInterruptException:
                rospy.loginfo("Unable to publish")
                pass
        rospy.spin()
