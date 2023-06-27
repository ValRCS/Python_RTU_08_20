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
    # let's make a class method to interactively ask for robot data and return new robot
    @classmethod # decorator to mark this as a class method
    def create_robot_interactively(cls):
        name = input("What is the name of your robot?")
        while True:
            try:
                speed = int(input("What is the speed of your robot?"))
                weight = int(input("What is the weight of your robot?"))
                height = int(input("What is the height of your robot?"))
                x = int(input("What is the x position of your robot?"))
                y = int(input("What is the y position of your robot?"))
                break
            except ValueError:
                print("Please enter a valid number!")

        return cls(name, speed, weight, height, x, y) # cls will be Robot class
    # i can call this before any instance of a class is created

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
        # there is single _
        # _ is used for private attributes but comletely optional hint
        self._momentum = self.speed * self.weight # we can set attributes that are not passed in
        # above is not really private - single _ is just a hint that it is for internal use
        self.__password = "1234" # we can set attributes that are not passed in
        # __ makes this attribute private - not really enforced in Python
        # Python utilizes so called name mangling - it changes the name of the attribute
        print(f"Created a new Robot {self.name} with speed {self.speed} and weight {self.weight}")
        # i can call my methods here
        self.print_location() # it is okay that I defined it later

    # let's make a method for __str__ dunder method
    # __str__ is called when we try to print our object
    # default prints memory location - not very useful
    # we can always get our memory location with id() function
    # we can return a string from __str__ method
    # only requirement is that we return a string
    def __str__(self):
        return f"Robot name {self.name} speed {self.speed} weight {self.weight} x:{self.x} y:{self.y}"
    
    # there is also __repr__ dunder method for representation of our object
    # usually __str__ is enough

    # let's make a method to combine two robots
    # we can return a new robot 
    # we will overwrite the default + operator
    def __add__(self, other):
        return Robot(name=f"Mega_{self.name}_{other.name}", 
                    speed=self.speed + other.speed, 
                    weight=self.weight + other.weight, 
                    height=self.height + other.height,
                    x=self.x + other.x,
                    y=self.y + other.y)
    
    # i could define equality with __eq__ method
    # I could define multiplication with __mul__ method
    # I could define subtraction with __sub__ method
    # and son
    # consult the docs for more info
    # docs: https://docs.python.org/3/reference/datamodel.html#special-method-names

    # let's make a method to return dictionary of our robot attributes
    def get_robot_dict(self):
        return {"name": self.name, 
                "speed": self.speed, 
                "weight": self.weight, 
                "height": self.height,
                "x": self.x,	
                "y": self.y}
    
    # let's make a move method
    def move(self, x, y):
        # add logic to check if x and y are numbers
        # if x and y are lead to valid location etc
        self.x += x
        self.y += y
        # now what should we return if anything?
        # we do not have to return anything
        # however it is a good idea to return self
        # this way we can chain methods
        return self # so we return the object itself this means we can call more methods on it
    
    def print_location(self):
        print(f"Robot {self.name} is at {self.x}:{self.y}")
        # again we can return self
        return self # if i did not return self I would have to stop chaining methods
    
    # so called information hiding - controlling access to attributes
    # let's get password
    def get_password(self):
        # here i can create logic to check if user is authorized
        # for now let's just return the password
        return self.__password # so methods have access to private attributes
    
    # let's make a method to change the password
    def set_password(self, new_password):
        # i could check here if length of password is at least 4
        # i could check if password has at least one number etc
        # for now let's just set the password
        self.__password = new_password
        # i could log here that password was changed
        return self # again we can return self to chain methods, not required
    
    # how about increasing speed?
    def increase_speed(self, amount=10):
        # we can add logic to check if amount is a number
        # we can add logic to check if amount is positive
        # we can add logic to check if amount is not too big
        self.speed += amount
        # here we could sent info real hardware to increase speed
        # the driver would be imported at the top of the file
        # we can return self to chain methods
        return self

# let's create a new robot from our Robot class blueprint
robbie = Robot("Robbie", 10, 100, 100)
print(robbie.name)
default_robot = Robot() # uses all default values
print(default_robot.name)
named_robot = Robot(name="Valdis")
print(named_robot.name)
my_robot_list = [robbie, default_robot, named_robot] # no new robots are created
# above is just a list of references to our objects - aliases
print(my_robot_list)
print(my_robot_list[0].name)

# i could make a loop to make multiple robots
# let's assign random locations to our robots
import random
robot_list = []
for i in range(10):
    robot_list.append(Robot(name=f"Robot{i}", 
                            x=random.randint(0, 125),
                            y=random.randint(0, 125)))
    
# now let's filter those robots that are close to 100, 100
filtered_robots = []
for robot in robot_list:
    if robot.x > 75 and robot.y > 75:
        print(robot.name)
        filtered_robots.append(robot)
# now I have a list of robots that are close to 100, 100
print(f"I have {len(filtered_robots)} robots close to 100, 100")
# let's print those robots
for robot in filtered_robots:
    print(robot)

# so we can initialize our objects with different values
# again all the above robots have separate attributes in separate memory locations

# next we will look into how to make our robots do something

mega_robot = robbie + default_robot # works because we have __add__ method
print(mega_robot)
another_mega_robot = robbie.__add__(named_robot) # works because we have __add__ method
print(another_mega_robot)

# so strings already have __add__ method
print("Valdis".__add__(" Saulespurens")) # works because we have __add__ method

# now we can move robbie
robbie.move(15, 10)
print(robbie)
robbie.print_location()
# i  an now chain methods
robbie.move(15, 10).print_location().move(15, 10).move(100,200).print_location()
print()
# I can not access my private attribute directly
# print(robbie.__password)
my_password = robbie.get_password()
print(my_password)
robbie.move(500,200).set_password("1234567890").print_location()
new_password = robbie.get_password()
print(new_password)
# i can print _momentum because it is not really private
print(robbie._momentum)


# let's talk briefly about inheritance
# we can make a new class that inherits from Robot everything
# then we can add new methods or overwrite existing ones

# Let's make FlyingRobot class

class FlyingRobot(Robot):
    # now everything from Robot is available to FlyingRobot
    # this includes __init__ method as well
    # if we overwrite __init__ method we will lose access to Robot __init__ method
    # we will need to call super().__init__ to call Robot __init__ method
    # we can add new methods
    def preflight_check(self):
        print("Starting preflight check")
        print("Checking wings")
        print("Checking fuel")
        print("Checking engines")
        print("Checking tail")
        print("Preflight check complete")

flying_robot = FlyingRobot("Flyer", 10, 100, 100)
print(flying_robot) # __str__ method is inherited from Robot
flying_robot.preflight_check() # this method is only available to FlyingRobot

# alternative to inheritance is to use composition
# we can make a class that has a Robot as an attribute
# then we can use Robot methods on our new class
# we can also add new methods to our new class

class FlyingRobot2:
    def __init__(self, name, speed, weight, height):
        self.robot = Robot(name, speed, weight, height)
        # we could create more objects here
        # now we have a Robot as an attribute
        # we can use Robot methods on our new class
        # we can also add new methods to our new class
        # we can also overwrite Robot methods
    def preflight_check(self):
        print("Starting preflight check")
        print("Checking wings")
        print("Checking fuel")
        print("Checking engines")
        print("Checking tail")
        print("Preflight check complete")
    def __str__(self):
        # we can overwrite __str__ method
        return f"Robot {self.robot.name} is at {self.robot.x}:{self.robot.y}"
    
flying_robot.increase_speed(300).move(100,100).print_location()
print(flying_robot)


# I can make a utility class for static methods

class RobotUtils:
    # static methods are well suited for utility classes
    # so only one copy of these methods will exist in memory
    # when we do not need to access any attributes
    # weight conversion
    @staticmethod # this is a decorator, notice no self
    def kg_to_pounds(kg):
        return kg * 2.20462
    
    @staticmethod
    def pounds_to_kg(pounds):
        return pounds / 2.20462

# i can call static methods without creating objects!
print(RobotUtils.kg_to_pounds(100))
print(RobotUtils.pounds_to_kg(100))
# one advantage we gain naming space less chance of name collision


# finally let's create a function that interactively asks user for robot data
# then creates a robot and returns it

def create_robot():
    name = input("What is your robot name? ")
    while True:
        try:    
            speed = float(input("What is your robot speed? "))
            weight = float(input("What is your robot weight? "))
            height = float(input("What is your robot height? "))
            break
        except ValueError:
            print("Please enter a number")
    # location is assumed to be 0,0
    return Robot(name, speed, weight, height)

# now we can create a robot
# my_robot = create_robot()
# i can call class methods without creating objects
another_robot = Robot.create_robot_interactively() # notice no self again, no cls either

# there is data class module in Python 3.7 and above
# it is a decorator that can create a class with attributes and methods
# it is a bit like a named tuple but with methods
# it is a bit like a Java Bean
# it is a bit like a C struct
# in C# it is called a record
# in Scala it is called a case class

from dataclasses import dataclass
# lets make one for person
@dataclass # this add some nice methods to our class
class Person:
    name: str
    age: int
    height: float
    weight: float
    # so __init__ method is created for us
    # we can add methods
    def bmi(self):
        return self.weight / (self.height / 100) ** 2
    
# now we can create a person
valdis = Person("Valdis", 50, 180, 100)
print(valdis) # this should be a nice __str__ method

