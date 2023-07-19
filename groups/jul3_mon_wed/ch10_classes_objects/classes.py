# Let's talk about classes and objects in Python

# class is a blueprint/template for creating objects
# object is an instance of a class
# we can create as many objects as we want from a class
# objects have attributes/data and methods/class functions

# everything is an object in Python
# we can check the type of an object using type() function
# print(type(777))
# name = "Valdis"
# print(type(name))

# classes combine data and functions that work with that data
# data we often call attributes
# functions in the class we call methods (Python) or class functions
# Offical Python Docs on Classes https://docs.python.org/3/tutorial/classes.html

# what do we do if we need to store some data and have some functions that work with that data

# let's see first how we would do it without classes

# let's say I want to create some robots
# how would I do it without classes in Python?
# I would need to store some data about the robot - say in a dictionary

# robot_dict = {
#     name: R2D2,
#     color: blue,
#     weight: 100,
#     height: 75,
#     speed: 10,
#     battery: 100,
#     x: 0,
#     y: 0
# }

# # now I would like to modify and display the robot's data using some functions

# def print_robot(robot):
#     print(fRobot {robot['name']} is at {robot['x']},{robot['y']} with battery {robot['battery']})

# def move_up(robot):
#     robot['y'] += robot['speed']
#     robot['battery'] -= 10
#     # this is IN PLACE modification of the robot dictionary
#     # so return is not needed but we can
#     return robot

# # let's try to move our robot
# print_robot(robot_dict)
# move_up(robot_dict)
# print_robot(robot_dict)

# how about if we need many similar robots?
# we would need to create many dictionaries and pass them around

# let's do the same thing with classes

# classes use CamelCase naming convention - PEP008 - https://www.python.org/dev/peps/pep-0008/#class-names
class SimpleRobot:
    name = "R2D2"
    color= "blue"
    weight= 100
    height= 75
    speed= 10
    battery= 100
    x= 0
    y= 0
    # in general we will want to use a constructor to create our objects - later

    # we can have methods that work with our data
    # methods are functions inside a class
    # print robot data
    def print_robot(self): # in other languages self is called this - reference on particular object itself
        # tehcnially we can call this variable anything but self is the convention
        print(f"Robot {self.name} is at {self.x},{self.y} with battery {self.battery}")
        # print color info
        print(f"Robot {self.name} has color {self.color}")

    # i can have a method to move my robot
    def move_up(self):
        self.y += self.speed
        self.battery -= 10
        # this is IN PLACE modification of the robot dictionary
        # so return is not needed but we can
        # so methods that have nothing to return might as well return self
        return self # this is kind of nice because we can chain methods
        

# let's create an instance of our class
# we can create as many instances as we want

# we use the class name as a function to create an instance
# robot_1 = SimpleRobot()
# robot_2 = SimpleRobot()

# # let's check the type of our robots
# print(type(robot_1))
# print(type(robot_2))
# # memory location is different so we have two different objects
# print(robot_1)
# print(robot_2)
# # we can have custom print function for our class - later on
# # compare robot ids
# print(id(robot_1))
# print(id(robot_2))
# # for now they have same data
# print(robot_1.name)
# print(robot_2.name)
# robot_1.color = "red"
# print(robot_1.color)
# print(robot_2.color) # different object so different data

# now I can my class methods
# robot_1.print_robot() # notice I do not need to pass self
# robot_2.print_robot()

# # let's move our robots
# robot_1.move_up()
# robot_1.print_robot()
# robot_2.move_up()
# robot_2.move_up().move_up().move_up() # we can chain methods
# robot_2.print_robot()

# let's make a bit more serious robot class

class Robot:
    # we will use a constructor to create our objects
    # constructor is a special method that is called when we create an object
    # constructor is called __init__ in Python
    # technically __init__ is called right after the object is created
    # we can pass some parameters to our constructor
    # we can use default values for our parameters - DO NOT USE lists or dictionaries as default values!

    # __init__ is a special method so it has double underscores
    # Python classes has about 100 special methods that we can use
    # full list of special methods https://docs.python.org/3/reference/datamodel.html#special-method-names
    def __init__(self, name="R2D2", color="blue", weight=100, height=75, speed=10, battery=100, x=0, y=0):
        # self is a reference to the object itself
        # we can use self to access and modify object attributes
        print("Creating a new Robot")
        self.name = name
        self.color = color
        self.weight = weight
        self.height = height
        self.speed = speed
        self.battery = battery
        self.x = x
        self.y = y
        print("Robot created")
        # i can call other methods from my constructor
        self.print_robot() # we can call other methods from our constructor 
        print(self) # we can print our object will use __str__ method

    # let's make print_robot method - this is arbitrary name
    def print_robot(self):
        print(f"Robot {self.name} is at {self.x},{self.y} with battery {self.battery}")
        # print color info
        print(f"Robot {self.name} has color {self.color}")
        # let's add return self so we can chain methods
        return self

    # we can make a custom __str__ method to print our object
    # this is a special method that is called when we try to print our object
    # we can use this method to print our object in a custom way
    # we can use this method to return a string representation of our object
    # so __str__ can return anything as long as it is a string
    def __str__(self):
        return f"Robot weighting {self.weight} kg {self.name} is at {self.x},{self.y} with battery {self.battery}"

    # now let's make some methods for moving our robot
    # first let's make a function that uses both x and y
    def move(self, x, y, battery_use=10):
        self.x += x
        self.y += y
        self.battery -= battery_use
        return self # again we can chain methods
    
    # now let's make some methods that move our robot in different directions
    def move_vertically(self, y=1):
        self.move(0, y) # we could add battery use here as well
        # there could be an hardware call here to move the robot
        return self
    
    def move_horizontally(self, x=1):
        self.move(x, 0)
        return self
    
    # we could have made also move up down left right methods

    # let's make an add method for createing sum of two robots
    def __add__(self, other):
        # we can create a new robot with sum of two robots
        #
        new_name = self.name + "_" + other.name
        new_color = self.color + "_" + other.color
        new_weight = self.weight + other.weight
        new_height = self.height + other.height
        new_speed = self.speed + other.speed
        new_battery = self.battery + other.battery
        new_x = self.x + other.x
        new_y = self.y + other.y
        # now we can create a new robot
        new_robot = Robot(name=new_name, color=new_color, weight=new_weight, height=new_height, speed=new_speed, battery=new_battery, x=new_x, y=new_y)
        return new_robot # not self because we are creating a new robot

    # there are __sub__ __mul__ __div__ methods as well for -, *, / operators
    # there are also comparison methods __lt__ __gt__ __eq__ __ne__ __le__ __ge__ for <, >, ==, !=, <=, >= operators

# let's create some robots
r2d2 = Robot() # r2d2 is an instance of Robot class
print(r2d2.name)

# let's create a robot with custom name
c3po = Robot(name="C3PO", weight=150, color="gold")
# print(c3po.name)

# # now let's print our robots
# r2d2.print_robot()
# print(r2d2) # this is not very useful for now but we will fix it with __str__ method

# now we can move our robots
r2d2.move(10, 10).print_robot().move_vertically().move_horizontally(3).print_robot()# i could keep chaining methods

# i can move negatively as well
c3po.move(-10, -10).print_robot().move_vertically(-3).move_horizontally(-2).print_robot()

# i could move the coordinates directly but that would not use the battery and 
# would defeat the purpose of the class

# now we can use + to add our robots
r2d2_c3po = r2d2 + c3po # this works because I have defined __add__ method