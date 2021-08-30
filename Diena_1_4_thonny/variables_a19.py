print("Valdis")
# we declare variables in Python when we first use them
my_name = "Valdis"
print(my_name)
print(type(my_name))
my_num = 42
print(my_num)
print(type(my_num))
a = 42
b = 42
print(a,b,my_num)
b = 9001
c = 9001
my_result = b + c
print(b,c,my_result)
c += 10000 # shorter way of writing c = c + 10000
print(b,c,my_result)
d = a # d points to the same value as a
print(a,d)

a2 = 50 # we can do this but generally this smells of improvement
a3 = 51
a4 = 52 # there are better data structures

# one of the hardest things in programming is naming variables

launch_codes_to_nuclear_weapons = "GoodBEEF" # a bit long

# short variables which are fine
# x,y,z  would be fine when dealing with coordinates
# i for iterator,
# t for temporary
# c for characters
# f for file

# h for height
# l for length is a bit iffy, use of l is discouraged
# why? because l can be confused with 1 and I on some systems

# all capital variable means that it really is a constant
RTU = "Riga Technical University"
# we shouldn't change this

# we use English
kaķis = "my cat"  # please do not do this :)
print(kaķis)
my_cat = "my cat Muris" # that is fine
smiley_msg = "AHmm ! 😀 -> \u1F600" # this is 16bit Unicode and 0
print(smiley_msg)
smiley_again = "Aha ! 😀 -> \U0001F600" # for Unicode encoded with more than 4 Hex symbols you need to use 32
print(smiley_again)
