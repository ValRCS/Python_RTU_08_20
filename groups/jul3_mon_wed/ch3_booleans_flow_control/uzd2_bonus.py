# --- 2. Uzdevums
while True:
    try:
        salary = float(input("Alga?"))       
        y = int(input("Nostradātie pilnie gadi?"))
        break
    except ValueError:
        print("Nepareizi ievadītie dati") 
b = 0.15 # 15%
by = 2 # years to get bonuss
bonuss_value = 0.0
if y > by:
    bonuss_value = salary * b * (y- by)
else:
    print("Sorry no bonuss this year")
print(f"Tavs bonuss ir {bonuss_value:.2f} EUR") 