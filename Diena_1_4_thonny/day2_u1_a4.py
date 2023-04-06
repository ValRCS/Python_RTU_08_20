import datetime
# Uzdevums 1
target_age = 40
name = input("Kā Jūs sauc?")
vecums = int(input(f"Sveiks {name}. Cik Jums ir gadi?"))
daudz_gadi = target_age - vecums
if vecums > target_age:
    print(f"Jums jau ir pāri {target_age} atpūšaties!")
else:
    print(f"Lieliski, Jums pēc {daudz_gadi} gadi būs {target_age} gadi.")
    current_year = datetime.datetime.now().year  
    year_target_reached = current_year + daudz_gadi
    print(f"Tas būs {year_target_reached} gadā!")
