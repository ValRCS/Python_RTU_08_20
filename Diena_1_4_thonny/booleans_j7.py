# Booleans
# the simplest data type there is 0 or 1, yes or no,
is_sunny = True
is_summer = True
is_rainy = False
print(is_sunny, is_summer, is_rainy)
print(f"is_sunny is {is_sunny} this is data type of {type(is_sunny)} ")

# i can use comparison == to obtain Boolean values
print(2 * 2 == 4)  # notice == NOT = !!!
# I can assign results of comparison
is_calc_correct = 2*2 == 5 # the expression will be evaluated from right side
print(is_calc_correct)

# we can also use in equality
a = 2
b = 4
is_math_good = a*2 == b
print(is_math_good)
print(4 != 5) # True because values are NOT EQUAL
are_values_not_equal = a*2 != b # False since the values are EQUAL
print(are_values_not_equal) # since 4 != 4 is False

# greater than
print("a > b", a > b)
print("b > a", b > a)
# i can chain multiple comparison
c = 10
print("c > b > a", c > b > a) # all comparisons must be true to get true
cba_in_order = c > b > a
print(cba_in_order)
d = 42
print(d > c > b > a) # and so on

# less than
print(f"{a} < {b}", a < b)
print("b < a", b < a)

# we also have >= greater or equal
print(f"{a*2} >= {b}", a*2 >= b)

# we also have <= less or equal
print(f"{a*2} <= {b}", a*2 <= b)
print(f"{a*20} <= {b}", a*20 <= b)

# there is also special is comparision
# is compares whether variables refer to same data in memory
# this will be more important when we have complex data types
print(a is 2) # do not use is for numerics

empty_value = None # Captain Nemo - nil nothing
print(empty_value is None) # this is considered good practice

my_name = "Valdis"
neighbor_name = "Voldemars"
print(f"{my_name} < {neighbor_name} ? ", my_name < neighbor_name)
# True but why is it True?
print("Valdis" < "Vol") # also True
# for length we simply use len function
# available for strings and some other data types
print(f"{len(my_name)} < {len(neighbor_name)} ? "
      , len(my_name) < len(neighbor_name))

# lexigraphical comparision will mean that Latvian letters will have higher
# value than English letters
print(ord("k"), ord("ķ"))