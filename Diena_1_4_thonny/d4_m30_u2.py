# Ex 2

while True:
    try:
        size = int(input("Ievadiet eglītes augstumu: "))
        break
    except ValueError:
        print("Please enter a whole number")
        
        
space = size-1
stars = 1
for i in range(1, size+1):
    print(" "*space + "*"*stars, end="\n")
    space -= 1
    stars += 2
    
for n in range(size):
    print((" " * (size - n - 1)) + ("*" * (1 + n * 2)))