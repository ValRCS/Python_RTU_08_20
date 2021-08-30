# 1.uzd.
import datetime
current_year = datetime.datetime.now().year
my_name = input("What is your name?")
my_name = my_name.capitalize() # make name start with uppercase letter
age = int(input(f"How old are you,{my_name}?"))
hundred = 100
until_hundred = hundred - age
year = current_year + until_hundred
print(f"You will be 100 years old in {until_hundred} years, and it will be in {year}!")