my_list = []
a = int(input("Ievadi sākuma skaitli: "))
b = int(input("Ievadi beigu skaitli: "))
for i in range(a,b+1):
    print(f"{i} kubā: {i**3}")
    my_list.append(i**3)
print(f"Visi kubi: {my_list}")

cube_list = [[n, n**3, f"{n} kubā: {n**3}"] for n in range(a,b+1)]
print(cube_list)