# We will make an application to calculate food prices
name = input("What is your name? ")
print(f"Nice name {name}! I like it")
food = input(f"What is your favorite food {name}? ")
print(f"Cool I like {food} too!")
price = input(f"How much is 1kg of {food} in your corner store? ")
print(f"Oh {price} for 1kg of {food} that's quite a bit..")
# so we need to convert to numeric data type
# for price float would be okay
price = float(price) # float attempts to convert value to float
# we might want to round price at some point before displaying
double_price = price * 2

print(f"So double price would be {double_price} or would it?")

# maybe we want to allow fractional purchase maybe we do not
# so we could convert to int or float
quantity = int(input(f"Okay, how many kg of {food} do you want to buy? "))
# i could have used quantity = int(quantity)
total = price * quantity
# https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
print(f"{name} you would pay {total:.2f} for {quantity} kg of {food}.")
# at this point I still have total with possibly multiple digits after comma
# i could also round up total
total = round(total, 2)
print(f"{name} you would pay {total} for {quantity} kg of {food}.")
