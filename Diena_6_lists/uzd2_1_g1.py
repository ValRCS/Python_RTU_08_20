cube = [] # could use list()
a = int(input("Ievadi sākuma skaitli:"))
b = int(input("Ievadi beigu skaitli:"))
for i in range(a, b+1):
    c = i ** 3
    cube.append(c)
    print(f"{i} kubā ir {c}")
print(f"Visi kubi: {cube}")