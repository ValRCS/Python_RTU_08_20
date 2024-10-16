# 3.uzdevums
while True:
    print("Please enter a valid integer number or press Enter or type Q to quit: ")
    num = input("-> ")
    if num =="" or num == "Q":
        print("OK you want to quit alright")
        break
    try:
        num = int(num)
        if num <= 0:
            print("Sorry you did not enter a valid number")
        else:
            print("Cool you entered an integer!", num)
            is_prime = True # hipotēze visi skaitļi ir pirmskaitļi
            
            for n in range(2, int(num**0.5)+1):
                if num % n == 0:
                    is_prime = False
#                     print(f"{num} is not prime it divides by {n}")
                    break # we break from inner for loop
            if is_prime: # ja ir tikai viens dalītājs, tad skaitlis ir pirmskaitlis
                print(f'Yes {num} is prime')
            else:
                print(f'No {num} is not prime it divides by {n}')
            break # we break out of outer loop
    except ValueError:
        print("Sorry you did not enter a valid number")
print("This is the end")