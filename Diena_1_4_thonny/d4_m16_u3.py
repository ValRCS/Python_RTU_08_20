# 3.uzdevums
 
number = int(input("Ievadiet veselu pozitīvu skaitli: "))
for a in range(2, int(number**0.5)+1):
    if number % a == 0:
        print(f"Nav pirmskaitlis, jo dalās ar {a}")
        break
else: # this runs if there was no break in for loop
    print("Ir pirmskaitlis!")

