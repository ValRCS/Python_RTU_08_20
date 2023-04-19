#trešais
number1 = int(input("Lūdzu ierakstiet pirmo skaitli: "))
number2 = int(input("Lūdzu ierakstiet otro skaitli: "))
number3 = int(input("Lūdzu ierakstiet trešo skaitli: "))
 
if number1<=number2<=number3:
    print(f"{number1}, {number2}, {number3}")
elif number1<=number3<=number2:
    print(f"{number1}, {number3}, {number2}")
elif number2<=number1<=number3:
    print(f"{number2}, {number1}, {number3}")
elif number2<=number3<=number1:
    print(f"{number2}, {number3}, {number1}")
elif number3<=number1<=number2:
    print(f"{number3}, {number1}, {number2}")
else:
    print(f"{number3}, {number2}, {number1}")

# in real life we would put numbers in a list and sort them
# big advantage of lists is that they can be very large and still be sorted