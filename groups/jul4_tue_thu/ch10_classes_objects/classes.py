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
robot1 = SimpleRobot() # this takes class and creates an object from it
# we can create more objects from the same class
robot2 = SimpleRobot()
# i could keep making more robots of course

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

# let's create a more advanced robot class
# we will call it Robot
class Robot:
    # first we will want to add ability to create robots with different attributes
    # for that we use __init__ method - this is a special method that is called when we create a new object
    # it is almost like constructor in other languages
    # we can pass in parameters to __init__ method and then use them to create our object
    # we can also set default values for our parameters - use sane defaults meaning common values
    # one warning - we should not use mutable objects as default values such as lists or dictionaries!!
    # we can pass in lists or dictionaries as parameters but we should not use them as default values

    # we will use self to refer to the object we are creating
    def __init__(self, 
                 name="R2D2", 
                 color="blue", 
                 speed=1, 
                 direction="N", 
                 weight=100, 
                 height=100, 
                 battery=100,
                 x=0,
                 y=0,
                 api_key="1234567890",
                 debug=True): # we can have as many parameters as we want):
        if debug:
            print("Starting to create a new Robot")
        self.name = name
        self.color = color
        self.speed = speed
        self.direction = direction
        self.weight = weight
        self.height = height
        self.battery = battery
        # coordinates
        self.x = x
        self.y = y
        # private attribute
        # we should have made validation here as well
        self.__api_key = api_key # notice __ in front of api_key
        # the concept is called information hiding or encapsulation
        # in other we hide our dirty laundry from outside world
        # technically it is done through process called name mangling - we change the name of the attribute
        if debug:
            print("Finished creating a new Robot now let's print it")
            self.print_robot() # we can call other methods from inside our class EVEN before we finish creating the object

    # let us explore more dunder methods
    # there are about 100 of them
    # docs: https://docs.python.org/3/reference/datamodel.html#special-method-names
    # we will override __str__ method
    # this is a method that is called when we try to print our object
    def __str__(self): # only requirement is that we return some sort of string
        return f"Robot {self.name} is at {self.x}, {self.y} and is facing {self.direction}"
    
    # we can also override __repr__ method
    # this is a method that is called when we try to print our object in a list or other collection
    def __repr__(self): # only requirement is that we return some sort of string
        return f"REPR: Robot {self.name} is at {self.x}, {self.y} and is facing {self.direction}"
    
    # let's create our own add method
    # we will use it to add two robots together
    # we will return a new robot with combined attributes
    def __add__(self, other_robot):
        # we will first create new attributes for our new robot
        new_name = self.name + "_" + other_robot.name
        new_color = self.color + "_" + other_robot.color
        new_speed = (self.speed + other_robot.speed) / 2 # make up your own formula
        new_x = self.x + other_robot.x
        new_y = self.y + other_robot.y
        new_weight = self.weight + other_robot.weight
        # we could do more complex calculations here
        # we could also add some randomness, for now we use some defaults as well
        new_robot = Robot(name=new_name, color=new_color, 
                          speed=new_speed, weight=new_weight,
                          x=new_x, y=new_y)
        return new_robot

    # let's createa a method to print our robot
    def print_robot(self): # so same syntax as for functions but we have to add self as first parameter
        # so self is a reference to the concrete object itself
        print(f"Robot {self.name} is at {self.x}, {self.y} and is facing {self.direction}")
        # print heigh and weight and battery
        print(f"Robot {self.name} is {self.height}cm tall and weighs {self.weight}kg and has {self.battery}% battery left")
        return self

    # let's make a method to move our robot
    def move_robot(self, delta_x, delta_y, battery_drain_factor=0.1):
        self.x += delta_x
        self.y += delta_y
        # let's decrease battery using amount of movement
        self.battery -= (abs(delta_x) + abs(delta_y)) * battery_drain_factor
        # the changes are IN PLACE so we do not need to return anything
        # for convenience we could return the robot anyway
        return self
    
    # so for private attributes we can create special methods called getters and setters
    # we can use them to get and set values of our private attributes
    # we can also use them to do some checks on our data
    # let's create a getter for our api_key
    def get_api_key(self):
        # we would check if we are allowed to get the api_key
        # we could also do some other checks
        return self.__api_key # so not returning self but the value of our private attribute
    
    # let's create a setter for our api_key
    def set_api_key(self, new_key):
        # validate the new key
        if self.__is_valid_api_key(new_key): # again we can access private methods from inside our class 
            self.__api_key = new_key # so inside we have access to our private attribute
            return True
        # else: is not needed because 
        return False
    
    # let's create a separate validator method that is private
    def __is_valid_api_key(self, new_key, min_length=10):
        if len(new_key) < min_length:
            print("New key is too short")
            return False
        # we could do more checks here for example if the key is unique or contains only numbers and letters
        return True
    
# let's creat these new robots
r2d2 = Robot() # using default values
# c3po = Robot("C3PO", "gold", 0.5, "E", 150, 150, 100, 10, 10) # using our own values
# let's use named parameters for our c3po robot
c3po = Robot(name="C3PO", color="gold", 
             speed=0.5, direction="E", weight=150, height=150, battery=100, x=10, y=10)

# let's move our robot a little
r2d2.move_robot(10, 25).print_robot().move_robot(10, -10).print_robot()

# by default all properties and methods are public in Python
# so I could do this
r2d2.battery = 0 # but in general we do not want to do this

# so let's try accessing our private attribute
try:
    print(r2d2.__api_key)
except AttributeError as e:
    print("AttributeError", e)

# now we can access our api_key using our getter method
print(r2d2.get_api_key())
r2d2.set_api_key("afdadf")
print(r2d2.get_api_key())
# let's try to set a new key
r2d2.set_api_key("foobar1234")
print(r2d2.get_api_key())

# let's go back to printing our robot
print(r2d2) # so this is not very useful but shows that we have two different objects in memory
print(c3po)
print(c3po.__str__()) # same as above - usually there is no need to call dunder methods directly

# now let's try adding our robots together
r2c3 = r2d2 + c3po # so this will call our __add__ method
# same as r2c3 = r2d2.__add__(c3po) # syntactic sugar for the win!
print(r2c3)

# i could even create a list of robots
robot_list = [r2d2, c3po, r2c3]
print(robot_list) # this uses __repr__ method
for robot in robot_list:
    print(robot) # this uses our __str__ method

# we could create a big list of robots if we want
big_robot_list = []
# let's use random to add randome locations
import random # usually imported at the top of the file

for i in range(100):
    random_x = random.randint(-100, 100)
    random_y = random.randint(-100, 100)
    random_face = random.choice(["N", "S", "E", "W"]) # random face
    # good for putting robots on a field somewhere
    big_robot_list.append(Robot(name=f"Robot_{i}", 
                                x=random_x,
                                y=random_y,
                                direction=random_face,
                                debug=False)) # i could adjust some parameters here

# let's print our last robot
print(big_robot_list[-1])
# let's print first 3 robots
print(big_robot_list[:3])
# of course we could have stored our 
# robots in a dictionary as well by key or id or robot_name if it unique

# now let's talk a  litle bit about inheritance
# let's make a flying robot class but we will inherit from our Robot class
# we do not want to repeat all the code from Robot class

# let's create a FlyingRobot class
class FlyingRobot(Robot): # so we pass in the class we want to inherit from
    # so we have default constructor from Robot
    # we have all the methods from robot
    # let's make a new method for flying
    # we could add z here
    # z = 0 # so we have z coordinate fixed for start
    # better idea would be to override our __init__ method
    def __init__(self,
                    name="R2D2",
                    color="blue",
                    speed=1,
                    direction="N",
                    weight=100,
                    height=100,
                    battery=100,
                    x=0,
                    y=0,
                    z=0,
                    debug=True):
        # first we should init our own attributes
        self.z = z 
        # why first because our parent class might need some of our attributes
        # we can call the parent class constructor
        # we can do that using super() method
        # super() will call the constructor from the parent class
        super().__init__(name=name, color=color, speed=speed, direction=direction, weight=weight, height=height, battery=battery, x=x, y=y, debug=debug)

        # our own constructor is done here

    def fly(self, delta_x, delta_y, delta_z, battery_drain_factor=0.1):
        self.x += delta_x
        self.y += delta_y
        self.z += delta_z # this will have a problem because we do not have z in our Robot class
        # let's decrease battery using amount of movement
        self.battery -= (abs(delta_x) + abs(delta_y) + abs(delta_z)) * battery_drain_factor
        # the changes are IN PLACE so we do not need to return anything
        # for convenience we could return the robot anyway
        return self
    
    # let's override our __str__ method to include z
    def __str__(self): # only requirement is that we return some sort of string
        return f"Flying Robot {self.name} is at {self.x}, {self.y}, {self.z} and is facing {self.direction}"

    # let's overwrite our print_robot method
    # but we want to use the print_robot method from Robot class
    # we can do that by using super() method
    # super() will call the method from the parent class
    def print_robot(self): # so same syntax as for functions but we have to add self as first parameter
        # so self is a reference to the concrete object itself
        super().print_robot() # this will call the print_robot method from Robot class
        # print z
        print(f"Robot {self.name} is at {self.z} meters above ground")
        return self

# let's create a flying robot
flying_robot = FlyingRobot(name="Icarus")
print(flying_robot) # so we can print it
# let's try to fly
flying_robot.fly(10, 10, 10).print_robot() # so we can fly

# there is long ongoing discussion between inheritance and composition

# in composition we store objects inside other objects

# let's create a new class called RobotWorld
class RobotWorld:
    def __init__(self, name="Robot World", robot_list = (), debug=True):
        self.name = name
        self.debug = debug
        self.robot_list = list(robot_list) # so important that default value is not mutable
        if self.debug:
            print(f"Creating a new Robot World called {self.name}")
    
    def add_robot(self, robot):
        if self.debug:
            print(f"Adding robot {robot.name} to {self.name}")
        self.robot_list.append(robot)
        return self
    
    def print_robots(self):
        print(f"Printing robots in {self.name}")
        for robot in self.robot_list:
            print(robot)
        return self
    
    def move_robots(self, delta_x, delta_y, delta_z):
        if self.debug:
            print(f"Moving robots in {self.name}")
        for robot in self.robot_list:
            # check that robot is flying
            if isinstance(robot, FlyingRobot):
                robot.fly(delta_x, delta_y, delta_z)
            elif isinstance(robot, Robot):
                robot.move_robot(delta_x, delta_y)
            else:
                print(f"Unknown robot type {type(robot)}")
        return self
    

# let's create a new robot world
robot_world = RobotWorld(name="Robot World")
# let's add some robots
robot_world.add_robot(r2d2)
robot_world.add_robot(c3po)
robot_world.add_robot(r2c3)
robot_world.add_robot(flying_robot)

# let's move our robots
robot_world.move_robots(10, 10, 10)
# print our robots
robot_world.print_robots()
# of course we can still move individual robots inside our robot world
robot_world.robot_list[0].move_robot(10, 10) # so this will move r2d2
robot_world.print_robots()

# another way of using composition would be to build a robot from parts
# say separate class for head, body, legs, arms, etc