# print(my_name)  # error because my_name is not yet known
my_name = "Valdis"
print(my_name)
my_text = "Alice said 'where is the rabbit?' hmm"
print(my_text)
also_text = 'I wanted " in my text'
print(also_text)

print(my_name)

a = 2  #not an equality but assignment
b = 5
c = b+a  # from right side
# use such short names only for short segments
print(a,b,c)
print(f"{a}+{b}={c}") # f-strings
result_string = f"{a}+{b}={c}"
print(result_string)

# variables start with small letter
# there is a special variable _ means we do not care about it

myName = "Valdis"  # avoid if we already using my_name
print(my_name, myName) # bad style to mix both styles

# ALL CAPS signify constants
# that's just a convention, theoretically you can change them
PI = 3.1415926
print("This is just a variable", PI)
print(f"This is just a variable {PI}")
# PI = 3
# print(f"Hmm my math looks strange {PI}")

# i, it commonly used for looping
# j,k as well for more looping (cycling)

# x,y,z where we have some 2D/3D coordinates
# c could be character in a string
# f for filestream
# t for time or temporary

b2 = 325 # legal but try to use sparingly we have better options

# variables have dynamically assigned data types
print(a, type(a))
print(my_name, type(my_name))
print(f"Variable {my_name} is of type {type(my_name)}")
print(type(PI))

# floats have their limitations
# imposed by IEEE-754 standard
a = 0.1
b = 0.2
c = a + b  # c should be 0.3 but floats are weird
print(a,b,c)
d = round(c, 2) # so round up to 2 digits after comma
print(d)
round_pi = round(PI,4)  # 4 digits after comma
print(round_pi)
print(round(0.50001), round(0.5), round(0.4999))

simple_pi = int(PI) # we get integer part of number
print(simple_pi, type(simple_pi))

floating_pi = float(simple_pi)
print(floating_pi, type(floating_pi))

# we can turn anything into a string
pi_string = str(PI)
print(pi_string, type(pi_string))
print("Hello Mr. " + str(7))

print(type(0.334234))
print(int('007'))  # we can transfer to string




