#1. uzdevums
TARGET_AGE = 100
import datetime
# current_year = 2024
current_year = datetime.datetime.now().year # so it works next year as well

name = input("What is your name?")
print(f"Nice to meet you, {name}! I'm Johnny!")
age = input(f"If I may ask, {name}, how old are you?")
age_int = int(age)
target_age_reached = current_year - age_int + TARGET_AGE
print(f"{name}, now you are {age}, but you will be {TARGET_AGE} years old in {target_age_reached}")
 