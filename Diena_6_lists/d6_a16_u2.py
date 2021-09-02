cubes = []
sakuma_skaitlis=int(input("Ievadiet sakuma skaitli:"))
beigu_skaitlis=int(input("Ievadiet beigu skaitli:"))
for n in range(sakuma_skaitlis,beigu_skaitlis+1):  # could also use range(10)
    cube = n**3
    print(f"{n} kubā : {cube}")
    cubes.append(cube)
print(cubes)
# not recommened but we can put print inside our list comprehension (since it gives None)
# cubes_also = [print(f"{n} kubā : {n**3}") or n**3 for n in range(sakuma_skaitlis,beigu_skaitlis+1)]
# better just create cubes with no side effects
cubes_also = [n**3 for n in range(sakuma_skaitlis,beigu_skaitlis+1)]