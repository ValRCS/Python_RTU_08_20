#2. uzd

while True:
    try: 
        start = int(input("Lūdzu ievadiet sākuma skaitli: "))
        end = int(input("Lūdzu ievadiet beigu skaitli: "))
        break
    except ValueError:
        print("Nepareiza ievade, nepieciešams skaitlis")
        # continue # not needed as we are at the end of the loop


cube_list = []
 
for i in range(start,end+1):
    cube = i**3
    cube_list.append(cube)
    print(f"{i} kubā: {cube}")
print(f"Visi kubi: {cube_list}")