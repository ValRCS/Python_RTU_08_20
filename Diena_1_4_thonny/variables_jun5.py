# how about some variables to store our data?
a = 5 # in Python we do not need to declare variables
# first assignment declares it
# also there are not type declaration
print(a)
print(type(a)) # data have types - dynamically assigned
my_name = "Valdis"
print(my_name)
print(f"Hello my name is {my_name} and my number is {a}")
# i can mutate variables
my_name = "Voldemārs"
print(my_name)
# so variables are case sensitive
# bad practice to use these similar names
myName = "Voldem"
myname = "Wolly"
print(my_name, myName, myname)

# Python for multiple word variables
# we use _ to separate such as my_variable
# camelStyle is less used and not recommended
name = "Valdis"
print(name) # prints contents of variable
print("name") # this is just a string literal not a variable!
print(type(name)) # so variable name is of type str - string

######################### just a comment ########
# in assignment right side is executed first
# assignment is done with = 
b = a + 100 # b will be integer because a and 100 are integers
print(a, b)
c = b * a
d = b ** a # 105 to the 5th power
print(c)
print(d)
print(f"{my_name} created a big number {d}")



