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

# we can import only certain functions from a module
from my_functions import say_hi, say_bye

say_hi("Valdis")
say_bye("Valdis")

# so this is convenient but we might have name clashes - 
# if we had say_hi and/or say_bye defined locally or by some other module
# then we would have to use my_functions.say_hi() or my_functions.say_bye()

# if i want to keep namespace but make it shorter I can provide an alias
import my_functions as mf # very common among larger libraries
# we keep the namespace but we can use shorter name

mf.say_hi("Valdis")
mf.say_bye("Valdis")

# it goes without saying we only need one approach for each module

# finally we can import specific things from a module with an alias
from my_functions import say_hi as sh, say_bye as sb # again careful of name clashes
sh("Valdis")
sb("Valdis")

# we can import everything from a module DO NOT USE THIS!!
# from my_functions import * # again careful of name clashes
# AVOID because it does not truly import everything and also can cause name clashes

# again avoid naming your modules after standard library modules
# so avoid random.py, sys.py, math.py etc 

# now onto packages
# what is package in Python?
# a package is a folder (used to require __init__.py file but not anymore)

# let's import my_mod1 from my_package
# we could import with a long name
import my_package.my_mod1
# then we have to use the long name
my_package.my_mod1.lets_rock("Valdis")
# typically we would rename the module
import my_package.my_mod1 as mm1 # again no need to do it twice in real
mm1.lets_rock("Valdis")

# importing just the my_package will not work

# of course we can import just the specific function
from my_package.my_mod1 import lets_rock
lets_rock("Valdis")
# and we can even rename it
from my_package.my_mod1 import lets_rock as lr #not good practice
lr("Valdis")

# generally we want to rename modules but keep original names for functions,classes

# exception might be something like ET for element tree
# import xml.etree.ElementTree as ET
# this is class for parsing XML files from standard library
# import xml.etree.ElementTree as ET

# so what is a library then?
# a library is a collection of packages and modules
# we use the name library but there is no special meaning in Python
# standard library is a collection of modules and packages that come with Python