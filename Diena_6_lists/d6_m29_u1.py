# 1. uzdevums
# numb_list = []
# while True:
#     try:
#         numb = float(input("Input number:"))
#         numb_list.append(numb)
#         avg = sum(numb_list) / len(numb_list)
#         print(f"Average: {avg}")
#         numb_list.sort()
#         print(f"BOTTOM 3: {numb_list[:3]} TOP 3: {numb_list[-3:]}")
#         quit_prog = input("Input q to quit:")
#         if quit_prog == "q": 
#             break
#         else:
#             continue
#     except ValueError:
#         print("That's not a number!")

# Pirmais uzdevums
 
import statistics
my_list = []
while True:
    user_input = input("Enter a number or q to quit: ")
    if user_input.lower().startswith("q"):   
        print("quit")
        break
    try:
        num = float(user_input)
    except ValueError:
        print("ievdijat ne numuru")
        continue # we contine to start of the loop skipping my_list.append(num)
    my_list.append(num)
print(my_list)
print(f"videja vertiba ir {statistics.mean(my_list)}")
my_list.sort()  # IN PLACE
print(my_list)

print(f"3 min vertibas: {my_list[:3]} 3 max vertibas {my_list[-3:]} ")