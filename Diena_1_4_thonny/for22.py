for n in range(7):
    print(n)
for _ in range(4): # _ signifies, that loop iterable is not used
    print("Hello")
for c in "Potatoes":
    print(c)
for i in range(1,101): # we can add start to range
    print(i, end=",")
print("")
for i in range(1,20,3): # we can add step as well
    print(i, end=":::")
print("")
for item in ["car","tv","money","kids"]:
    print("Working with",item)
    
for n in range(10):
    if n % 2 == 0:
        print("Got even number!",n)
    else:
        print("How odd", n)


for i in range(5): # outer loop
    for j in range(5): #inner loop
        print(i,j)
    
for i in range(2):
    print(i)
    i -= 150
    print(i)