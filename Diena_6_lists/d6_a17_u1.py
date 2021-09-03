# # 1.uzdevums "a" variants
my_list = []
quit = "q"
while True:
    num = input("Please enter number, if You want to quit Enter q: ")
    if num == quit:
        break
    else: 
        my_list.append(float(num))
        my_list.sort()
        print(f"Average number is: {round(sum(my_list)/len(my_list), 2)} and all given numbers are: {my_list}")
        print(f"min(3) = {my_list[:3]}, max(3) = {my_list[-3:]}")


# num_list = []
# while True:
#     entry = input("Ievadiet skaitli ")
#     if entry == "q":
#         print("all done exiting")
#         break
#     num = float(entry)
#     num_list.append(num)
#     avg = round((sum(num_list))/(len(num_list)), 4)
#     print(avg)
