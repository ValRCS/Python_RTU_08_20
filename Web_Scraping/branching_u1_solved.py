#pirmais
name = input("Lūdzu ievadi savu vārdu:\n").title()
while True:
    try:
        text = input(f"{name}, ievadiet pašreizējo temperatūru:\n")
        text = text.replace(",", ".") # to accoount for those using , instead of .
        temperature = float(text) # this will raise ValueError if not a float number
        break
    except ValueError:
        print("Ievadītā vērtība nav skaitlis. Lūdzu, ievadiet skaitli.")

if temperature < 35:
    print("Vai nav par aukstu?")
# elif 35 <= temperature <= 37: # alternative would be 35 <= temperature and temperature <= 37
elif temperature <= 37: # this already includes 35 <= temperature
    print("Viss kārtibā!")
    print(f"Jūs esat vesels! Temperatūra ir {temperature} grādi.")
else:
    print("Iespējams drudzis.")