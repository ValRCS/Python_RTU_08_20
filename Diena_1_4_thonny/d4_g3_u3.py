num = int(input("Ievadiet pozitīvu skaitli: "))
if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(num, "- nav pirmskaitlis")
            print("jo dalās ar", i)
            break
    else:
        print(num, "- ir pirmskaitlis")
else:
    print(num, "- nav pirmskaitlis")