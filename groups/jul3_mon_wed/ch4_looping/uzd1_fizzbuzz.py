# Cikli 1. uzdevums FizzBuzz
max_range = 100
fizz = 5
buzz = 7
buffer = "" # idea is to only print once
# since printing to something is actually relatively slow operation
for n in range(1, max_range + 1):
    end = ","
    if n == max_range:
        end = "\n" # could be "" 
    
    if n % fizz == 0 and n % buzz != 0:
        print("Fizz", end=end)
        buffer += "Fizz" + end
    elif n % buzz == 0 and n % fizz != 0:
        print("Buzz", end=end)
        buffer += "Buzz" + end
    elif n % buzz == 0 and n % fizz == 0:
        print("FizzBuzz", end=end)
        buffer += "FizzBuzz" + end
    else:
        print(n, end=end)
        buffer += str(n) + end # could have used f"{n}{end}"
# and I print buffer later
print("*"*40)
print(buffer)