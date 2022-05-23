import datetime # par importiem runāsim atsevišķi
TARGET_YEAR = 50 # i could also use input for this
my_name = input("What is your name? ")
age = input("What is your age? ")
delta = TARGET_YEAR-float(age)

current_year = datetime.datetime.now().year
print(f"Jums būs {TARGET_YEAR}. dzimšanas diena {round(current_year+delta)}. gadā")