# 6. nodarbība 4. uzdevums "Pirmskaitļi"
 
def prime_list(lenght):
    prime_list = []
    counter = 2
    while len(prime_list) < lenght:
        prime = True
        for i in range(2, counter):
            if counter % i == 0:
                prime = False
                counter += 1
                break
        if prime:
            prime_list.append(counter)
            counter += 1  
    return prime_list
 
list_lenght = int(input('Enter list lenght: '))
 
print(f'here is first {list_lenght} prime numbers {prime_list(list_lenght)}')