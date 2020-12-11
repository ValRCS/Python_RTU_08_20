# First task
# my_name = input("What is your name?")
# age = int(float((input(f"How old are you, {my_name}?"))))
# y = 100
# print(f"You will turn 100 after {y - age} years!")

# 1 uzd
import datetime
TARGET_AGE = 75
curr_year = datetime.datetime.now().year
name = input(f"What is your name? ")
age = input(f"What is your age, {name}? ")
age = int(age)
reach_target = TARGET_AGE - age
year_target = curr_year + reach_target
print(f"{name}, you will be at the age of {TARGET_AGE} after {reach_target} years at year {year_target}!!!")