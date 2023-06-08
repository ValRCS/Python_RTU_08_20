import datetime # standard library for Python
target_age = 100 # critical information is saved in one place
# DRY - Do not repeat yourselves
name = input("What is your Name? ")
age = int(input(f"Hi {name}, it is nice to meet you, how old are you? "))
years_to_target = target_age - age
current_year = datetime.datetime.now().year
print(f"""Nice, you'll be {target_age} years old in {years_to_target} years!
That is going to be the year {current_year + years_to_target}.""")
