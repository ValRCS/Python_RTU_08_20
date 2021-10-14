my_list = []
while True:
    user_number = input("Ievadiet skaitļus vai q lai beigtu spēli")
    if user_number == "q":
        print("The End")
        break
    else:
        entered_number = float(user_number)
        my_list.append(entered_number)
        my_average =  sum(my_list) / len(my_list)
        my_average = round(my_average, 2)
        print("average of your list is", my_average)
        print("my list is", my_list)
        sort_list = sorted(my_list, reverse=True) # alternative would be my_list.sort()
        print(f"Ievadītie skaitļi: Top3 {sort_list[:3]}, Bottom3 {sort_list[-3:]}")