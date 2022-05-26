# Uzd 1
fizz = 3
buzz = 5
start = 1
stop = 40
for n in range(start, stop+1):
    end = ","
    if n == stop:
        end = "\n"  # back to default newline
        
    if n%fizz == 0 and n%buzz == 0:
        print("FizzBuzz", end=end)
    elif n%fizz == 0:
        print("Fizz", end=end)
    elif n%buzz == 0:
        print("Buzz", end=end)
    else:
        print(n, end=end)