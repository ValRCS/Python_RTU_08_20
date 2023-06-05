# good practice for naming variables
# use english names
# lower case
# multiple words separated by _
# use meaningful names
# a,b,c should be used for very short fragments/functions
# a4 would only make sense if we are talking a4 paper
# x, y are okay for 2d
# x,y,z for 3d
# i,j for loops
# t for temporary
# s for string also short fragments
# my_variable is also bad name because has no semantic meaningful

my_name = "Valdis"
name = "Some place" # okay name
current_year = 2023
year = 2023 # okay but maybe not too clear
PI = 3.1415926 # not really a constant
print(PI)
# uppercase are generally understood to be on constant
PI = 3 # Alabama in 19th century
print(PI)
# not a good idea!
# 🍺 = "this is beer"
# print(🍺)
our_beer = "this is fine 🍺"
print(our_beer)

my_home_city = "Rīga" # this is fine
# up to 4 words should be enough
this_is_too_long_a_name_for_variable = "too loong"
print(my_home_city)

PI = 3.1415926
print(PI, round(PI,4), round(PI,2), round(PI,0))
round_pi = round(PI,2)
# i could do more stuff here
print(round_pi)
# my_result should be named to something what it means
my_result = round(10/6, 3)
print(my_result)
# round uses even roundin
# means .5 are rounded to even number
# so 2.5 to 2
# but 3.5 to 4
print(round(1.5))
print(round(2.5)) # down to even 2
print(round(2.51))
print(round(3.5)) # up to even 4
print(round(3.51))