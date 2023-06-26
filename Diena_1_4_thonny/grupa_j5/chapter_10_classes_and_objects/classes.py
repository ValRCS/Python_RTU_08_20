# let's talk about classes and objects in Python

# first of all everything in Python is an object (almost everything)
# you do not have to program in object oriented way
# but it is very useful to know about objects

# class is a blueprint for creating objects

# classes -> combine data and functionality
# objects -> instances of classes / actual realizations of classes
# Docs: https://docs.python.org/3/tutorial/classes.html


# let's imagine I want to build a robot
# how would I store the data about the robot?
# how about the functionality of the robot?

# i could use a dictionary to store data about the robot
# i could use functions to store functionality of the robot

robot_dict = {
    "name": "Robby",
    "color": "red",
    "weight": 30,
    "height": 100,
    "speed": 10,
    "direction": 0
    }

def move_forward(robot, distance=1):
    robot["direction"] += distance # 1 by default
    print("Robot moved forward")
    # no need to return anything because we are changing the robot dictionary

# in the above example we have data and functionality separated
# in larger projects this can become a problem - we need to keep track of data and functionality separately

# let's try to combine data and functionality into a class
# let's start with super simple SimpleRobot class - no init, just one method
class SimpleRobot:
    def move_forward(self, action):
        print(f"Robot performed {action} action")

# let's create an object from the class
mini_robot = SimpleRobot()
# let's call the method on the object
# mini_robot.move_forward("forward")
# # i could assign some data / properties to this object
# mini_robot.name = "Mini"
# mini_robot.color = "blue"
# # but this gets tedious very quickly
# # we lose the benefit of having data and functionality combined

# # i could even add a new method to the object
# def move_backward(action):
#     """Regular function that takes action as input"""
#     print(f"Robot performed {action} action")
# mini_robot.move_backward = move_backward # this is reference to the function not calling it

# mini_robot.move_backward("backward") # works, but not very elegant

# let's talk about composition
# our robot could consist of many parts
# let's make a new class for a robot part
class RobotHead:
    def __init__(self, eye_color="black", shape="round", eyes=2):
        self.color = eye_color
        self.shape = shape
        self.eyes = eyes
        print(f"New head created with color {self.color}, shape {self.shape} and {self.eyes} eyes")

    def describe_myself(self):
        print(f"I am a {self.color} {self.shape} with {self.eyes} eyes")
        return self

    def blink(self):
        print("Blinking")
        # insert call to actual hardware here
        return self # again we return self so we can chain methods
    # we do this when we do not need to return anything else

    def look_around(self):
        print("Looking around")
        return self


class Robot:

    # __init__ is a special method that is called 
    # when we create an object from the class
    # __ are so called dunder methods - double underscore
    # list of all __ methods: https://docs.python.org/3/reference/datamodel.html#special-method-names
    def __init__(self, name="unknown", color="metallic", weight=50, height=60, speed=100, x=0, y=0):
        # here we put everything that we want to happen when we create an object
        print("Creating a robot")
        self.name = name
        self.color = color
        self.weight = weight
        self.height = height
        # for names that are for internal use only we use single underscore
        # for example _speed
        # this does not prevent us from accessing the attribute from outside
        # simply a convention - hey, this is for internal use only
        self._speed = speed
        self.y = y
        self.x = x
        self.head = RobotHead(eye_color="blue")
   

        self.__secret_password = "1234" # this is private attribute, cannot be accessed from outside
        # note the double underscore in front of the attribute name
        # the name is mangled - it is changed to _Robot__secret_password
        # technically it is still possible to access it from outside but it is not recommended
        print(f"Robot {self.name} created")
        print("Properties:")
        print(self.__dict__)

    def move_forward(self, distance=1):
        self.y += distance
        # if I am not returning anything, I might as well return self
        # this way I can chain methods
        return self

    def describe_myself(self):
        print(f"Hi, I am {self.name} and I am {self.color}")
        return self

    def print_my_location(self):
        print(f"My location is {self.x}, {self.y}")
        return self
    
    # i could add read sensors method
    def read_sensors(self):
        print("Reading sensors")
        # here would be real code call to harware sensors
        # emulator
        import random
        self._speed = random.randint(0, 150) # random speed between 0 and 150
        return self._speed # notice not self
    
    def get_password(self):
        # so called getter method
        # here would go code to check if the password is correct
        # whether the robot is allowed to read the password etc
        print("Password is", self.__secret_password)
        return self.__secret_password
    
    def set_password(self, new_password):
        # so called setter method
        # here would go code to check if the password is correct
        # whether the robot is allowed to change the password etc
        # check validity of the new password
        if len(new_password) < 4: # very simple check
            print("Password too short")
            return self
        self.__secret_password = new_password
        print("Password changed")
        return self # so we can chain methods

    def __str__(self):
        # so whenever we print the object, this method is called
        # we override the default __str__ method which was basically useless
        return f"Robot {self.name} with color {self.color} at location {self.x}, {self.y}"
    # i could return anything in __str__ method as long as it is a string

    # let's make a method that will allows us to add two robots together
    def __add__(self, other_robot):
        # we are overriding the default __add__ method for + operator
        # so new name will be Mega + original name + name of the other robot
        new_name = "Mega" + self.name + other_robot.name
        # new speed will be average of the two robots
        new_speed = (self._speed + other_robot._speed) / 2
        return Robot(name=new_name, speed=new_speed) # return new robot

# again nothing is happening here because we are just defining the class

# let's create an object from the class
robbie = Robot("Robbie", "red", 30, 100, 10)
# # let's check what type of object robbie is
# print(type(robbie))

# # let's check what attributes robbie has
# print(robbie.__dict__) # turns out robbie attributes are stored in a dictionary

# # let's check what methods robbie has
# print(dir(robbie)) # turns out robbie methods are stored in a list

# # i can print some of the attributes of robbie
# print(robbie.name)
# print(robbie.color)

# i could create another robot
maggie = Robot(name="Maggie", 
               color="blue", 
               weight=40, 
               height=120, 
               speed=20) # i could use named arguments for clarity
maggie.describe_myself()

# how about Bender?
bender = Robot("Bender", "gold", 100, 200, 50)
bender.describe_myself() # notice no need to pass self as argument! it is automatically passed
# i could even create robot with no arguments
anonymous_robot = Robot()
anonymous_robot.describe_myself()

# i could even creata  list of new robots
robots = []
for i in range(10):
    robots.append(Robot(name=f"Robot_{i}"))

# let's move bender forward
bender.move_forward(10)
bender.print_my_location()
bender.move_forward(-4)
bender.print_my_location()

print(mini_robot) # this is not very useful, just shows memory location
print(bender) # now this should be useful

# now I can chain those methods that return self
bender.move_forward(10).print_my_location().describe_myself().move_forward(15).print_my_location()

# again I can read any attribute of the object as long as it is not private
print(bender.name)
print(bender.color)
print(bender.weight)
# print(bender.__secret_password) # this will not work
# instead we need to use the method that returns the password
bender.get_password()

# i can even change the password
bender.set_password("new_password").get_password()
bender.set_password("123").get_password() # this will not change because the password is too short
# note set_password returns self so I can chain methods
# read_password returns the password so my chain is broken

monster_robot = bender + robbie # possible because we have defined __add__ method
print(monster_robot)

# so i could keep making new methods and attributes

# but what if I want to make a new class that is very similar to Robot?

# let's make a new class that inherits from Robot
class SuperRobot(Robot): # notice Robot in parentheses
    # this means that SuperRobot everything that Robot has
    # it is possible to define __init__ method again
    # however that is not required
    # it would inolve calling the __init__ method of the parent class - a bit more advanced
    # instead we are just using the __init__ method of the parent class- Robot

    # and we can add new methods and attributes
    def super_move_forward(self, distance=1):
        self.y += distance
        self.x += distance
        return self
    
# in real life inheritance is not always the best solution
# composition is often better

# let's make a super robot
super_robot = SuperRobot("SuperRobot", "green", 100, 200, 50)

# super robot can do anything robot can do
super_robot.move_forward(10).print_my_location().describe_myself()
# only new ability is super_move_forward
super_robot.super_move_forward(15).print_my_location().describe_myself()

super_robot.head.blink().describe_myself() # describe_myself is from RobotHead class
super_robot.describe_myself() # describe_myself is from SuperRobot class

# let's make RobotLeg class
class RobotLeg:
    def __init__(self, color="white", length=100):
        self.color = color
        self.length = length
        self._speed = 0
    
    def kick(self):
        print("Kicking")
        return self
    
    def bend(self):
        print("Bending")
        return self
    
    def __str__(self):
        return f"Robot leg with color {self.color} and length {self.length}"
    

# how about RobotArm class?
class RobotArm:
    def __init__(self, color="white", length=100):
        self.color = color
        self.length = length
        self._speed = 0
    
    def wave(self):
        print("Waving")
        return self
    
    def bend(self):
        print("Bending")
        return self
    
    def __str__(self):
        return f"Robot arm with color {self.color} and length {self.length}"
    
# finally RobotBody class
class RobotBody:
    def __init__(self, color="white", length=100):
        self.color = color
        self.length = length
        self._speed = 0
    
    def bend(self):
        print("Bending")
        return self
    
    def __str__(self):
        return f"Robot body with color {self.color} and length {self.length}"
    

# let's make a new composable Robot class
class HumanoidRobot:
    def __init__(self, name="Anonymous", color="white", weight=100, height=200, speed=0):
        print("Creating a new humanoid robot")
        self.name = name
        self.color = color
        self.weight = weight
        self.height = height
        self._speed = speed
        self.head = RobotHead() # so i create a head instance using the RobotHead class
        self.body = RobotBody(color=color, length=height/2) # so body is half the height
        self.left_arm = RobotArm(color=color)
        self.right_arm = RobotArm(color=color)
        self.left_leg = RobotLeg(color=color)
        self.right_leg = RobotLeg(color=color) 
        self.x = 0
        self.y = 0   
        print(f"For your information, my name is {self.name}")
    
    def move_xy(self, x=0, y=0):
        self.x += x
        self.y += y
        return self
    
    def print_my_location(self):
        print(f"{self.name} location is {self.x}, {self.y}")
        return self
    
    def __str__(self):
        return f"Robot {self.name} with color {self.color} at location {self.x}, {self.y}"

# let's make a new humanoid robot
# its name is Robocop
robocop = HumanoidRobot(name="Robocop", color="silver", weight=200, height=220, speed=10)
print(robocop)
# let's move robocop
robocop.move_xy(10, 20).move_xy(-5, 10)
print(robocop)

# of course I could inherit from HumanoidRobot and make a new class 
# with some new methods and attributes
# we will callit EthicsRobot
class EthicsRobot(HumanoidRobot):
    # print Asimov's laws of robotics
    def print_laws(self):
        print("Asimov's laws of robotics:")
        print("1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.")
        print("2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.")
        print("3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.")
        return self
    
# let's make a new ethics robot
ethics_robot = EthicsRobot(name="EthicsRobot", color="white", weight=100, height=200, speed=0)
print(ethics_robot)
# let's move ethics robot
ethics_robot.move_xy(10, 20).move_xy(-5, 10)
print(ethics_robot)
# let's print the laws
ethics_robot.print_laws()

# there are also class methods - methods that belong to the class not to the instance

# we could create a dictionary of HumanoidRobot instances
names = ["Alice", "Bob", "Charlie", "Diana"]
#, "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
robots = {}
for name in names:
    robots[name] = HumanoidRobot(name=name, color="white", weight=100, height=200, speed=0)

# alternatively we could have had a class RobotStorage or RobotFactory
# that would have a dictionary of robots inside

# let's print the robots
for name, robot in robots.items():
    print(robot)

# let's move the robots in various directions
robots["Alice"].move_xy(10, 20).print_my_location()
robots["Bob"].move_xy(-5, 10).print_my_location()
robots["Charlie"].move_xy(20, -10).print_my_location()
robots["Diana"].move_xy(-10, -20).print_my_location()
