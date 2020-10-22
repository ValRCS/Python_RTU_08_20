my_list = []
while True:
    my_input = input("ievadiet skaitli vai Q lai beigtu: ")
    if my_input.lower().startswith('q'):
        break
    my_input = float(my_input)
    my_list.append(my_input)
 
my_list_sorted = sorted(my_list, reverse=True)
print(f"3 lielākās un 3 mazākās vērtības no {len(my_list)} ievadītajām:\n{my_list_sorted[:3]} ... {my_list_sorted[-3:]}")
print(f"ievadītās vērtības to ievadīšanas secībā:\n{my_list}\nto vidējā vērtība: {sum(my_list)/len(my_list)}")  


# my_list = []
# while True:
#     my_number = (input("PRESS b to quite!  Enter the number : "))
#     if my_number == "b":
#         print("Game over")
#         break
#     else:
#         if my_number.isdigit():
#             my_list += [float(my_number)]
#             print(f"Your list: {my_list}")
#             print(f"Sum = : {sum(my_list)}")
#             print(f"Avarage = {sum(my_list)/len(my_list)}")
#             my_list_2 = sorted(my_list,reverse=True)
#             print(f"Your Bottom 3 list: {my_list_2[-3:]} Your Top 2 list {my_list_2[:3]}")
 
#         else:
#             my_number = input("Enter the number : ")


# # from typing import Reversible


# # count = 0
# # totalSum = 0
# # allNumbers = []
# # while True:
# #     number = input("ievadiet skaitli")
# #     if number.isnumeric():
# #         number = float(number)
# #         count += 1
# #         totalSum += number
# #         average = (totalSum) / count
# #         allNumbers.append(number)
# #         allNumbers.sort(reverse=True)
# #         top3list = allNumbers[:3]
# #         bottom3list = allNumbers[-3:]
# #         print(f"ievadīto skaitļu vidējā vērtība ir {average}, visi ievadītie skaitļi ir: {allNumbers}, TOP3 ir: {top3list}, BOTTOM3 ir: {bottom3list}")
# #     if str(number) == "q":
# #         print("Paldies par piedalīšanos :)")
# #         break