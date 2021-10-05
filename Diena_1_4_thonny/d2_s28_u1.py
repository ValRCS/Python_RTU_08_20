import datetime #call for Date/Time
current_year = datetime.datetime.now().year #get year variable
target_age = 65
my_name=input("Kāds ir Tavs vārds?")
print(f"Mans vārds {my_name}")
 
my_age=input(f"Cik Tev ir gadu{my_name}?")
print(f"Es esmu {my_age} jauns/a.")
 
my_age = int(my_age)
my_century= target_age-my_age
target_year = current_year+my_century
print(f"{my_name} Man būs {target_age} gadi pēc {my_century} gadiem")
print(f"So {my_name} will be {target_age} in {target_year}")