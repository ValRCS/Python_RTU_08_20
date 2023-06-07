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