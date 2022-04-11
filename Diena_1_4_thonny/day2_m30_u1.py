import datetime
target_age = 100
current_year = datetime.datetime.now().year
my_name = input("What is your name friend? ")
my_age = int(input(f"How old are you, {my_name}? "))
years_to_reach = target_age-my_age
target_year = current_year+years_to_reach
print(f"Nice, you'll be {target_age} years old in {target_year} which will be {years_to_reach} years from now!") 