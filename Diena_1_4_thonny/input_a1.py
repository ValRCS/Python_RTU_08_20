name = input("What is your name friendo? ")
print(f"That is a nice name {name}!")
# input always gets a string
food = input(f"What is your favorite food {name}?")
print(f"Cool I like {food} too")
price = input(f"How much does {food} cost in your store in €?")
double_price = price*2
print(double_price) # will this be what we want?
# we want to cast our string to int or float (float here)
price = float(price) # we reuse price variable
real_double = price*2
print(real_double)
# i can cast immediately by wrapping input
quantity = int(input(f"How many kg of {food} do you want to buy? "))
total = quantity * price
total = round(total, 2) # so we only keep 2 digits after comma
print(f"Neat, you bought {quantity} kg of {food} for €{total}")