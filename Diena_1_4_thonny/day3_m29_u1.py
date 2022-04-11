# task No1
temp = float(input("What is your body temperature? " ))
if temp < 35:
    print("Do you have cold? ")
    print(f"Jūsu temperatūra ir {temp} °C, Vai nav par aukstu?")
elif 35 <= temp <= 37:  # same as 35 <= temp and temp <= 37
    print("All good ")
    print("Jūsu temperatūra ir normas robežās °C, Viss ir kārtībā!")
else:
    print("Probably you have fever ")
    print("Jūsu temperatūra pārsniedz 37 °C, Iespējams Jums ir drudzis!")