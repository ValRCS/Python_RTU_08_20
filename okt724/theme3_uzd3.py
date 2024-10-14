#3.uzdevums
num1 = float(input('Ievadiet pirmo skaitli: '))
num2 = float(input('Ievadiet otro skaitli: '))
num3 = float(input('Ievadiet trešo skaitli: '))

if num1 <= num2 <= num3: # same as num1 <= num2 and num2 <= num3
    print(num1, num2, num3)
elif num1 <= num3 <= num2:
    print(num1, num3, num2)
elif num2 <= num1 <= num3:
    print(num2, num1, num3)
elif num2 <= num3 <= num1:
    print(num2, num3, num1)
elif num3 <= num2 <= num1:
    print(num3, num2, num1)
else: # elif num3 <= num1 <= num2
    print(num3, num1, num2)