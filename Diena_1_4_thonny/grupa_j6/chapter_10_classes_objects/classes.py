# Let's talk about classes and objects in Python

# Class is a blueprint / template for creating objects
# objects are instances of a class - concrete realizations of a class

# in Python everything is an object, even primitive types like int, float, bool, str
# we can check this with type() function 
name = "Valdis"
print(type(name))

# classes combine data and functions that work with that data
# data are often called attributes
# functions are often called methods including Python
# Docs: https://docs.python.org/3/tutorial/classes.html - somewhat dry

# let's image we want to create robots
# how could we store data about a robot?
# we could use a dictionary

# robot_dict  = {"name": "R2D2", 
#                "speed": 10, 
#                "weight": 100, 
#                "height": 100,
#                "x": 0,	
#                "y": 0}

# # then we would want some functions to work with our robot
# # we could create a function that would print out our robot
# def print_robot(r):
#     print(f"Robot {r['name']} has speed {r['speed']} and weight {r['weight']}")

# print_robot(robot_dict)

# # how about moving our robot?
# def move_robot(r, x, y):
#     r['x'] += x
#     r['y'] += y
#     # we could even return the new position or robot
#     return r # IN PLACE function so no need to return robot

# robot_alias = move_robot(robot_dict, 10, 20)
# print(robot_alias)
# print_robot(robot_dict)
# print(robot_alias is robot_dict) # True

# issue with above approach is that our data and functions are separate
# for organizing our code we could use classes

# let's make a simple robot class
# class names are CamelCased - each word starts with a capital letter
# no underscores in class names
class SimpleRobot:
    # usually not the best approach to set attributes here
    x = 0
    y = 0
    name = "R2D2"
    speed = 10
    weight = 100
    height = 100

    # let's make a function to move our robot - method
    def move(self, x, y):
        self.x += x
        self.y += y

    # let's make a print info method
    def print_info(self):
        print(f"Robot {self.name} has speed {self.speed} and weight {self.weight}")

    # do not do this!! - technically it works but it is not Pythonic
    def print_something(this): # NOT PYTHONIC style - this JAVA or C++ style!!
        print(f"Robot {this.name} has speed {this.speed} and weight {this.weight}")

# let's run our code again
# we can create an instance of a class by calling the class name

robot1 = SimpleRobot() # creates an instance of a class - an object
# now I can access the attributes of my object
print(robot1.name)
print(robot1.x)
print(robot1.y)

robot_2 = SimpleRobot() # completely separate object with identical attributes for now
print(robot_2.name)
print(robot_2.x)
print(robot_2.y)

# let's move our robot
robot1.x += 10
robot1.y += 20
print(robot1.x)
print(robot1.y)
# how second robot loc
print(robot_2.x)
print(robot_2.y)

# above approach is far from perfect because we have to set all the attributes manually
# now we could use move method
robot1.move(15, 25) # notice no need to pass self - it is done automatically
print(robot1.x)
print(robot1.y)
robot_2.move(100, 200)
print(robot_2.x)
print(robot_2.y)

robot_2.print_info() # notice no need to pass self - it is done automatically
robot_2.print_something() 

# for now what happens if we print a robot?
print(robot1) # shows memory location
print(robot_2) # not very useful
# later on we will see how we can make it more useful

# let's make a normal Robot class with __init__ method
class Robot:
    """This is a Robot class
    Creation of a Robot requires a name, speed, weight, height
    x and y are optional and default to 0

    """

    # let's make a constructor method
    # __init__ is a special method that is called when we create an instance of a class
    # __init__ should be written exactly like this
    # __ are so called dunder methods - double underscore
    # there are about 100 dunder methods in Python
    # docs: https://docs.python.org/3/reference/datamodel.html#special-method-names
    # most important one is __init__ and __str__
    # self is a reference to the object itself
    # we can pass in arguments to our constructor
    # note use of default values
    def __init__(self, name="anonymous", speed=45, weight=100, height=180, x=0, y=0):
        print("Creating a new Robot")
        # so I assign the arguments to my object attributes
        self.name = name
        self.speed = speed
        self.weight = weight
        self.height = height
        self.x = x
        self.y = y
        print(f"Created a new Robot {self.name} with speed {self.speed} and weight {self.weight}")

# let's create a new robot from our Robot class blueprint
robbie = Robot("Robbie", 10, 100, 100)
print(robbie.name)
default_robot = Robot() # uses all default values
print(default_robot.name)
named_robot = Robot(name="Valdis")
print(named_robot.name)

# so we can initialize our objects with different values
# again all the above robots have separate attributes in separate memory locations

# next we will look into how to make our robots do something


