import datetime
age_to_reach = 100
name = input("Ievadi savu vārdu: ") 
current_age = int(input(name+"Ievadi savu vecumu: "))
after_year = age_to_reach - current_age

current_year = datetime.datetime.now().year
target_year = current_year + (age_to_reach - current_age)
print(f'{name} {target_year} gadā, pēc {after_year} gadiem kļūs {age_to_reach} gadus vecs.')