#3.Uzdevums
my_name = "Valdis"
celsius = input(f"And the last question - how many degrees Celsius is in this room, {my_name}? ")
celsius = float(celsius)
farenheit = 32+celsius*9/5 #<<<<Houston we have a problem
farenheit = round(farenheit, 2)
print(f"Great, thank you for cooperation. So in farenheit it is {farenheit}.")





#  farenheit = 32+celsium*(9/5)
#  
# cels = float(input("Norādiet Celsija vienības: "))
# farenheit = 32+cels*(9/5)
# farenheit = round(farenheit, 2)
# print(f"Farenheitu vienības: {farenheit}")