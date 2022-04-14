# Warmup_Project | Hamlet Fernandez


# Drive in Square
*The task for this part of the assignment is to program teh turtlebot to drive in a square indefinitely. My immediate thought upon reading the task was to use the same approach as spin in a circle. I used a lot of the same code from our spin in a circle lab but added logic to support 90 degree turns instead of a constant angular velocity.*

## Functions
DriveInSquare (object) This object houses the entire module. It initializes the node and the rospy.Publisher such that we can send messages to the rostopic /cmd_vel. It also defines two methods, turn() and run() which act as the main bodies of our implementation. More details on then below:

turn() simply turns the robot. It is a function designed to abstract the turtlebot turning 90 degrees. It is not a function meant to be ran alone, however. Rather, it is called by run() after the robot drives a fixed distance. To turn the turtlebot, turn() changes the robots angular velocity while setting the linear velocity to 0. The goal of these changes is to have the robot turn left in place. 

run() acts as our while loop that keeps the robot moving indefinitely. It tells the robot to drive a fixed distance, calls turn() to create our corner edges of our square, and the loop inherently alternates these two processes. 

## GIF

## Challenges
The main challenge of this task was figuring how to turn the robot preciesely 90 degrees. I was comfortable changing and setting the turtlebots linear and angular velocities from our class's labs. As such, I was able to rely on familar code structure. My initial attempts at getting the robot to turn 90 degrees included using sleep to "turn off" certain functionality. For example, after the turtlebot had driven with a linear velocity of x = 1 and angular velocity of 0 for 3 seconds, I would call sleep, flip the velcoities, wait another 3 seconds, and repeat. Using time to measure 90 degree angles was difficult and imprecise- I did not have a way to correlate angular velocity to angles in the moment. 

## Future Work

## Takeaways
### one

### two

# Person Follower
*The task for this part of the warmup project was to program the turtlebot folowing a moving person. As part of the specifications, the person could be moving to the front, side, or behind the turtlebot. As recommended, I planned on subscribing to the turtlebot's integrated scan topic and LaserScan sensory msgs.*

## Functions
Like usual, I have a class object, PersonFollower, that houses all of the code. Granted, I'm not that experienced in python yet so a lot of my strategies so far involve copy and pasting structure from my previous assignments. PersonFollower is initalied with its node 'person_follower_node' and a publisher self.follow_pub() to the '/cmd_vel' topic alongside a subscriber to the '/scan' topic. 
When initializing, I set variables I planned to use to drive the turtlebot. Variables like forwardSpeed, turnSpeed, and methods like forwardCommand, turnLeftCommand, turnRightCommand were set to then be used inside robot_scan_received();

robot_scan_received(self, data) is a method designed for the turtlebot to read and respond to the scanner. The data received from the scanner (after a simple "print(data)") contains the header, angle_min, angle_max, angle_increment, scan_time, range_min, range_max, ranges, and intensities properties. At first glance, I isolated the ranges as I thought they'd be important. In gazebo, I generated a cylinder and placed it at various points around the turtlebot. The ranges consequently changed to include values between 0 and 3.5 depending on how close or far away I placed the cylinder.

I also realized that the scan object defined a circle around the turtlebot with indices of the ranges[] list representing roughly all 360 angles that can be scanned. As such, my initial attempt to isolate what's considered "forward" for the turtlebot was to define a forward minimum (I chose 45 degrees) and a forward maximum (I chose 135 degrees). I thought that these would be computed as forward_range_min = np.pi  / (4 * data.angle_increment)
forward_range_max = (3 * np.pi) / (4 * data.angle_increment). 

My goal with these values was to include logic that programmed the robot to drive forward when values in the forward range were between 1 and 3.5 nd to turn right otherwise. I figured I'd choose 1 as the minimum to  have the robot stop driving forward 1 m(?) away from the person if the person had stopped moving. When the person moved away from these forward ranged I would then program the turtlebot to turn right until it finds the person again. 

It is for thsi reason I wanted to put the response, publishing to twist, inside robot_scan_received() such that whe the robot searches for the person, it can respond quickly as soon as the forward ranged are filled with valid values. 

## GIF

## Challenges
What i thougth would be correct forward values were not! The values I computed for 45 degrees and 135 degrees gave me a valid section of the ranges list but when I placed a cylinder in front of the turtlebot in gazebo the values did not change. In fact, when I placed teh cylinder towards the left and teh back of the turtlebot the values changed. I then started thinking I might have had the orientation of the turtlebot confused where 0 degrees may not have been to the immediat right of the turtlebot. My second attempt included 0 degrees immediately to the front of the robot (rotating everyting counterclockwise). I then tried to compute 45 degrees and -45 degrees (360 - 45). This is where forward_range_min = np.pi  / (4 * data.angle_increment)
        forward_range_max = ((2 * np.pi) / data.angle_increment) - forward_range_min comes from. These values did not really work either.  

## Future Work 

## Takeaways
### one
The scanner is pretty cool and grbabing data from ranges is very intuitive. Even if I didn't finish, I want to keep learning more about the scan topic and see what it can do. 

### two

# Wall Follower
* This task of the warmup project focused on programming the turtlebot to follow a wall instead of a person. For this assignment, I would have used the scan topic to pick a fixed distance from the wall (1 m as the minimum and maximum range) then publish a forward velocity to Twist while the range was constant. At the same time, if the ranges at the forward indicies reached 1m, I would turn left or right depending on if the wall was on the robots right or left. This could be determined depending on where the 1's are in the range list. 

## Functions


## GIF

## Challenges

## Future Work

## Takeaways
### one

### two
