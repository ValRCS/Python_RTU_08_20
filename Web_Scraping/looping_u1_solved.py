start = 1
stop = 100

for n in range(start, stop+1):
    end = ","
    if n % 5 == 0 and n % 7 != 0:
        print("Fizz", end=end)
    elif n % 5 != 0 and n % 7 == 0:
        print("Buzz", end=end)
    elif n % 5 == 0 and n % 7 == 0:
        print("FizzBuzz", end=end)
    else:
        print(f"{n}", end=end)

# we could have done this by checking if n is divisible by 5 and 7 first
# and then by 5 and 7 separately
print() # default end is newline
print("*"* 20)

for n in range(start, stop+1):
    end = ","
    if n == stop:
        end = "\nFinished Whew!\n"
    
    if n % 5 == 0 and n % 7 == 0:
        print("FizzBuzz", end=end)
    elif n % 5 == 0:
        print("Fizz", end=end)
    elif n % 7 == 0:
        print("Buzz", end=end)
    else:
        print(f"{n}", end=end)