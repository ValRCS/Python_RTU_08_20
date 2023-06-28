# a simple program that will demonstrate how to import a modules and packages

# usually ALL imports go at the top of the file
# first let's see where python looks for modules
import sys # this is standard library module
print(sys.path) # this is a list of paths where python looks for modules

# list of all standard library modules
# https://docs.python.org/3/library/index.html
# so those are modules that are already installed with python
# all you have to do is import them and use them

# what is module after all?
# module is a file with python code with .py extension - so simple

# so I will import my_module.py because it is in the same folder
import my_module

# now I can use my_module.my_data
print(my_module.my_data)
print(my_module.my_list)
print(my_module.my_string)
# and i can use my_module.my_function
result = my_module.my_function(10, 20)
print(result)
print(my_module.another_function(10, 20))

# i can make object from my class
my_car = my_module.Car("Ford", "Focus")
another_car = my_module.Car("Audi", "A4")

# so why use modules?
# 1. to organize code - we can put related code in one file
# 2. to reuse code - we can import module in many programs
# 3. to avoid name conflicts - we can use module name to access code
# 4. to make code easier to understand - we can use module name to access code

# so how would I import a specific Robot class from Robot.py?
# i could do it like this
from Robot import Robot # notice how it is similar from datetime import datetime
# so now I can use Robot class
robot1 = Robot("R2D2", 1977)

# i could import module and rename it - this is very common
import Robot as rb # two letter names are very common
robot2 = rb.Robot("C3PO", 1977) # of course I also have Robot imported already

# finally I could import Robot class and rename it
from Robot import Robot as RB # a bit less common
robot3 = RB("BB8", 2015)

# of course I could have just done the basic import
import Robot
robot4 = Robot.Robot("Johnny5", 1977)
# again only use one of the four ways to import
my_data = 500
# of course I can change values of variables in my_module
my_module.my_data = 200
my_module.my_list.append(6)
my_module.my_string = "Hello from my_program.py"
# print those values
print(my_module.my_data)
print(my_module.my_list)
print(my_module.my_string)

# if there is potential conflict we import as alias
import my_module as mm # this is very common
# usually we import only once in a program
mm.my_data = 300
mm.my_list.append(7)
# print those values
print(mm.my_data)
print(my_module.my_data) # so this is also changed
print(mm.my_list)



# one thing to be careful, avoid calling your files same as 
# standard library modules - such as string.py or datetime.py 
# then your modules will have priority over standard library modules

# a bit careful here
# print(my_data)  # this is my_data from my_program.py not imported my_data
# from my_module import my_data # possible conflict with my_data already defined
# print(my_data)
# finally do not import with * !!!!
# from my_module import * # this is bad practice
# hard to know exactly what is imported and pollutes namespace -
#  global scope is full of junk

# now what is package?
# package is a folder with .py files and optional __init__.py file

# so now let's import my_module_1 from my_package
import my_package.my_module_1
print(my_package.my_module_1.my_function_1(10, 20))
# i could import with alias
import my_package.my_module_2 as mm2
print(mm2.my_function_2(10, 20))
# finally i could import just a single function (or class or variable)
from my_package.my_module_2 import my_function_2
print(my_function_2(10, 200))