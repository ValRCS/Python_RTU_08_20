a = int(input("ievadiet veselu, pozitīvu skaitli skaitli: "))
x = 2
is_prime = True
for x in range (2, int(a**0.5)+1): #nedalīsim ar pašu ciparu
    if a%x==0:
        print(f"{a} nav pirmskaitlis jo dalās ar {x}")
        is_prime = False
        break
#     if x==a-1:
#         print(f"{a} ir pirmskaitlis")
if is_prime:
    print(f"{a} ir pirmskaitlis")