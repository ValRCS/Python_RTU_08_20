# we will write a small app
# to calculate your food prices

# first we will ask for user name
# we could hard code it..
# name = "Valdis"
# https://docs.python.org/3/library/functions.html#input
name = input("What is your name friend? ")
print(f"Wow! That's a nice name {name}! I like it...")
# print(f"Now {name} what is your favorite food?")
# # print automatically includes newline by default
# food = input("") # i could have put text from above line inside parenthesis
food = input(f"Now {name} what is your favorite food?")
print(f"Oh {name} you like {food}. I am not adverse to {food} myself.")
price = input(f"How much is/are {food} in your neck of woods?")
# we could replace all , in price with .
price = price.replace(",", ".")
print(f"Aha! {price} for {food} that's inflation for you")
# quantity = input(f"How many kg of {food} do you want to buy today?")
# i could type cast immediately
quantity = float(input(f"How many kg of {food} do you want to buy today?"))

print(f"I would like to calculate total price for {food} x {quantity}")
# this will be error we cant multiply two strings...
# total = quantity * price
# first we need to perform type conversion
# for now we ignore possibility of erronous user input
price = float(price)
# quantity = int(quantity) # could have been float
total = quantity * price
total = round(total, 2) # so round 2 digits after comma
print(f"Super!\nSo you would pay €{total} for {quantity} kg of {food}")