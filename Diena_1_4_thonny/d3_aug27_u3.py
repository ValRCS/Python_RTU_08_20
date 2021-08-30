# number = int(input ("Ievadiet veselo pozitīvo skaitli."))
number = 59
square_root = number ** 0.5
start = int(square_root)
while (number % start) != 0:
    start -= 1 
if start >= 2:
    print (f"Jusu numurs: {number} nav pirmskaitlis.")
else:
    print(f"Jusu numurs: {number} ir pirmskaitlis.")

# # W = abs(int(input("Vai ievadītais skaitlis ir pirmskaitlis?")))
# W = 100169
# 
# flag = True
#  
# if W > 1:
#     for i in range(2, int(W**0.5)+1):
#         if W%i == 0:
#             print(f"{W} dalās ar {i}, tātad nav pirmskaitlis")
#             flag = False
#             break
#             
# if flag:
#     print("ir pirmskaitlis!")
# else:
#     print("nav pirmskaitlis!")