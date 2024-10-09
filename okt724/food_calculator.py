# Let's make a food price calculator
print("This program will calculate the price of your favorite food")
# first let's get the name of the person
# so name will be our first variable, it could be anything starting with letter
# instead of assigning
# name = "Valdis"
# we will use input function to obtain name from console input by user
name = input("What is your name friend? ") # input() would print nothing
print(f"Why, that is a nice name - {name}! I like it :) ")
# input always returns string - text, nothing else after enter is pressed
# now let's ask for the favorite food
# same type of operation just different variable
# note use of f-strings for inserting of variables in text
food = input(f"What is your your favorite food {name}?")
print(f"Cool, I love {food} myself as well")
# now we would like to find a price for the food
# first we will print the prompt - no input
print(f"So {name}, how much is 1kg of {food} in your corner store?")
# now I will go to next line and ask for input
price = input("->") # could be just input(), but cursor could be hard to see
print(f"Oh, {price} for 1kg of {food} that is quite a bit, isn't it?")
# let's calculate the price if it is doubled or for 2kg
price_2kg = price * 2 # will this work?
print(f"So would 2kg price for {food} be {price_2kg}?")
# so above is most likely not what we want
# what is the issue?
# we multiplied string, because input ALWAYS returns string
# Python has several primitive data types
# we know str already - that is string
# for numbers we have two common primitives
# int - integer, no commas
# float - floating point, has commas, precise for around 15 digits after comma
# we can attempt to convert string to float with float function
price_float = float(price) # I added _float for education purposed but could be any other name
# note that we depend on user to provide valid number
price_3kg = price_float * 3
print("Now let's try this again")
print(f"Then 3kg of {food} should be {price_3kg}")

# now let's ask how much food they
quantity = input(f"How many kg of {food} do you want to buy {name}?")
print(f"Wow you want to buy {quantity} kg of {food}")
# we need quantity to be number
# let's assume we only allow full numbers - integers
# then lets convert quantity
# I will overwrite the old quantity with new quantity
quantity = int(quantity) # again will fail on non integers
# now we are almost ready to calculate
# first let's print data types
# usually we do not need to print them, but good for debugging purposes
print(f"name is {name} and its data type is {type(name)}")
print(f"price is {price} and its data type is {type(price)}")
print(f"price_float is {price_float} and its data type is {type(price_float)}")
print(f"quantity is {quantity} and its data type is {type(quantity)}")
# now let's calculate the total from price and quantity
total = price_float * quantity
print(f"Alrighty {name}! So {quantity} kg of {food} would be {total}")
# it is possible the total would not be so nice due to floats
# we might want to round it up a bit
total_int = int(total) # this will round down guaranteed to integer
total = round(total, 2) # 2 digits after comma, we lose all the extra digits
# old value of total was overwritten by rounded version 
print(f"So {total} price while integer portion is {total_int} Euros")
# there are a couple more primite data types for next lesson
