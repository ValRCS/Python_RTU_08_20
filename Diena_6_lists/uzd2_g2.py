# Ievas ideja
sk1 = int(input("Ievadi mazāko skaitli: "))
sk2 = int(input("Ievadi lielāko skaitli: "))
kubi = []
# while sk1 <= sk2:
for n in range(sk1, sk2+1):
    print(f"{n} kubā ir {pow(n, 3)}")
    kubi.append(pow(n, 3))
print("Visi kubi: ", kubi)
