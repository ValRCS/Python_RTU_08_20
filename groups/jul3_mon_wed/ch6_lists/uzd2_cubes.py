# Otrais 

def get_cubes(a,b):
    # we could add some validation here
    # for example we could check if a and b are integers
    # also we could add negative step when a > b
    # alternatively we could swap a and b
    if isinstance(a, int) and isinstance(b, int):
        return [n**3 for n in range(a,b)]
    else:
        return [] # i prefer empty list over None
 
def print_cubes(a,b):
    cubed_numbers = get_cubes(a,b)
    print(f'Visi kubi: {cubed_numbers}')
    # if I had get_cubes then I would want to return cubed_numbers
 
first_number = int(input("Ievadiet pirmo skaitli: "))
last_number = int(input("Ievadiet pēdējo skaitli: "))
 
print_cubes(first_number,last_number)