num = int(input("Your number:"))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(f"Your number {num} is not a prime number it divides by {i}")
           break
   else:
       print("Your number is a prime number")
else:
    print("Your number is not a prime number")


# skaitlis = int(input("Ievadi skaitli"))
# i = (skaitlis - 1)
# h = 0
# while h <= 1:
#     
#     if h > 0 :
#         print(f"{skaitlis} nav pirmskaitlis {i}")
#     else:
#         print(f"{skaitlis} ir pirmskaitlis {i}")
#     h += skaitlis % i



# n = int(input("Ievadiet naturālu skaitli: "))
# sqrt_n = int(n**0.5+1)
#print(sqrt_n)
# ir_pirmskaitlis = True
# if n % 2 == 0:
#     ir_pirmskaitlis = False
# else:
#     for i in range(3, sqrt_n, 2):
#         if n % i == 0:
#             ir_pirmskaitlis = False
#             print(f"{n} divides by {i}, so it is NOT prime!")
#             break
#  
# if n == 1:
#     ir_pirmskaitlis = False
#     
# if n == 2 or n == 3:
#     ir_pirmskaitlis = True
#     
# if ir_pirmskaitlis:
#     print(f"{n} ir pirmskaitlis")
# else:
#     print(f"{n} nav pirmskaitlis")