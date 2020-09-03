# Arna variants
my_list = []
while True:
    my_input = input("ievadiet skaitli vai Q lai beigtu: ")
    if my_input == "q" or my_input == "Q":
        break
    my_input = float(my_input)
    my_list.append(my_input)
    # create a new list with sorted values
    my_list_sorted = sorted(my_list, reverse=True)
    print(
        f"3 lielākās un 3 mazākās vērtības no {len(my_list)} ievadītajām:\n{my_list_sorted[:3]} ... {my_list_sorted[-3:]}")
    print(
        f"ievadītās vērtības to ievadīšanas secībā:\n{my_list}\nto vidējā vērtība: {sum(my_list)/len(my_list)}")
