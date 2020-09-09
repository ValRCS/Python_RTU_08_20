fizz = 3
buzz = 5
for x in range(1,21):
    z=""
    if x%fizz==0:
        z+="Fizz"
    if x%buzz==0:
        z+="Buzz"
    if z=="":
        z=x   
    
    print(z)
