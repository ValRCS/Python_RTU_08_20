name = input("What is your name friend? ") # input always returns string
print(f"Why that's a nice name {name}! I like it!")
food = input("What is your favorite food? ")
print(f"Oh {food}, I like {food} myself")
price = input(f"How much is {food} in your market?")
double_price = price * 2
# not quite what we want
# print(f"So double the price is {double_price}??")
# solution we type-cast string to integer or float
# possible Error on bad input - we can handle it later
real_price = float(price)
# we can convert immediately
# assumption here that people only buy whole kilos of some food
# could have used float
quantity = int(input(f"And how many kg do you want to buy of {food}?"))

total = real_price * quantity

# will display 4 digits after comma not changing total
print(f"Wow so {quantity} kg of {food} would cost {total:.4f}.. hmm")

# we might want to round it after all, changing total to rounded version
total = round(total, 2) # 2 digits after comma
print(f"Wow so {quantity} kg of {food} would cost {total}.. hmm")


# so we have str, int, float so far
# we can convert anything to str
# we can convert float to int or str
# converting float to int we lose data after decimal
# we can convert int to float

# floats are tricky IEEE-754 standard
# not all rational numbers can be stored properly
# https://en.wikipedia.org/wiki/IEEE_754

# a = 0.1
# b = 0.2
# c = a + b
# print(a, b, c)
# # what do we do we can round after comma
# # also we can force display with format
# print(f"so {c} or {c:.4f}") # c is not changed
# # or I could round the c
# PI = 3.1415926 # capitals indicate constant, BUT it is not hard constant!
# rounded_pi = round(PI, 4) # 4 digits after comma
# print(PI, rounded_pi)


# a = 5
# b = 5
# print(id(a), id(b)) # same spot in memory for PRIMITIVE TYPES
# name = "Valdis"
# another_name = "Valdis"
# different_name = "Voldis"
# print(id(name), id(another_name), id(different_name))
# as soon as no variables point to "Valdis" the memory holding
# "Valdis" will be garbage collected - automatically
# for complex types (lists, dictionaries) it might not be true
