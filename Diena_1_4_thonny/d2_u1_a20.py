import datetime
current_year = datetime.datetime.now().year
my_name = input("What is your name? ")
my_age = int(input(f"How old are you {my_name}? "))
my_total_age = 100
total = my_total_age-my_age
print(f"So {my_name}, in {total} years you will celebrate 100 years!")
year_100 = current_year+total
print(f"That will be in {year_100}.")

print(f"{my_name}, in {year_100} year You will be 100 years old")

# my_name = input("What is your name? ")
# age = input(f"{my_name}, how old are you? ")
# age_remaining = 100 - int(age)
# print(f"{age}! That's {age_remaining} till 100")
# target_year = age_remaining + current_year

# print("Tev būs 1.uzdevums")
# myName = input("Kā tevi sauc? ")
# print("Sveiks,", myName, "!")
# print(myName, ",")
# years = input("cik tev ir gadu? ")
# print("Vai tā ", str(years), "?")
# cent = 100 - int(years)
# import datetime
# currentYear = datetime.datetime.now().year
# born = currentYear - int(years)
# cent_year = born + 100
# print("Sanāk, ka tu esi dzimis", born, "gadā!")
# print("Tad, mīļais, pēc", cent, "gadiņiem", cent_year, "gadā tev paliks 100 !")
# print("Es ar tādiem večukiem nedraudzējos!")