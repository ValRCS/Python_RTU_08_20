pirmaisSk = int(input("Ievadiet sākotnējo skaitli: "))
otraisSk = int(input("Ievadiet noslēdzošo skaitli: "))
kubi = []

for i in range(pirmaisSk, otraisSk+1):
    print("{} kubā: {}".format(i, i**3))
    kubi.append(i**3)
print('Visi kubi:', kubi)
print(kubi[1:4])
