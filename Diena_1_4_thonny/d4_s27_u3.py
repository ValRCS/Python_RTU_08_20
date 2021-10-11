# entered_number = int(input("Please, enter integer: "))
# if entered_number == 1 or entered_number == 2:
#     print("Your entered number is a prime!") # 1 technically is not a prime
# else:
#     for i in range(2, entered_number):
#         if entered_number % i == 0:
#             print(f"Dividing with {i}")
#             print(f"Your entered number {entered_number} is not a prime number")
#             break
#         elif i == entered_number-1:
#             print("Your entered number is a prime!")        
    
# print("That's it")


# user_input = int(user_input)
user_input = 25
# end_num_to_chek = int(math.sqrt(user_input))
end_num_to_chek = int(user_input**0.5)
 
for i in range(2, end_num_to_chek+1):
    if user_input % i == 0:
        print(f"Skaitlis NAV pirmskaitlis! so {user_input} divides by {i}")
        break
else:
    print("Skaitlis IR pirmskaitlis!")