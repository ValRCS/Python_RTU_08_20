my_name = input("What is your name friend? ")
# input will always return a string after enter even empty
print(my_name)
print(f"That is a nice name {my_name}!")

food = input(f"What is your favorite food {my_name}?")
print(f"Cool I like {food} too!")

price = input(f"{my_name}, how much is {food} at your market?")
double_price = price*2
price = float(price) # so we convert string to float
# not always possible, but we assume our users are following instructions
real_price = price*2
print(f"{price} doubled is {double_price}")
print(f"Sorry, real {price} doubled is {real_price}")

quantity = int(input(f"How many kg of {food} do you want to buy?"))

total = price * quantity
print(f"Total so far is {total}")
total = round(total, 2) # 2 because we want to see cents
print(f"So, {my_name} you will have to pay {total} for {quantity} kg of {food}")

# for this example we assume users input correct type of data


