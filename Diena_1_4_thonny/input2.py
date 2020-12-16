my_name = input("What is your name? ")
print(f"Cool name {my_name}")
food = input(f"What is your favorite food {my_name}? ")
price = input(f"{my_name} how much are {food} at your market?")

# we need to cast this to int or float first!
price = float(price)

# we can cast immediately
quantity = int(input(f"How many kg of {food} do you want to buy?"))
# quantity = int(quantity) # could use float if we allow partial quantity

total = round(price*quantity,2) # remember about floats
print(f"So, {my_name} you will pay {total} Euros for {quantity} kg of {food}")



