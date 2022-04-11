print("Valdis")
# if we need to use the same value in different places
# in Python first time we use variable we declare it
name = "VisValdis"  # think of name as a shortcut (reference,pointer) to actual value
print(name)
print("Do more stuff")
print(name)
# do not confuse with string "name"
print("name")
print(type(name)) # what data type is stored in name

print("Hello there {name} !") # just string no variables
print(f"Hello there {name} !") # f-string formating

a = 2
b = 3
c = a*b # evaluation happens on the right side first
print(a,b,c)
print(f"{a}*{b}={c} indeed")
print(type(c)) # this is an int type at the moment
# dynamic types means we can change on the run
c = "cūkkarpas akademija" # better to keep same types
print(c)
print(type(c)) # now string

c = 100
print(type(c)) # again int

PI = 3.1415926  # ALL CAPS should be used for constants
print(PI)
print(type(PI)) # float for floating comma types

MY_CONST = 2.71
print(MY_CONST)

my_result = a*b*c
print(my_result)

# finding good names for variables is probably the hardest task
# in programming
# a, b,c are not great names for variables for longer programs
# unless a,b,c have some meaning
a4 = 8.50 # bad name for variable unless it refers to a4 paper size
print(a4)

# typical short variables
# c could be character single character string
# i, it could be used in loops for for iteration
# j, k for nested loops
# s - string
# f - file
# t - time or temporary
# x,y,z - where we have 2D vai 3D coordinates

this_is_too_long_for_a_normal_variable = 5523

# ideally 1 to 3 word long variables

year_2000 = 5_000_345 # right side underscores are just cosmetic
print(year_2000)
y2k = year_2000 # now both y2k and year_2000 point to same value
print(y2k)

print(id(year_2000), id(y2k)) # shows memory address (virtual) for variable
# id we would use on more complex data types when comparing contents or copy

round_pi = round(PI, 2)
print(round_pi)
small_pi = round(PI) # no digits after comma
print(small_pi)

# type-casting to different data types
whole_pi = int(PI) # get the whole (integer) partition of number
print(whole_pi)

print(round(MY_CONST), int(MY_CONST))

my_string = str(a4)  # almost anything can be converted to str
print(my_string)

print(a4*3)
print(my_string*3) # difference

import math
print(math.floor(PI))
print(math.ceil(PI))
print(math.pi)

my_text = "3.3426"
my_float = float(my_text)
print(my_float)

my_number = 5
print("Valdis " + str(my_number))
# better would be with f-string
print(f"Valdis {my_number}")

# floats are weird (any language) IEEE-754 standard
a = 0.1
b = 0.2
c = a+b
# will c be 0.3 ?
print(a,b,c)
c = round(c, 4)  # 4 here is precision
print(c)
print(round(PI,4))
