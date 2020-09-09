temp = input(f"Ievadiet temperaturu\n")
temp = float(temp)
if temp < 35:
    print("Nav par aukstu")
elif temp >= 35 and temp <= 37:
    print("viss kartiba")
else:
    print("Iespejams drudzis")
# else:
#     print(f"Ha haa... Sads parametrs {temp} neder")