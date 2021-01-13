x=int(input("Ievadiet saraksta sākuma skaitli  "))
y=int(input("Ievadiet saraksta beigu skaitli  " ))
cubes=[num**3 for num in range(x, y+1)] # izdrukai sarakstā tiek iekļautas vērtības, kuras ir kāpinātas kubā
pretty_cubes = [f"{n} kubā: {n**3}" for n in range(x, y+1)]
print(pretty_cubes)
print(*pretty_cubes, sep="\n") # i can unroll the list into values useful for functions
print("Saraksta skaitļu vērtības kubā:")
print(cubes) #tiek izdrukātas saraksta skaitļu vērtības, kāpinātas kubā