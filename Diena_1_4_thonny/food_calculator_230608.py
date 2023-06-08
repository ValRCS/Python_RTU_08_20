# we will make a simple application for
# calculating food prices
name = input("What is your name? ")
print(f"Nice name {name}! I like it.")
food = input(f"What is your favorite food {name}? ")
print(f"Wow I like {food} too!")
# now we will run into a problem with numbers
price = input(f"How much does 1kg of {food} costs near you? ")
double_price = price * 2 # will not work correctly
print(f"Hmm so double price would be {double_price} ?")
# so solution is to convert string to float
price = float(price) # for now we assume input will be correct
# so price was converted to floating point
real_double_price = price * 2
print(f"Now really double price would be {real_double_price} !")
# we can do this conversion immediately
quantity = int(input(f"How many kg of {food} do you want to buy? "))
total = price * quantity
# note sum is not good name for variable because it is used by Python
# https://docs.python.org/3/library/functions.html
# possible but would lead to a mess
print(f"""So {name}
You would pay €{total:.2f} for {quantity} kg of {food}.
Does that sound reasonable?""")
# notice .2f which will show only 2 digits after comma
print(round(total,0)) # so zero digits after comma
print(round(total,1))
print(round(total,2))
print(round(total,3))
# total still is whatever the calc did
# now we will actually overwrite it
total = round(total, 2) # i could do this if I am satisfied with my result
print(f"so {total} for for {quantity} kg of {food}")

# rounding in Python is so called round to even
# this means 2.5 rounds to 2 and 3.5 rounds to 4
# 4.5 rounds to 4 and 5.5 rounds to 6



