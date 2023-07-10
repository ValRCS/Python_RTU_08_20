height = 0
 
while height <= 0:
    try:
        height = int(input("Lūdzu ievadiet eglītes augstumu: "))
        if height <= 0:
            print("Vajag vismaz 1!")
    except ValueError:
        print("Tas nav skaitlis!")
 
for i in range(height):
    # spaces = height - i - 1
    # stars = "*" * (2 * i + 1)
    # row = " " * spaces + "*" * stars
    row = " " * (height - i - 1) + "*" * (2 * i + 1)
    print(row)