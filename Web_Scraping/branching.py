## Let's talk about boolean data types

# Boolean data types are either True or False

is_spring = True
is_raining = False
# it is a good practice to use descriptive variable names
# for booleans is_ prefix is used

# we can get boolean types from comparison operators
# >, <, >=, <=, ==, !=
# these operators return True or False

# let's compare some numbers

print("5 > 3", 5 > 3)
print("5 < 3", 5 < 3)
print("5 == 3", 5 == 3) # == is used to check if two values are equal
print("5 != 3", 5 != 3) # != is used to check if two values are not equal
print("5 >= 3", 5 >= 3)
print("5 <= 3", 5 <= 3)

# typically there will be at least one variable in the comparison
# but we can also compare two variables
a = 5
b = 3
print(f"{a} > {b}", a > b)
print(f"{a} < {b}", a < b)
print(f"{a} == {b}", a == b)
print(f"{a} != {b}", a != b)
print(f"{a} >= {b}", a >= b)
print(f"{a} <= {b}", a <= b)

# we can also compare strings
name = "Valdis"
neighbor = "Voldemārs"
print(f"{name} < {neighbor}", name < neighbor)
# why is this True?
# because strings are compared by their unicode values
# and unicode values are compared by their numerical values
# so we can compare strings by their unicode values
# in this case 2nd letter of Voldemārs is unicode 111
# and 2nd letter of Valdis is unicode 97
print(ord("a"), ord("o"), ord("a") < ord("v"))
# link to ascii table https://www.ascii-code.com/

# if we want to compare by length we can use len() function
print(f"Length of {name} {len(name)} < {len(neighbor)} {neighbor}", len(name) < len(neighbor))

# we can also compare memory using is operator
# this is not very useful in our current context
# will be useful when we use complex data structures

## Boolean Logic
# Named after George Boole - wikipedia: https://en.wikipedia.org/wiki/George_Boole

# Boolean logic is used to combine multiple boolean values

# simplest is negation using not
# not True is False
# not False is True
print("not True is", not True) # in Python we use English not instead of !
print("not False is", not False)
# we can create a toggle with not
is_spring = not is_spring # so reverse of itself
print("is_spring is now", is_spring)
is_spring = not is_spring
print("is_spring is now", is_spring)
is_spring = not is_spring
print("is_spring is now", is_spring)
is_spring = not is_spring
print("is_spring is now", is_spring)

# we can have a conjunction using and
# True and True is True
# True and False is False
# False and True is False
# False and False is False
print("True and True is", True and True)
print("True and False is", True and False)
print("False and True is", False and True)
print("False and False is", False and False)
print("is_spring and is_raining", is_spring and is_raining)
# we can have longer chains of and
print("True and True and True is", True and True and True)
# but one False will make the whole thing False
print("True and True and False is", True and True and False)

# Finally we have disjunction using or
# True or True is True
# True or False is True
# False or True is True
# False or False is False
print("True or True is", True or True)
print("True or False is", True or False)
print("False or True is", False or True)
print("False or False is", False or False)
print("is_spring or is_raining", is_spring or is_raining)

## Branching with if
# if is a keyword in Python
# it is used to create a branch in the code
# if some condition is True then we execute some code
# otherwise we skip it

# let's create a simple program that will ask for a number
# and then print if it is even or odd

# we will use input() function to get user input
# input() function returns a string
# so we need to convert it to integer using int() function

# we will use % operator to check if number is even

# we will use if statement to check if number is even
number = int(input("Please enter a number "))
if number % 2 == 0:
    # we are inside if block
    print(f"{number} is even")
    # this is indented so it will only run if number is even
    print("This will only run if number is even")
else: # else is optional
    # we are inside else block
    print(f"{number} is odd")
    # this is indented so it will only run if number is odd
    print("This will only run if number is odd")
# this will run always we are in main block
print("This will run always")

if is_raining:
    print("It is raining")
    print("Take an umbrella")
else:
    print("It is not raining")
    print("No need for an umbrella")

# we also have elif which is short for else if
# we use it when we have more than two options
# like in the fairy tale of road with three forks - only one is correct

# let's create a simple program that will ask for a number
# and then print if it is over 42 or under 42 or exactly 42

# number = int(input("Please enter a number "))
if number > 42:
    print(f"{number} is over 42")
    # we could have more lines here
elif number < 42:
    print(f"{number} is under 42")
    # we could have more lines here
else:
    print(f"{number} is exactly 42")
    print("This is the answer to the Ultimate Question of Life, the Universe, and Everything")

# normal code that runs always continues after if block
print("This will run always")


# we could have nested if statements

if is_spring:
    print("It is spring")
    if is_raining:
        print("It is raining")
    else:
        print("It is not raining") 
else:
    print("It is not spring")
    if is_raining:
        print("It is raining but not in spring")
    else:
        print("It is not raining but not in spring") 

# so we have 4 options in the nested if

# Error handling
# we can use try except to handle errors

# let's try to convert a string to integer
# number = int("Valdis")
# print(number)

# we can use try except to handle errors
text = input("Please enter a number ")
try:
    number = int(text) # if we have error here we will jump to except
    print(number) # will not run if we have ValueError
except ValueError as e: # good practice to handle specific error
    print(f"Something went wrong {e}")
    # we could assign default value
    number = 0 # to continue working

# so try except is a bit similar to if else

# we use try except when we are not sure if something will work - untrusted input for one

# so idea of try is to try something and if it fails we will handle it
# otherwise the program will crash - we will get an error