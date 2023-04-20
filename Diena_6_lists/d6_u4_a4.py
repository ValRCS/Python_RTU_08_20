# 4. pirmskaitļi
 
while True:
    user_inp = input("Cik pirmskaitļi vajadzīgi? ")
    
    try:
        length = int(user_inp)
        if length < 0:
            print("Lūdzu, ievadiet pozitīvu veselu skaitli.")
            continue
        break
    except ValueError:
        print("Lūdzu, ievadiet veselu pozitīvu skaitli.")
        # continue # not needed since we are at the end of the loop
 
prime_list = []
number = 1
 
while len(prime_list) < length:
    number += 1
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            break
    else:
        prime_list.append(number)
 
print(f"Pirmie {length} pirmskaitļi: {prime_list}")