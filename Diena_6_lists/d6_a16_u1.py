# my_list = []
# counter = 0
# while counter < 5:
#     a = float(input("Insert num "))
#     my_list.append(a)
#     print(my_list)
#     counter += 1
#     print(sum(my_list)/counter)

# 1.b
 
# my_list = []

# while True:
#     number = input("Ievadiet skaitli: ")
#     if number == "q":
#         break
#     else:
#         number = float(number)
#         my_list.append(number)
#         print(round(sum(my_list) / len(my_list),2),my_list)

#1c
num_list = []
while True:
    a = input("Ievadi skaitli:")
    if a == "q":
        break
    else:
        a = float(a)
        num_list.append(a)
        num_list_avg = sum(num_list)/len(num_list)
        print(f"Vidējā skaitļu vērtība ir {round(num_list_avg, 2)}") # vajadētu dabūt nost iekavas
        print(f"Vidējā skaitļu vērtība ir {num_list_avg:.2f}") # vajadētu dabūt nost iekavas
        print(f" MIN(3) = {sorted(num_list)[:3]}, MAX(3) = {sorted(num_list)[-3:]}")