# import datetime
# dt = datetime.datetime.today().year
# x=100
# name = input("Ievadiet savu vārdu: ")
# y = float(input(f"Ievadiet savu vecumu, {name}: "))
# i = x-y
# z = x-y+float(dt)
# print("Pēc", f"{i:.0f}", "gadiem Jums būs 100.gadi! \n"
# "Tas būs", f"{z:.0f}.", "gadā")

# pretty much optimal  (without bonus current year)
target_age = 80
name = input("What's your name? ")
years = int(input(f"How old are you {name}? "))
time_left = target_age - years
print(f"O, then you will be {target_age} years old in {time_left} years!")

# mans_vards = "Valdis"
# mans_vards = input("Kā tevi sauc?")
# print(mans_vards)
#  
# # mans_vards2 = "Valdi" # mans vārds jautājuma formai
# # print(f"Cik tev gadu, {mans_vards2}?")
#  
#  
# import datetime
# dt = datetime.datetime.today().year
# mans_vecums = int(input(f"Cik Tev gadi {mans_vards}?"))
# a =100 #gadi, kuri jāsasniedz
# b = a-mans_vecums #cik vēl līdz 100 gadiem
#  
# print(f"You will be {a} years old in {b} years")  