# # print(my_name)  # error because my_name is not yet known
# i create variables at the time of assignemnt
my_name = "Valdis"
print(my_name)
print(type(my_name))
also_my_name = "Valdis"

# we use either " or ' for strings
my_text = "Alice said 'where is the rabbit?' hmm"
print(my_text)
also_text = 'I wanted " in my text'
print(also_text)
print(my_name)
# 
# print(my_name)
# 
a = 2  #not an equality but assignment from right to left
b = 5
c = b+a  # from right side
# # use such short names only for short segments
print(a,b,c)
print(f"{a}+{b}={c}") # f-strings
result_string = f"{a}+{b}={c}"
print(result_string)

#a, b, c are integers at the moment
print(type(a))

# variable identificators are case sensitive!
my_Name = "Voldemars"
print(my_Name)

weather_2022_05 = "sunny"
# 
# # variables start with small letter
# # there is a special variable _ means we do not care about it
# 
# myName = "Valdis"  # avoid if we already using my_name
# print(my_name, myName) # bad style to mix both styles
# 
# # ALL CAPS signify constants
# # that's just a convention, theoretically you can change them
PI = 3.1415926  #usually at the start of program
print("This is just a variable", PI)
print(f"This is just a variable {PI}")
# possible but not recommended...
# PI = 3
# print(f"Hmm my math looks strange {PI}")
# 
# # i, it commonly used for looping
# # j,k as well for more looping (cycling)
# 
# # x,y,z where we have some 2D/3D coordinates
# # c could be character in a string
# # f for filestream
# # t for time or temporary, temperature
# s could be string
# 
# b2 = 325 # legal but try to use sparingly we have better options
# a4 = 8.50 # good name for A4 paper but otherwise avoid
# 
# # variables have dynamically assigned data types
print(a, type(a))
print(my_name, type(my_name))
print(f"Variable {my_name} is of type {type(my_name)}")
print(type(PI))
# 
# # floats have their limitations
# # imposed by IEEE-754 standard
a = 0.1 # here a is changed from int to float
b = 0.2
c = a + b  # c should be 0.3 but floats are weird
print(a,b,c)
d = round(c, 2) # so round up to 2 digits after comma
print(d)
round_pi = round(PI,4)  # 4 digits after comma
print(round_pi)
# round(somenumber) will round 0 digits after comma
# so 1.5 is rounded UP
print(round(1.50001), round(1.5), round(1.4999))
#
# type casting
simple_pi = int(PI) # we get integer part of number
print(simple_pi, type(simple_pi))
# 
floating_pi = float(simple_pi)
print(floating_pi, type(floating_pi))
# 
# # we can turn anything into a string
pi_string = str(PI)
print(pi_string, type(pi_string))
print("Hello Mr. " + str(7))
print(f"Hello Mr. {PI}") # i can skip conversion with f-strings
# 
# print(type(0.334234))
print(int('007'))  # we can transfer to string

my_float = float("3.242525627") # I can convert text to float
print(my_float)

pi_float = float(pi_string)
print(pi_float)
# pi_int = int(pi_string) # ValueError
# print(pi_int)
pi_int = int(pi_float) # so float-> int no problem
print(pi_int) # again 3
some_int = int("-3412515774234") # this works
print(some_int)

some_float = 5.3422321
some_int = 10_000
result = some_float + some_int # float and int are both numeric
print(result)
print(round(result, 2))
rounded_result = round(result,2)
print(rounded_result)

# int -> str, int -> float no problem
# anything -> str
# float -> int
# 
# 