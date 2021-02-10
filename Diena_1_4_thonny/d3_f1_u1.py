temperature = float(input("What is your body temperature? "))
if temperature < 35:
    print("nav par aukstu")
elif temperature > 37:
    print("iespējams drudzis")
else:
    print("viss kārtībā")


# temperatura = float(input("Lūdzu, ievadiet savu ķermeņa temperatūru: "))
# a = "Vai Jums nav par aukstu?"
# b = "Viss kārtībā!"
# c = "Jums iespējams drudzis!"
# if temperatura <= 35:
#     print(a)
# elif temperatura >=35.1 and temperatura <= 36.9:
#     print(b)
# elif temperatura >=37:
#     print(c)
# else:
#     print("Hmm alien temperature", temperatura)