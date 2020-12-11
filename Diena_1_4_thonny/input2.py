myName = input("What is your name?")
print(f"Cool name {myName}")
food = input(f"What is your favorite food {myName}?")
price = input(f"{myName} how much is {food} at your market?")
quantity = input(f"How many kg of {food} do you want to buy?")
# we need to cast this to int or float first!
price = float(price)
quantity = int(quantity) # could use float if we allow partial quantity
total = round(price*quantity,2) # remember about floats
print(f"So, {myName} you will pay {total} Euros for {quantity} kg of {food}")



