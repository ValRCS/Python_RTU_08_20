print("Valdis")
my_name = "VisValdis" # = is assignment not equality
print(my_name)
# 
print(my_name)
# # daru ko vēl
print("Doing something else")
print(my_name)
# 
# # use short variable names when it is obvious what they refer to
# # or when they are not going to be used
a = 2
b = 3
c = a*b
print(a,b,c)
# A = 20 # lets not do this, capital starts should be used for classes
# mixedCase = "ok if project already uses"

d=33 # less used, but its ok
# 
# # c - character
# # x, y, z - 2D, 3D coordinates
# # i - iterators, index
# # n - number,
# # s - sometimes string
# # t - temporary, if used as a throwaway in short code
# # f - fileDescriptor
# 
# # variable in Python should start with small lower letter
# # can be followed by uppercase , numbers and some symbols such a _
# myName = "Valdis" # camelCase, less used in Python
# 
very_long_variable_name = 9000
# 
# # if you name your variable with ALL CAPS that indicates a constant
MY_PI = 3.1415926
# MY_PI = 3 # i could change it but thats bad practice
# # this is only a convention, you can still change the contents, just a bad style
# 
# # avoid using this if you have my_name
# my_Name = "Voldis" # different from my_name !!!! avoid
my_name = "Still Valdis with extras" # changed original
# 
# # variable contents (references) can be changed
print(a,b,c,d)
d = a + b + c # evaluation happens from right to left
print(a,b,c,d)
# 
print(type(my_name), type(a), type(MY_PI))

kaķis = "minka" # avoid!!
cat = "muris" # good!
my_cat = "ņauva varam" 
# 
is_sunny = False # Booleans
is_raining = True
# 
nothing = None # special none type
print(nothing, type(nothing))
# 
# # Python is garbage collected automatically
# # if some value is not used anymore it is cleaned from memory after some time
my_name = "Voldemars"
# # since we have no values pointing to "VisValdis"
# # "Valdis" will not be available
# 
# # to be fully precise Python always keeps first 256 numbers in memory
# # and also from -10 to -1
# 
my_zero = 0
also_zero = 0 # this and above point to same value 0
my_one = 1
my_big_number = 43242
my_million = 1_000_000 # _ will be ignored it is just for show
# 
# # we can print where in memory our values reside
print(id(my_zero), id(also_zero), id(my_one), id(a), id(b), id(my_big_number))