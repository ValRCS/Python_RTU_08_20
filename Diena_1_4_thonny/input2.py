my_name = input("What is your name? ")
# my_name = my_name.title()
# # whatever we write before pressing enter will be saved as string
# # and my_name will have reference to our text
print(f"Cool name {my_name}") # formatted string
print("Cool name " + my_name + " indeed") # not that fun
print("Cool name", my_name, "something") # one white space is default for each comma
food = input(f"What is your favorite food {my_name}? ")
price = input(f"{my_name} how much are {food} at your market?")
double_price = price*2 # what do you think will happen here?
print(f"{price} doubled is {double_price}")

# # # # 
# # # # # we need to cast this to int or float first!
price = float(price) # so data type here changes from str to float
real_double = price*2
print(f"Oops {price} doubled is {real_double}")
# # # # 
# # # # # we can cast immediately
quantity = int(input(f"How many kg of {food} do you want to buy?"))
# # # # # quantity = int(quantity) # could use float if we allow partial quantity
# # # #
total = price*quantity
print(f"Total so far is {total}")
total = round(price*quantity, 2) # remember about floats so only 2 digits for float 
print(f"So, {my_name} you will pay {total} Euros for {quantity} kg of {food}")
# # # # notice that with f-strings I do not convert to str all my numbers
# # # # 
# # # # 
# # # # 