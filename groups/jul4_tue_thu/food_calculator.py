name = input("What is your name friend? ") # input returns string after return
print(f"Nice to meet you {name}!")
food = input(f"{name} what is your favorite food? ")
print(f"Wow I like {food} too")
price = input(f"How much is/are {food} in your local market?")
double_price = price*2
# # hmm not quite what we want
# print(f"So {price} double is {double_price} ??")
# so I need to type-cast to correct data type
# here either int or float would be appropriate
# we leave error checking for another discussion
# we cast string to floating point number
price = float(price)
# i can cast immediately
quantity = int(input(f"How many kg of {food} do you want to buy?"))
total = price * quantity
# so if it involves float
print(f"Wow so {quantity} kg of {food} costs {total}. Inflation, eh?")
# https://en.wikipedia.org/wiki/IEEE_754
# what can we do?
# we can just format output leaving data intact
print(f"Wow so {quantity} kg of {food} costs {total:.2f}. Inflation, eh?")
# i can also use built in round to modify original / or save to new variable
total = round(total, 2) # so round to 2 digits after comma
# i can add number of how many spaces to allocate

print(f"Wow so {quantity} kg of {food} costs {total:10.2f}. Inflation, eh?")

