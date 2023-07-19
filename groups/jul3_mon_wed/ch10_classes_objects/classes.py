# Let's talk about classes and objects in Python

# class is a blueprint/template for creating objects
# object is an instance of a class
# we can create as many objects as we want from a class
# objects have attributes/data and methods/class functions

# everything is an object in Python
# we can check the type of an object using type() function
print(type(777))
name = "Valdis"
print(type(name))

# classes combine data and functions that work with that data
# data we often call attributes
# functions in the class we call methods (Python) or class functions
# Offical Python Docs on Classes https://docs.python.org/3/tutorial/classes.html

# what do we do if we need to store some data and have some functions that work with that data

# let's see first how we would do it without classes

# let's say I want to create some robots
# how would I do it without classes in Python?
# I would need to store some data about the robot - say in a dictionary

robot_dict = {
    "name": "R2D2",
    "color": "blue",
    "weight": 100,
    "height": 75,
    "speed": 10,
    "battery": 100,
    "x": 0,
    "y": 0
}

# now I would like to modify and display the robot's data using some functions

def print_robot(robot):
    print(f"Robot {robot['name']} is at {robot['x']},{robot['y']} with battery {robot['battery']}")

def move_up(robot):
    robot['y'] += robot['speed']
    robot['battery'] -= 10
    # this is IN PLACE modification of the robot dictionary
    # so return is not needed but we can
    return robot

# let's try to move our robot
print_robot(robot_dict)
move_up(robot_dict)
print_robot(robot_dict)

# how about if we need many similar robots?
# we would need to create many dictionaries and pass them around