my_name = "Valdis" # variables can be used immediately without declaration
my_Name = "Visvaldis" # different from line 1
# print("Valdis")
# print("Valdis")
print(my_name)

print("Hello ", my_name) # this works because , by default gives you one whitespace
print("Hello " + my_name) # less nice
print(f"Nice to meet you {my_name}") # f-strings from Python 3.6 and up
print(type(my_name)) # we can find out data type of variable
print(id(my_name)) # also the memory(virtual) address of where the variable points to

# naming variables
# variables start with lower case alpha leter(English please only)
# after that we can use numbers, letters and some symbols such as _

myName = "Valdis" # so called camelCase less used in Pytho
# if you use one style stick to it in one code
print(my_name, myName)
print(id(my_name), id(myName)) # both variables point to same memory address

a = 120  # so a automatically becomes int (integer) data type
b = 30
c = a + b # evaluation happens from right to left
print(a,b,c)
print(type(a),type(b), type(c))

# data types can change!!
a = "Aha!" # generally we do not want to change data types
print(a)
print(type(a),type(b), type(c))

# c = a + b # this will not work as given, think about what we are adding
c = a + str(b) # so we can make a string out of b
# str is an example of type casting
print(a,b,c)

my_msg = "9000"
my_num = int(my_msg) # not everything can be made into int, but here no problem

print(my_msg, my_num) # not much difference when printed

my_result = my_num + 55
print(my_result)

my_long_msg = "Hello\n darkness \n my old friend"
print(my_long_msg)

# \U is for symbols after 65536 decimal (after FFFF in hex)
smiley_again = "Aha ! 😀 -> \U0001F600" # for Unicode encoded with more than 4 Hex symbols you need to use 32
print(smiley_again)
# if unicode fits into 4 hex symbols then we use \u
some_characters = "I think this is chinese: \u53F8 anyone know it?"
print(some_characters)

# one more data type
my_pi = 3.1415926
print(my_pi)
import math # we can also import additional functionality and values
print(math.pi) # if you need more precise

print(type(my_pi)) # so float represents a value with a floating comma ..

my_int = int(my_pi) # so all digits after comma are lost
my_float_back = float(my_int) # well what will happen with our pi ?
print(my_pi, my_int, my_float_back)

is_sunny = True
is_raining = False
