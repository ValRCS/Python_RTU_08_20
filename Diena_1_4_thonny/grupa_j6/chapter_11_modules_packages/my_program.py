# let's see how we can import modules and packages

# usually all imports go at the top of the file
# import module_name
# it is possible to import only specific functions from a module

# what is the order on how python looks for modules?
# let's import sys and see what is in sys.path
import sys # standard library module
# all standard library modules docs are here: https://docs.python.org/3/library/
print(sys.path) # we will see the order of paths where python looks for modules
# so current folder is first, then python standard library, then site-packages etc

# what is a module then?
# it is a file with .py extension - so simple text file with .py extension
# so any regular file can be a module
# but it is a module only if we import it
# so let's import my_module.py
import my_module # we can import any file that is in the same folder

# what will happen?
# python will execute all code in my_module.py not under any function or class

# we get access to everything in my_module.py

# we can access variables
print(my_module.my_variable) # notice the . notation
print(my_module.my_list)
print(my_module.my_string)

# i can change the variable in my_module.py
my_module.my_variable = 100
print(my_module.my_variable)

# i can call my function
print(my_module.my_function(10, 20))

# i can create objects from my class
my_object = my_module.MyClass("Valdis")
print(my_object) # we have pretty print because we have __str__ method

# so what do I get when I use modules?
# reasons to use modules
# 1. code reuse - we can use code from other modules
# 2. organization - we can organize our code into modules
# 3. abstraction - we can hide implementation details in modules
# 4. namespace separation - we can have same names in different modules
# 5. performance - we can load modules only when we need them

# also we can split work between multiple programmers - team work

# we have other ways of importing modules
# we could change a name of the module to something shorter(less typing) or longer...

import my_module as mm # we can import any file that is in the same folder
# typical to use two or three letter abbreviations
# we can use any name we want but it is good to be consistent
print(mm.my_variable) # notice the . notation
# also notice we have same variable value as before from my_module.py !
mm.my_list.append(200)
print(mm.my_list)
print(my_module.my_list) # we have same list because we are using same module

# i can also import specific things from a module - one or more
from my_module import my_variable, my_list, my_function
# now we call them directly without any module name
print(my_variable) # again reference to my_module.my_variable
print(my_list) # same my_module.my_list
print(my_function(10, 20))
# with above we do not have access to my_string or MyClass directly
# also we need to be careful not to overwrite any variables or functions
#  that are in global namespace

# also careful to not name your modules the same name as standard library modules
# why?
# because we will not be able to import the standard library module anymore
# so do not name your modules sys.py or math.py or random.py, datetime.py etc

# we can import specific things from a module and rename them to alias
from my_module import my_variable as mv  #, my_list as ml, my_function as mf
print(mv)
print(my_variable)
print(mm.my_variable)
print(my_module.my_variable)
# they are all the same object
print(mv is my_variable, my_variable is mm.my_variable, mm.my_variable is my_module.my_variable) # so we have two references to the same object
# normally we only import once and then use the same reference , no need to import 4 times!

# finally we have a way to import everything from a module
# this is not recommended because we can overwrite our own variables
# import * from my_module # this is not recommended! 

# if I only want class I need to import it directly
from my_module import MyClass # not import my_module.MyClass
my_object_2 = MyClass("Valdis")

# so how would I import Robot class from Robot.py file?
from robot import Robot
my_robot = Robot("Valdis")
print(my_robot)
# if i used import Robot then I would need to use Robot.Robot("Valdis")
import robot
my_robot_2 = robot.Robot("Robbie")
print(my_robot_2)
# again no need to import twice! use just one import statement

# now how do I import modules from packages?
# we can import packages and modules from packages

import my_package.my_mod_1 # we can import any file that is in the same folder
# now I can call
print(my_package.my_mod_1.mult(10,20))
# nicer would be to use alias
import my_package.my_mod_2 as mp2
print(mp2.add(10,20))
# i could creat deeper packages
# folder with subfolders and files etc

# if we have module and package, how about library?
# library is a collection of packages and modules
