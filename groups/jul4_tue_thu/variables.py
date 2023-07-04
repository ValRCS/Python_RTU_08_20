# we usually will want to save some data while the program is running
# Python has automatic type inference no need to declare data types
a = 2 # duck typing, it quacks like int, walks like int, it is a int
print(a)
# we can determine data type by type
print(type(a)) # class int
# we can find memory address that variable points to
print(id(a)) # not real memory since OS manages it for us
print(hex(id(a)))
b = 2
print(id(b)) # points to same address
name = "Valdis"
my_name = "Valdis"
print(id(name), id(my_name), name is my_name) # is compares by id
# i change name to Voldemars
name = "Voldemārs"
print(id(name), id(my_name), name is my_name) # is compares by id

# when nothing points to value then it is garbage collected (usually very quickly)

food = "potatoes"
print(food)
# https://peps.python.org/pep-0008/#function-and-variable-names
# food = 100 # we can do this but unless it is throwaway variable avoid doing this
# print(food)

# we can use string interpolation using f-strings since Python 3.6+
# so i can use { } to put any expression inside including variables
print(f"Hello {my_name}, so I hear you like {food}?")
# there is also older .format method
# also we can use concatenate with +
# i could have save this first
greeting = f"Hello {my_name}, so I hear you like {food}?"
print(greeting)
# i can put arbitrary expressions inside
print(f"So {a} to the power of 10 is {a**10}")
# i can format numbers with f strings
# https://peps.python.org/pep-0008/#constants
PI = 3.1415926 # this is not true constant but by convention indicates consant
print(f"{PI=} {PI} {PI:.2f} {PI:.4f}") # original is not changed


