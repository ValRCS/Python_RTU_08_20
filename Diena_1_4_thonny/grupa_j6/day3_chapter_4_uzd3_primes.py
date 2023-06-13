# skaitlis=None
# while skaitlis is None:
#     try:
#         skaitlis = int(input(f"Lūdzu ievadi veselu , pozitīvu skaitli! "))
#         if skaitlis <= 0:
#             skaitlis = None
#             raise ValueError
#     except ValueError:
#         pass # pass is empty instruction used where syntax demands to do something
#  
# pirmskaitlis = True;
# for dal in range(2,skaitlis): # potential improvement here
#     if skaitlis % dal == 0:
#         print(f"{skaitlis} dalās ar {dal} bez atlikuma!")
#         pirmskaitlis = False
#         break
#  
# if pirmskaitlis:
#     print(f"{skaitlis} ir pirmskaitlis")
# else: 
#     print(f"{skaitlis} nav pirmskaitlis")

number_to_check = int(input("Enter positive integer "))

for i in range(2, int(number_to_check ** 0.5) + 1):
    if number_to_check % i == 0:
        print(f"{number_to_check} is not a prime number!")
        print(f"{number_to_check} divides by {i} with no reminder")
        break
else: # so we finished the loop with no break
    print(f"{number_to_check} is a prime number!")

