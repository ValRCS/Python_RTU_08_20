# # 1 uzdevums
name = input("Enter your name: ")
age = int(input(name + ", how old are you?"))
import datetime
currentYear = datetime.datetime.now().year
print("You will be 100 in", 100-age, "years and that will be year", currentYear+(100-age))


# name = input("What is your name?")
# age = input (f"What is your age {name}?")
# age_till_100 = 100 - int(age)
#  
# import datetime
# current_year = datetime.datetime.now().year
# # current_year = 2020
#  
# year_with_100 = current_year + age_till_100
# print(f"{name}, after {age_till_100} years in {year_with_100} you will be 100 years old!")