# myFood = "potatoes"
myFood = input("What is your favorite food?") #input prasa ievadīt tekstu(str)
# price = 0.45
price = input(f"How much does {myFood} cost in your shop?")
price = float(price) # we need to clean up price since it was a string from input
# quantity = 10
quantity = input(f"How many {myFood} do you want to buy?")
quantity = int(quantity)
total = round(price * quantity, 2) # so we guarantee only 2 places after comma
print(f"It will cost {total} Euros to buy {quantity} kg of {myFood}")