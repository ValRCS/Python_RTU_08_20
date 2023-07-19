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