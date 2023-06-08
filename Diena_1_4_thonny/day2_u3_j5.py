# exercise 3
 
# Prompt for temperature in Celsius
try:
    print("Program to convert Celsius to Farenheit")
    celsius = float(input("Enter the temperature in Celsius ℃: "))
    # as soon as we get error in this block we transfer to except
    print("This will not print on error")
except ValueError:
    print("bad input")
    # we should end the program here or figure out a way to return to try again
    # this would be nice in a loop
    # one way would be to set up some default ...
    print("Sticking with default 36.6")
    celsius = 36.6
 
# Convert Celsius to Fahrenheit
fahrenheit = 32 + celsius * (9/5)
 
# Print the temperature in Fahrenheit
print("The temperature in Fahrenheit is:", round(fahrenheit,2))
print(f"Farenheit temperature is {fahrenheit:.2f} ℉ ")