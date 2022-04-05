# 1
import datetime
current_year = datetime.datetime.now().year
target_age = 100
my_name = input("What is your name? ")
your_age = input("Whats is your age? ")
your_age = int(your_age)
age_after = target_age - your_age
target_year = current_year + age_after
print(f"You will be {target_age} age old after {age_after} years in {target_year}")