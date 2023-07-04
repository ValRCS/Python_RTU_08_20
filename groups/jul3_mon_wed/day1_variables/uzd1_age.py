# 1 Uzdevums
import datetime # usually imports will go up top

name = input("What is your name?")
age = int(input(f"{name} How old are you!"))
# note age does not guarantee precise target
# birthday could be still to come this year..
target_age = 100
current_year = datetime.datetime.now().year

years_to_target = target_age - age

print(f"After {years_to_target} years you will bee {target_age} years old.")
print(f"It will be in {current_year + years_to_target}.")
 