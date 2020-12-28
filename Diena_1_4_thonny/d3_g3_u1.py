# manaTemperatura=float(input("Norādiet savu temperatūru Celsija grādos "))
# if manaTemperatura<36:
#     print("Vai nav par aukstu?")
# elif manaTemperatura>=36 and manaTemperatura<=37:
#     print("Viss kārtībā.")
# elif manaTemperatura>37 and manaTemperatura<=39:
#     print("Paliela temperatūra.")
# else:
#     print("Iespējams, drudzis.")
#

# t = float(input("Lūdzu, ievadiet temperatūru: "))
# if t < 35:
#     print("Jums nav par aukstu?") # Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# if t > 37:
#     print("Jums iespējams drudzis!") # Ja ir pāri 37, tad izvadiet "iespējams drudzis"
# if t >= 35 and t <= 37:
#     print ("Jums viss ir kārtībā!") # Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"

t = float(input("kāda ir Jūsu temperatūŗa? "))
if t < 35:
    print("nav par aukstu")
elif t >= 35 and t <= 37:
    print ("Viss kārtībā")
else:
    print ("Iespējams drudzis")