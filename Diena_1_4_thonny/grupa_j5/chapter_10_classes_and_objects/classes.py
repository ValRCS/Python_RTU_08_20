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
        self.speed = speed
        self.y = y
        self.x = x
        print(f"Robot {self.name} created")
        print("Properties:")
        print(self.__dict__)

    def move_forward(self, distance=1):
        self.y += distance

    def describe_myself(self):
        print(f"Hi, I am {self.name} and I am {self.color}")

    def print_my_location(self):
        print(f"My location is {self.x}, {self.y}")

    def __str__(self):
        # so whenever we print the object, this method is called
        # we override the default __str__ method which was basically useless
        return f"Robot {self.name} with color {self.color} at location {self.x}, {self.y}"
    # i could return anything in __str__ method as long as it is a string

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

