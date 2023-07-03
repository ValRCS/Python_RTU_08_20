# we might want to save some data while we are working - program is running
# Python offers dynamic typing and type inference - automatic types
a = 5
print(a)
print(type(a)) # for debugging less used in real code
# i can even find where in memory(virtual) the data lives
print("Memory address", id(a)) # not real memory address, OS specific

my_name = "Valdis"
print(my_name)
# i could do more stuff
# then decide to print it again
# f means formatted string
print(f"Hello, my name is {my_name}") # f -string from Python 3.6+

# so variables should start with lower or upper case letter
# can contain numbers, can contain _ underscores
# camelCase is generally avoided

# using f-strings I can format arbitrary evaluations
print(f"Variable a - {a} - squared it is {a**2}, nice isn't?")
# otherwise the old way would be with format or with concatenations
print("Variable " + str(a) + " squared is " + str(a**2))
print("Variable", a, "squared is",  a**2)
print("Variable", a, "squared is",  a**2, sep="***😀===") # i can define what comma sep does

drink = "beer"
big_drink = drink * 7 # i can multiply strings with number
print(big_drink)
print("*"*40)

