# 1. uzdevums
target_age = 65
my_name = input("Sveiks! Kâ Tevi sauc? ")
print(f"{my_name}? Mani arî sauc {my_name}. Prieks iepazîties.")
age = int(input(f"{my_name} cik Tev tagad ir gadu? "))
years_till_target = target_age - age
import datetime
current_year = datetime.datetime.now().year
total = years_till_target + current_year
print(f"Tâtad sanâk, ka tev bûs {target_age} gadu {years_till_target} pec gadiem un tad you bûs {total}. gads.")