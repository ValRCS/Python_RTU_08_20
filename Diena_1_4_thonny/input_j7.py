# handling user input
# Python has built in input function
name = input("What is your name friend? ")
print(f"Cool your name is {name}! I like it!")

print("Enter your favorite city")
# print by default finishes with newline
city = input("->") # so input could be blank
print(f"Sooo {name} you like living in {city}?")
# for numbers we will need to perform 
# type conversion