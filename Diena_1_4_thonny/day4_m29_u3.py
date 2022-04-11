#____N3_____
 
number = int(input("Please, enter number "))
 
search_interval = round(number ** 0.5)
i = 2
 
while i <= search_interval: #We cam accept '1' as exeption, or add additional IF
    if number % i == 0:
        print(f"Not prime {number} divides with {i}")
        break
    else:
        i += 1
else: # this is the strange else attached to while works when no break
    print(f"{number} is prime ")

print("All good")