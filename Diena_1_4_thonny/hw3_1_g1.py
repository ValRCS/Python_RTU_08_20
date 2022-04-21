t = float(input("Ievadiet temperaturu "))
if round(t,2)<35:
    print("Nav par aukstu?")
elif round(t,2)>37:
    print("Iespējams drudzis!")
else:
    print("Viss kārtībā :)")


# import sys
# 
# try:
#     temperature: float = float(input("Kāda ir Tava temperatūra? "))
# except ValueError as e:
#     print("Lūdzu ievadi skaitlisku vērtību!")
#     sys.exit(1) # we exit early
# 
# # temperature = float(input("Ievadiet savu temperatūru:"))
# if temperature < 35:
#     print("Vai nav par aukstu?")
# elif temperature >= 35 and temperature <= 37:
#     print("Viss kārtībā!")
# else:
#     print ("Iespējams drudzis!")