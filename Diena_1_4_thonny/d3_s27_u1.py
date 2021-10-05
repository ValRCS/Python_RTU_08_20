# 1.uzd Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"
print("1.uzdevums")
user_temp = float(input("ievadi savu temperatūru: "))
if user_temp < 35:
    print("Vai Tev nav par aukstu?")
# elif user_temp >= 35 and user_temp <= 37:
# elif 35 <= user_temp <= 37:
elif user_temp <= 37: # we know it is at least 35 here
    print("Izskatās, ka Tev viss kārtībā")
elif user_temp <= 39: # we know it is at least 37 here
    print("Drudzis, uzmanies!")
else: # virs 39
    print("Izsauksim ambulanci")