
# start_num = int(input("Insert start number: "))
# end_num = int(input("Insert end number: "))
# cubes = [f"The cube of the given number {num} is {num**3}" for num in range(start_num, end_num+1)]
# print(cubes)

first_num = int(input("Ievadiet sākuma skaitli(veselu skaitli): "))
last_num = int(input("Ievadiet beigu skaitli (veselu skaitli): "))
num_list = list(range(first_num, last_num+1))

cubes = []
for n in num_list:
    cube = n**3
    print(f"{n} kubā: {cube}")
    cubes.append(cube)

print(f"Visi cubi: {cubes}")