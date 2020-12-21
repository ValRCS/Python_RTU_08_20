number=int(input("Please enter a whole number:"))
i=1
end = int(number**0.5)+1
while i < end:
    i+=1
    if number % i != 0:
        continue
    if number % i == 0:
        print(f"Number {number} is not a prime number it divides by {i}")
        break
else:
    print(f"Number {number} is a prime number")