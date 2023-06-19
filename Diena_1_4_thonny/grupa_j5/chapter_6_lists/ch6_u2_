# todo add some error checking 
print("aprēķīnāsim skaitļu  cubus ³ ")

while True:
    try:
        a = int(input("ievadiet sākuma skaitli: "))
        b = int(input("ievadiet beigu skaitli: "))
        # notice we handle input here for both a and b
        break
    except ValueError:
        print("ievadiet veselu skaitli")

# we know we have a and b as integers here
# let's check if a is smaller than b
if a > b:
    step = -1
else: # includes a == b and a < b
    step = 1

numbers = list(range(a,b+step, step))
cube_list = []
# i could have used range(a,b+step, step) directly in for loop
# but i wanted to show how to create a list from range
for n in numbers:
    kubs = n**3
    print(f"{n} kubā ir: {kubs}")
    cube_list.append(kubs)
print(f"Visi kubi: {cube_list}")