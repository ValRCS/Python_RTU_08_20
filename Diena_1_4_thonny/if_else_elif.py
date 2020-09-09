# if
a = 0
b = 5
c = 10
if a > b:
    print("a > b")
    print("Also do this")
    print(a*b)
# a <= b:
else: # if a <= b:
    print(a,b)
    print("a is less or equal than b")
    
if a != 0:
    print("Cool a nonzero a")
    print(b / a)

b += 6
b -= 1

if b > c:
    print("b is larger than c", b, c)
elif b < c:
    print("b is smaller than c", b, c)
else:
    print("b is equal to c", b, c)
    
answer = input("Enter your code")
if answer == "a":
    print("alpha")
elif answer == "b":
    print("beta")
elif answer == "c":
    print("gamma")
else:
    print("you entered unclear", answer)
    
print("This will run on matter what")
a = 7
is_odd_digit = a in range(1,10,2) # 1, 3, 5,7,9