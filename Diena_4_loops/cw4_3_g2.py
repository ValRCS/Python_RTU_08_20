while True:
    try:
        number = int(input("Insert a number: "))
        if number < 0:
            raise ValueError
        break
    except ValueError:
        print("Not an integer!!!")
 
sqrt_val = round(int(number**0.5))+1
is_prime = True

for n in range(2, sqrt_val):
    if number % n == 0:
        print(f"Oh oh! {number} divides with {n} without reminder! Not a prime")
        is_prime = False
        break;

if is_prime:
    print(f"Skaitlis {number} ir pirmskaitlis!")
else:  
    print(f"Skaitlis {number} nav pirmskaitlis!")
    
    
    
# i = input("Ievadiet skaitli ")
# i=int(i)
# n=i
# j=0
# while n>0:
#     if i % n == 0:
#         j+=1
#     n-=1
# if j<=2:
#     print(f"Skatlis {i} ir pirmskaitlis")
# else:
#     print(f"Skatlis {i} nav pirmskaitlis")