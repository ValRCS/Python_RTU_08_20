# # infinite loop break and continue
# i=0
# while True:
#     print(f"Running forever or so it seems, i == {i}")
#     if i > 5:
#         print(f"nope, i've got to quit because i == {i}")
#         break # we exit loop and go to the line after loop
#     i+=1
# print("This runs after our break")

# # 
i = 0
is_end_of_world = False
# we have 3 exit conditions
while i < 4 and not is_end_of_world:
    my_input = input("Enter number or q to quit: ")
    if my_input == "q":
        print("I've got to break out!")
        break # with break we exit our loop
    num = float(my_input)
    result = num**3
    print(num, "cubed is", round(result, 2))
    if result > 9000:
        print("Big result!", result)
        is_end_of_world = True
    i += 1
print("This will will print after break")
