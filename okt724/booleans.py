# Let's look at another primitive but fundamental data type - Boolean
# named after George Boole - 19th century mathematician
# the simplest data type there is
# yes/no, true/false, red/black, 1/0, on/off
# Python uses True and False starts with uppercase!
# typically boolean variables start with is_ or sometimes are_
# is_ is just a convention
is_rainy = True
is_sunny = False
print(is_rainy, is_sunny)
print(type(is_rainy), type(is_sunny)) #just for debugging, usually users do not need to see types
print(f"Is it sunny? {is_sunny}")
print(f"Is it raining? {is_rainy}")

# usually we want to obtain our booleans by performing some operation
# simplest would be comparison with ==
# note == NOT = !!
print("Is 2+2 equal to 4?", 2+2 == 4)
print("Is 2+3 equal to 4?", 2+3 == 4)
# we could also save our booleans
# let's check our calculation
is_calculation_correct = 3*3 == 9
print("So 3*3 is equal to 9?", is_calculation_correct)

# we have other operators that return booleans
# there is inequality with !=
# we can also use variables for comparision
a = 2
b = 4
print("a*a == b ?", a*a == b)
print("a*a not equal to b?", a*a != b) # so this will be False, since 2*2 is equal to 4
print(10!=20) # True statement

# then we have greater and lesser operators
print("a < b ?", a < b)
print("a > b ?", a > b)

# we also have <= and >=
# so less or equal, and greater or equal
c = a*a
print("b >= c ?", b >= c)
print("b <= c ?", b <= c) # again True in this case

# python lets us compare multiple variables and numbers in one line
print("-5 < 0 < a < b < c ?", -5 < 0 < a < b < c)
print("-5 <= 0 <= a <= b <= c ?", -5 <= 0 <= a <= b <= c)
# i could also go a > b > c and so on

