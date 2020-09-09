num1 = input(f"Ievadiet skaitli nr.1\n")
num2 = input(f"Ievadiet skaitli nr.2\n")
num3 = input(f"Ievadiet skaitli nr.3\n")
 
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
 
 
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Sada kombinacija nav iespejama.")
    # labāk print (num1,num2,num3)
 
elif num1 < num2:
    if num2 < num3:
        print(f"Nr.1 = {num1}, Nr.2 = {num2}, Nr.3 = {num3}")
    else:
        if num1 > num3:
            print(f"Nr.3 = {num3}, Nr.1 = {num1}, Nr.2 = {num2}")
        else:
            print(f"Nr.1 = {num1}, Nr.3 = {num3}, Nr.2 = {num2}")
 
else:
    if num3 > num1:
        print(f"Nr.2 = {num2}, Nr.1 = {num1}, Nr.3 = {num3}")
    else:
        if num3 > num2:
            print(f"Nr.2 = {num2}, Nr.3 = {num3}, Nr.1 = {num1}")
        else:
            print(f"Nr.3 = {num3}, Nr.2 = {num2}, Nr.1 = {num1}")