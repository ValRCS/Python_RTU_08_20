# --- 1.2 Uzdevums ---
#----------------------
# sakums = int(input("Ievadiet sākuma skaitli: "))
# beigas = int(input("Ievadiet beigu skaitli: "))
 
# print("Ievadītie skaitļi un to kubi:")
 
# skaitlu_saraksts = []
 
# for skaitlis in range(sakums, beigas + 1):
#     kubs = skaitlis ** 3
#     print(skaitlis, kubs)
#     skaitlu_saraksts.append(kubs)
 
# print("Visu ievadīto skaitļu kubi:", skaitlu_saraksts)

# lets make function that returns sakums and beigas
def get_range():
    # let's use try/except to catch ValueError
    while True:
        try:
            sakums = int(input("Ievadiet sākuma skaitli: "))
            beigas = int(input("Ievadiet beigu skaitli: "))
            return sakums, beigas
        except ValueError:
            print('Ievadītajai vērtībai ir jābūt veselam skaitlim')

# now let's make a function to get cubes in range
def get_cubes(sakums:int, beigas:int) -> list: # TODO talk about type hints (PEP 484
    """Returns list of cubes in range sakums, beigas (inclusive)
    Args:
        sakums (int): start of range
        beigas (int): end of range
    Returns:
        list: list of lists with numbers and cubes
    """
    return [[skaitlis, skaitlis ** 3] for skaitlis in range(sakums, beigas + 1)]

# finally let's make a function to print cube list
def print_cubes(cubes):
    # print numbers and cubes
    for skaitlis, kubs in cubes: # we use unpacking here to get skaitlis and kubs
        print(skaitlis, kubs)
    # print only cubes
    just_cubes = [el[1] for el in cubes] # we get a new list of 2nd elements
    # print("Visu ievadīto skaitļu kubi:", cubes)
    print("Visu ievadīto skaitļu kubi:", just_cubes)

# now let's put it all together
def main():
    sakums, beigas = get_range()
    cubes = get_cubes(sakums, beigas)
    print_cubes(cubes)

# call it
main() # TODO talk about main guard and __name__ == '__main__'

    