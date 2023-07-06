
while True:
    try:
        temperature = float(input("Enter Temperature: "))
        break
    except ValueError:
        print("Please enter a floating point value")
 
if temperature < 35:
    print("Not too cold?")
elif temperature <= 37: # this is optional and temperature >= 35:
    print("OK") 
else: # so over 37 guaranteed
    print("illness is possible")
    
