# infinite loop break and continue
# i = 0
# while True:
#     print(i)
#     if i > 5:
#         break # exits the loop
#     i += 1
# print("At end",i)
i = 0
is_end_of_world = False
MAX_COUNT = 4 # Python does not have real constants but we use capital letters
while i < MAX_COUNT and not is_end_of_world:
    my_input = input("Enter number or q to quit: ")
    if my_input.lower().startswith("q"):
        print("Quitting this loop received input:", my_input)
        break
    num = float(my_input)
    print(num, "cubed is", round(num**3, 2))
    if num**3 > 9000:
        print("Big result!")
        is_end_of_world = True
    i += 1
print("This will will print after break")