# # myFood = "potatoes"
my_food = input("What is your favorite food?") #input prasa ievadīt tekstu(str)
# # price = 0.45
# we can use f-strings f"   text {my_var} more text" to format text
price = input(f"How much does {my_food} cost in your shop?")
double_price = price * 2 # will this work correctly?
print(f"Ahh {my_food} double priced would be {double_price}")
price = float(price) # we need to clean up price since it was a string from input
double_price_again = price * 2 
print(f"Ahh {my_food} double priced would be {double_price_again}")

# # quantity = 10
# i can cast immediately as well
quantity = int(input(f"How many kg of  {my_food} do you want to buy?"))
# quantity = int(quantity)
# total = price * quantity  # do not use sum as a variable name it is a function in Python
total = round(price * quantity, 2) # so we guarantee only 2 places after comma

print(f"It will cost {total} Euros to buy {quantity} kg of {my_food}")