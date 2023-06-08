import datetime # par importiem runāsim atsevišķi
current_year = datetime.datetime.now().year
name = input("Ievadiet Lietotāja vārdu!")
print(f"Lietotaja vārds {name} - saglabāts!")
age = int(input("Lai noskaidrotu cik gadi jums {name}, ir atlicis līdz pensijai, Ievadiet savu vecumu!"))
pension = 100 # good idea to keep magic numbers in variables
time_left = pension - age
print(f"""Cienītais {name},
Jums Līdz pensijai {pension} gados
atlikuši {time_left} gadi!""")
pension_year = current_year + time_left
print(f"You will have pension in year {pension_year}")