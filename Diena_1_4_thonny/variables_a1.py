print("Valdis") # so called string literal
my_name = "Valdis" # in Python we create variables when we use them
print(my_name)
print("Do more stuff")
print("Hello there", my_name) # lazy style by default , separator is one whitespace
print("How are you doing " + my_name + "?")
# there are some other ones but my favorite is the bew\
# f-strings - string interpolation
print("What are your plans for this evening {my_name}?")
print(f"What are your plans for this evening {my_name}?")
print(type(my_name)) # my_name is pointing at a string "Valdis"
my_number = 7
print(my_number)
print(f"{my_name} is {my_number} your lucky number?")
print(type(my_number)) # so int
my_name = 9000 # we can do this but logically better not
print(type(my_name)) # so now my_name is int type
print(my_name)
my_name = "Valdis"
print(f"Whew got my name {my_name} back")
my_friend = 'Edgars' # same as using "Edgars"
greeting = "Rabbit told Alice 'Let's jump' and she did"
print(greeting)
# myName = "Valdis" # do not mix naming styles in one program!

# you can use short names but for only short portions of program
# in a longer program you will forget what these mean!!!
a = 5
b = 3
c = a+b  # evaluation happens from right side first
print(a,b,c)

# popular short names for variables
# c for single character
# f for file stream or file
# s for string, text
# t for time or temporary
# x,y,z anywhere you need 2D,3D coordinates
# i, it, j, k - iterators in loops - in lecture 4

# next one is too long for practical reason
really_long_variable_with_a_long_description = "too much really"
# best are 2 or 3 word variables if one is not enough

a1 = 70 # can be used but use sparing
# a2, a3, a4 smells pretty bad - looks like we need a list data structure
# exception would be if those were paper sizes
year_2000 = 2000 # possible as well but use sparingly

my_float = 2.71828
print(type(my_float))
print(my_float)
# floats are weird - IEEE-754 applies to all languages
a = 0.1
b = 0.2
c = a+b
print(a,b,c)
print(f"{a}+{b}={c}")
rounded_result = round(c, 2) # round to 2 digits after comma
print(rounded_result)

PI = 3.1415926 # if we use capitals conventions says this should be constant
round_pi = round(PI, 4)
print(round_pi)
print(round(0.49), round(0.50), round(0.500001), round(0.51))
flat_pi = round(PI)
print(flat_pi)
print(type(flat_pi))
whole_pi = int(PI) # i can convert any float to whole
# int works then integer floor for positives
print(whole_pi, type(whole_pi))
float_pi = float(whole_pi)
print(float_pi)
# print(my_name + my_number) # will not work since str + int has no operation
print(my_name + " " + str(my_number)) # kind of ugly
print(f"{my_name} {my_number}")  # better use f-strings
str_from_number = str(my_number)
print(type(str_from_number))