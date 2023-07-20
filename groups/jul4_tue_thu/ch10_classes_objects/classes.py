# Let's talk about classes and objects in Python

# a class is a blueprint/template for an object
# then object is a concrete instance of a class
# from a single class we can create many objects
# class provides a way to organize data and functions together

# everything in Python is an object
# let's check it out
print(type(2023))
print(type(3.14))
print(type(True))
name = "Valdis"
print(type(name))

# so in our class definition we can have data and functions (called methods in Python)
# data we call attributes (in Python) also properties or fields in other languages

# official Python docs on classes: https://docs.python.org/3/tutorial/classes.html

# first let's try saving some data and functions that work with that data without classes

# let's say I want to create a robot that can move around

# i could save the data in a list but that would be confusing
# we would have to remember that the first element is x and second is y
# and third would be name and so on

# better idea would be to use a dictionary
# we could use keys like x, y, name, color, speed, etc.

# robot_dict = {
#     "x": 0,
#     "y": 0,
#     "name": "R2D2",
#     "color": "blue",
#     "speed": 1,
#     "direction": "N",
#     "weight": 100,
#     "height": 100,
#     "battery": 100
#     # if this was real hardware we would probably have more data such as hardware id ,etc
# }

# now let's create some functions that work with our robot
# first print current state of our robot
# def print_robot(robot):
#     print(f"Robot {robot['name']} is at {robot['x']}, {robot['y']} and is facing {robot['direction']}")
#     # print heigh and weight and battery
#     print(f"Robot {robot['name']} is {robot['height']}cm tall and weighs {robot['weight']}kg and has {robot['battery']}% battery left")

# # let's print state of our robot
# print_robot(robot_dict)

# # let's make a function to move our robot
# def move_robot_current_direction(robot, steps, battery_drain_factor=0.1):
#     if robot["direction"] == "N":
#         robot["y"] += steps
#     elif robot["direction"] == "S":
#         robot["y"] -= steps
#     elif robot["direction"] == "E":
#         robot["x"] += steps
#     elif robot["direction"] == "W":
#         robot["x"] -= steps
#     else:
#         print("Unknown direction")
#     # let's decrease battery
#     robot["battery"] -= steps * battery_drain_factor
#     # the changes are IN PLACE so we do not need to return anything
#     # for convenience we could return the robot anyway
#     return robot

# # let's move our robot
# move_robot_current_direction(robot_dict, 10)
# print_robot(robot_dict)

# # let's make a function to change direction
# def change_robot_direction(robot, new_direction):
#     # we could do some checks here
#     if new_direction not in {"N", "S", "E", "W"}: # sets will be faster than lists
#         print("Unknown direction")
#         return robot
#     robot["direction"] = new_direction # again IN PLACE modification of passed in robot
#     return robot

# # let's change direction
# change_robot_direction(robot_dict, "E")
# print_robot(robot_dict)
# # move east 25 steps
# move_robot_current_direction(robot_dict, 25)
# print_robot(robot_dict)

# # personally I would like a function that gives delta coordinates x and y
# # and direction would be implicit
# # let's make a function to move our robot
# def move_robot(robot, delta_x, delta_y, battery_drain_factor=0.1):
#     robot["x"] += delta_x
#     robot["y"] += delta_y
#     # let's decrease battery using amount of movement
#     robot["battery"] -= (abs(delta_x) + abs(delta_y)) * battery_drain_factor
#     # the changes are IN PLACE so we do not need to return anything
#     # for convenience we could return the robot anyway
#     return robot

# # let's move our robot
# move_robot(robot_dict, 12, -30)
# print_robot(robot_dict)

# so we can work with our robot but it is not very convenient
# also if we need more robots we would have to create more dictionaries
# we can do everything with functions but they are spread out and not very convenient

# classes to the rescue!
# classes use CamelCase naming convention PEP08 https://www.python.org/dev/peps/pep-0008/#class-names
# let's create a very simple robot class
class SimpleRobot:
    name = "R2D2"
    color = "blue"
    speed = 1
    direction = "N"
    weight = 100
    height = 100
    battery = 100
    # coordinates
    x = 0
    y = 0
    
    # let's createa a method to print our robot
    def print_robot(self): # so same syntax as for functions but we have to add self as first parameter
        # so self is a reference to the concrete object itself
        print(f"Robot {self.name} is at {self.x}, {self.y} and is facing {self.direction}")
        # print heigh and weight and battery
        print(f"Robot {self.name} is {self.height}cm tall and weighs {self.weight}kg and has {self.battery}% battery left")
        # again if I am not returning anything I do not need to use return statement
        # but returning self is a common practice so we can chain methods together
        return self

    # let's make a method to move our robot
    def move_robot(self, delta_x, delta_y, battery_drain_factor=0.1):
        self.x += delta_x
        self.y += delta_y
        # let's decrease battery using amount of movement
        self.battery -= (abs(delta_x) + abs(delta_y)) * battery_drain_factor
        # the changes are IN PLACE so we do not need to return anything
        # for convenience we could return the robot anyway
        return self # this will let us chain methods together using dot notation
    
# let's create a robot object
robot1 = SimpleRobot()
# we can create more objects from the same class
robot2 = SimpleRobot()

# let's check what we have
print(robot1)
print(robot2) # so this print is not very useful but shows that we have two different objects in memory
# we can access and modify attributes of our objects
print(robot1.name)
print(robot2.name)
robot1.name = "C3PO"
print(robot1.name)
print(robot2.name) # other robot is not changed

# let's print our robot
robot1.print_robot() # note no need to pass in self, it is done automatically!
robot2.print_robot()
# so far we have dot access to attributes and methods
# let's chain some moves and prints together
robot1.move_robot(10, 25).print_robot().move_robot(10, -10).print_robot()

# SimpleRobot class is a bit too simple, for one our data might change over time
# what if we have different attributes for different robots?
# we do not want to change each attribute for each robot by hand after creation - we can but it is not convenient
