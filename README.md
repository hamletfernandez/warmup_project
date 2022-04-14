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
*The task for this part of the assignment is to program teh turtlebot to drive in a square indefinitely. My immediate thought upon reading the task was to use the same approach as spin in a circle. I used a lot of the same code from our spin in a circle lab but added logic to support 90 degree turns instead of a constant angular velocity.*

## Functions



## GIF

## Challenges


## Future Work

## Takeaways
### one

### two

# Wall Follower


## Functions


## GIF

## Challenges

## Future Work

## Takeaways
### one

### two
