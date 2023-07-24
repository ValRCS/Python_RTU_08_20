# this will be our main program
# first we can import from standard library
# docs: https://docs.python.org/3/library/
# TODO over weekend look at some of these modules
# included with all regular python installations
# MicroPython does not have all of these modules - look at docs for your board

# module is essentially a file with python code with .py extension

# let's show path that is used to look for modules
import sys
print(sys.path)

# you can see that first we look in current directory only then in other places
# if you want to import from other directory you need to add it to sys.path

# so good rule to follow - do not name your .py files the same as standard library modules
# so string.py would be bad, my_string.py would be better
# random.py would be bad, my_random.py would be better
# also do not name your .py files the same as other modules you are importing


# we will want to use Robot class from robot.py
import robot # we get access to everything in robot.py
# i also want to use Math class from my_math.py
import my_math # we get access to everything in my_math.py
# because of main guard in my_math.py we will not run main code from my_math.py
# there are other ways of importing only specific things from a module - later
# we also have ways of providing aliases for modules - later

# i gain namespacing - no conflict with built-in modules
# presumably there is no robot in standard library...
# i can use robot.Robot
# i can use my_math.Math
# i can use my_math.Math.PI
# i can use robot.Android

new_robot = robot.Robot("Marvin", 1979)
print(new_robot)

# now we can use some math
print(my_math.Math.add(5, 6)) # no conflict with built-in math module

# we can also use circle_area
print(my_math.Math.circle_area(50))

# i can now make an Android
new_android = robot.Android("Marvin", 1979)
print(new_android)
new_android.speak() # only new addition to Android class

 # we can import module from package
 # for example we can import mod_1 from my_package
from my_package import mod_1 # usually we put imports at the top of the file
print(mod_1.add(5, 6))

# so package in Python is just a directory 
# __init__.py is no longer required - but can still use for backwards compatibility

# so let's call mod_2.round
import my_package.mod_2 # i will still need to use full name
print(my_package.mod_2.my_round(3.14159, 2))

# I can specify what I want to import from module
# say I only want Robot class from robot.py
# for fullness I also show how to import multiple things from a module
from robot import Robot, Android # now I can use Robot and Android directly 

also_robot = Robot("R2D2", 1977)
print(also_robot)
# I lose namespacing - no conflict with built-in modules
# presumably there is no Robot in standard library...

# i can also use aliases for my modules
import my_package.mod_2 as m2 # now I can use m2.my_round
print(m2.my_round(3.14159, 2))

# i can also use aliases for my classes or functions or variables
from robot import Robot as R, Android as A # careful with such short names
again_robot = R("C3PO", 1977)
print(again_robot)

# finally do not use * it is possible but not recommended
# from robot import * # now I can use Robot and Android directly
# this can lead to unexpected behavior - you can overwrite built-in functions

# to conclude - modules are just files with python code
# packages are just directories with modules and other subpackages
# library - collection of packages and modules

# generally we put imports at the top of the file
# we import whole module or specific things from module when we sure we need them
# it is possible to assign aliases to modules, classes, functions, variables

# for long module names it is a good idea to aliases

# standard library is huge - look at docs

# let's look at datetime module
# https://docs.python.org/3/library/datetime.html
# it has datetime class inside datetime module
# so typically we import like this
from datetime import datetime # to avoid writing datetime.datetime
# we can also import like this
# import datetime # then we would use datetime.datetime
# sometimes people use aliases
# import datetime as dt # then we would use dt.datetime
# from datetime import datetime as dt # then we would use dt
now = datetime.now()
print(now)
# format it nicely with _ using strftime
print(now.strftime("%Y_%m_%d_%H_%M_%S")) # you can adjust format to your liking
later = datetime.now()
print(later)
# we can calculate how much time passed
print(later - now) # so - is overloaded for datetime objects