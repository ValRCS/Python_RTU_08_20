# ################ task 1a ########################
# total = 0
# num_count = 0
# while True:
#     input_val = input("Input the digit:")
#     if input_val == 'q': #could check for str and if str [0] == 'q'
#         break
#     input_val = float(input_val)
#     num_count += 1
#     total += input_val
#     average_num = total/num_count
#     print(f"average number is {average_num}")

# uzdevums 1c
number_list = []
while True:
    inp_num = input('Please enter a decimal number or "q" if you want to quit the program: ')
    if inp_num == "q":
        break
    inp_num = float(inp_num)
    number_list.append(inp_num)
    average = sum(number_list)/len(number_list)
    print(f"This far you have entered numbers: {number_list}")
    print(f"The average of entered numbers is: {average}")
    sorted_number_list = sorted(number_list)
    bot3 = sorted_number_list[:3]
    top3 = sorted_number_list[-3:][::-1]
    print(f"BOTTOM3 {bot3} TOP3 {top3}")

    


# my_list = []
# while type(my_list) != float:
#     # if my_list != "q":   
#         my_list = [float(item) for item in input("Enter the list items : ").split()]
#         print(f"Your array: {my_list}")
#         average = sum(my_list) / len(my_list)
#         print(f"Average amount is: {average}")
#         pop3 = sorted(my_list)[-3:]
#         print(f"POP3 in our array: {pop3}")
#         bottom3 = sorted(my_list)[0:3]
#         print(f"BOTTOM3 in our array: {bottom3}")  