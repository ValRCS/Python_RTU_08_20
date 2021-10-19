# 1.c #
limit = 3
top = limit
bottom = limit
my_list2 = []
while True:
    numbers_input = (input("Ievadiet skaitļus vai spiediet 'q', lai izietu: "))
    if numbers_input == "q":
        break
    numbers = float(numbers_input)
    my_list2.append(numbers)
    my_list2.sort()

    avg_value = round(sum(my_list2)/len(my_list2), 2)
    print(f"Top {limit}:", my_list2[-top:])
    print(f"Bottom {limit}:", my_list2[:bottom])
    print("Vidējā vērība:", avg_value)