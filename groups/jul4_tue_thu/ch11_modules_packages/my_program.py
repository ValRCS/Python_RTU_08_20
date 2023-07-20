# let's talk a little bit how we can separate our code into different files
# i might have many functions that i want to use in my program
# i might have classes that I want to store in a separate file
# maybe those were made by someone else and I want to use them in my program

# first let's look where python looks for modules
# python looks for modules in the current directory
# this means your modules should not overwrite standard library modules
# bad name for your module would be random.py or sys.py or math.py etc
# TODO weekend assignment check out what standard library modules are available
# docs: https://docs.python.org/3/library/ # this is a good place to start
# regular Python will have those, MicroPython will have less standard library modules
# typically system imports are first
import sys # standard library module
print(sys.path) # prints path where python looks for modules

# then what is a module after all in Python?
# a module is just a file with a .py extension
# let's import robot from robot.py
import robot # this will import robot.py and run everything in it (including print statements)
# we generally do not want something to happen when we import a module
# we just want the definitions to be available
import my_functions # this will import my_functions.py and run everything in it (including print statements)
import my_math # this will import my_math.py and run everything in it (including print statements)
# so now we can make our robots
marvin = robot.Robot("Marvin")
marvin.say_hi()
alice = robot.Robot("Alice")
alice.say_hi()
# i can call my functions
my_functions.say_hi("Valdis")
# so by using module system we can separate our code into different files
# also i gain the ability to import other people's code
# also I gain namespace separation
# i can call my_math Math methods
print(my_math.Math.add(2, 3))
print(my_math.Math.sub(2, 3))
print(my_math.Math.circle_area(10))