     
#Uzdevums1
temp = float(input("Enter your temperature "))

# with elif and else we only get one path/case running
if temp < 35:
    print("Isn`t it too cold?")
# elif 35 <= temp <= 37: # 35 <= temp and temp <= 37
elif temp <= 37: # since we already checked for 35 this will cover 35 to 37    
    print("Everything OK!")
else:
    print("Probably chills")

# without elif you need to explicitly cover all cases
# we could potentially get all 3 paths/cases running 
if temp < 35:
    print("Jums nav pārāk auksti?")
if temp <= 37 and temp >= 35:
    print("Viss kārtība! Jūsu temperatūra ir normāla!")
if temp > 37:
    print("Jums ir drudzis!")
    