is_prime = True
num = int(input("Ievadiet skaitli: "))
for n in range(2, int(num**0.5) + 1):
    if num%n == 0:
        is_prime = False
        break
if is_prime:
    print(f"Skaitlis {num} ir pirmskaitlis")
else:
    print(f"Skaitlis {num} nav pirmskaitlis")

# # 3.Pirmskaitlis
# #import math
#  
# while True:
#     user_input = input('Ievadi naturālu skaitli. Ja vēlies iziet, spied q: ')
#  
#     if user_input == 'q':
#         break
#  
#     try:
#         input_int = int(user_input)
#  
#         if input_int <= 0:
#             print(f'Ievadītā vērtība ({user_input}) nav naturāls skaitlis')
#             continue
#  
#         #j = 0
#         if input_int == 1:
#             print(f'Ievadītais skaitlis ({input_int}) ir pirmskaitlis')
#         else:
#             for i in range(2, input_int + 1):
#                 if input_int % i == 0 and input_int != i:
#                     print(f'Ievadītais skaitlis ({input_int}) nav pirmskaitlis. '
#                           f'Jo {i} ir mazākais dalāmais ar kuru atlikums ir 0.')
#                     break
#                 elif input_int == i:
#                     print(f'Ievadītais skaitlis ({input_int}) ir pirmskaitlis')
#     except ValueError:
#         print(f'Ievadītā vērtība ({user_input}) nav naturāls skaitlis')
#         continue