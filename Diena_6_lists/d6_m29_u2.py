# 2.uzd.cubes
 
cubes=[]
while True:
    try:
        n1=int(input("Please enter number1: "))
        n2=int(input("Please enter number2: "))
        break
    except ValueError:
        print("That's not a integer number! try again")

step = 1 if n1 < n2 else -1 # so if n1 < n2 we will step 1, if n1 > n2 we will step -1
# same as above line
# if n1 < n2:
#     step = 1
# else:
#     step = -1

for n in range(n1, n2+step, step):
    cube=n**3
    print(f"{n} cubed: {cube}")
    cubes.append(cube)

print(f"All Cubes for this exercise= {cubes}")
 
print()